# vim:fileencoding=utf-8:foldmethod=marker

# System {{{


import asyncio
import datetime
import os
import json
from pathlib import Path


from .converter_Cache import convert_from_cache, convert_to_cache
from APP.config.dotenvfile import GetEnv
from APP.config.log import LogProses

from APP.config.manager import filemanager

# file_path = GetEnv("cache_local_path", "tmp/cache").str()

fileproses = filemanager.create("")


class FileCache:
    def __init__(self):
        file_path = GetEnv("cache_local_path", "tmp/cache").str()

        # file_path = "tmp/cache/"

        self.cache_file_path = Path(file_path)
        try:
            asyncio.create_task(fileproses.SaveFolder(file_path))

            # Path(file_path).mkdir(parents=True, exist_ok=True)
            self.file_path = file_path
            if GetEnv("cache.auto_clear", "False").str() != "True":
                try:
                    asyncio.create_task(fileproses.DeleteFolder(f"{file_path}/*"))

                    # Hapus folder cache jika sudah ada
                    # if os.path.exists(self.cache_file_path):
                    #     num_deleted_files = self.clear_cache_folder()
                    #     LogProses(
                    #         f"{num_deleted_files} files deleted from cache folder"
                    #     )

                except Exception as e:
                    LogProses(f"Error during cache init: {e}")

        except Exception as e:
            LogProses(f"Error during cache init: {e}")

    # def clear_cache_folder(self):
    #     num_deleted_files = 0
    #     # Hapus semua file di dalam folder cache
    #     for file in os.listdir(self.cache_file_path):
    #         file_path = os.path.join(self.cache_file_path, file)
    #         try:
    #             if os.path.isfile(file_path):
    #                 os.unlink(file_path)
    #                 num_deleted_files += 1
    #         except Exception as e:
    #             LogProses(f"Error deleting file {file}: {e}")
    #     return num_deleted_files

    def get(self, key):
        if GetEnv("cache.bypass", "False").str() == "True":
            return None

        if key is None:
            return None
        key = f"{key}.json"
        cache_file = Path(self.file_path) / key

        if os.path.exists(cache_file):
            with open(cache_file, "r") as file:
                try:
                    cache_data = json.load(file)
                    cache_data = convert_from_cache(cache_data)

                    value = cache_data.get("value")
                    ttl = cache_data.get("ttl")

                    if ttl is not None and ttl < int(
                        datetime.datetime.now().timestamp()
                    ):
                        # TTL sudah kedaluwarsa
                        try:
                            os.remove(cache_file)
                        except Exception as e:
                            LogProses(f"Error removing cache file: {e}")
                            return None
                        return None
                    return value

                except json.JSONDecodeError as e:
                    LogProses(f"Error decoding cache: {e}")
                    return None
        else:
            return None

    def add(self, key, value, ttl=None):
        key = f"{key}.json"
        cache_file = Path(self.file_path) / key
        try:
            cache_file.touch(exist_ok=True)
        except Exception as e:
            LogProses(f"Error creating cache file: {e}")
            return False

        try:
            # Menyimpan value dan TTL sebagai objek JSON
            cache_data = {"value": value}
            if ttl is not None:
                ttl = int(ttl) + int(datetime.datetime.now().timestamp())
                cache_data["ttl"] = ttl

            cache_data = convert_to_cache(cache_data)

            with open(cache_file, "w") as file:
                json.dump(cache_data, file, indent=2)
            return True

        except Exception as e:
            LogProses(f"Error saving cache: {e}")
            return False

    def delete(self, key):
        try:
            key = f"{key}.json"
            cache_file = Path(self.file_path) / key
            # print(cache_file)
            os.remove(cache_file)
            return True
        except Exception as e:
            LogProses(f"Error deleting cache: {e}")
            return False


# }}}
