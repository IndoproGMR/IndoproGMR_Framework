import asyncio
import datetime
import os
import json


from .converter_Cache import convert_from_cache, convert_to_cache
from APP.config.dotenvfile import GetEnv
from APP.config.log import LogProses, debugProses

from APP.config.manager import filemanager


fileproses = filemanager.create("")


class FileCache:
    def __init__(self):
        file_path = GetEnv("cache_local_path", "tmp/cache").str()

        self.file_path = file_path

        if GetEnv("cache_auto_clear", "False").is_("True"):
            try:
                # await fileproses.DeleteFolder(f"{file_path}/*")
                asyncio.create_task(fileproses.DeleteFolder(f"{file_path}/*"))

            except Exception as e:
                LogProses(f"Error during cache init: {e}")

        try:
            self.cache_file_path = file_path
            # await fileproses.SaveFolder(file_path)
            asyncio.create_task(fileproses.SaveFolder(file_path))
        except Exception as e:
            LogProses(f"Error during cache init: {e}")

    async def get(self, key):
        if GetEnv("cache.bypass", "False").str() == "True":
            return None

        if key is None:
            return None

        cache_file = os.path.join(self.file_path, f"{key}.json")

        try:

            cache_data = await fileproses.ReadFile(cache_file, suspandLog=True)

            if not cache_data:
                return None

            value = cache_data.get("value")
            ttl = cache_data.get("ttl")

            if ttl is not None and ttl < int(datetime.datetime.now().timestamp()):
                await self.delete(key)
                return None
            return value

        except Exception as e:
            LogProses(f"Error tidak dapat mendapatkan key cache: {e}")
            return None

    async def add(self, key, value, ttl=None):
        try:
            key = f"{key}.json"
            cache_file = os.path.join(self.file_path, key)

            cache_data = {"value": value}
            if ttl is not None:
                ttl = int(ttl) + int(datetime.datetime.now().timestamp())
                cache_data["ttl"] = ttl

            cache_data = convert_to_cache(cache_data)

            cache_data = await fileproses.SaveFile(cache_data, cache_file)

            return True

        except Exception as e:
            LogProses(f"gagal Menyimpan cache: {e}")
            return False

    async def delete(self, key):
        try:
            key = f"{key}.json"

            await fileproses.DeleteFile(key, self.file_path, forceDelete=True)

            return True

        except Exception as e:
            LogProses(f"gagal menghapus cache: {e}")
            return False
