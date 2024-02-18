import os
import json
from .converter_Cache import convert_from_cache, convert_to_cache
from pathlib import Path

from APP.config.dotenvfile import getenvval


class FileCache:
    def __init__(self, file_path):
        file_name = "cache.json"
        self.cache_file_path = Path(file_path) / file_name
        try:
            if getenvval("cache.auto_clear", "False") == "True":
                # bila file sudah ada di maka hapus cache.json nya
                if os.path.exists(self.cache_file_path):
                    os.remove(self.cache_file_path)

            Path(file_path).mkdir(parents=True, exist_ok=True)
            self.file_path = file_path
            self.cache_data = self.load_cache()
        except Exception as e:
            print(f"Error during cache init: {e}")
            self.cache_data = {}

    def load_cache(self):
        if os.path.exists(self.cache_file_path):
            with open(self.cache_file_path, "r") as file:
                try:
                    cache_data = json.load(file)
                except json.JSONDecodeError:
                    cache_data = {}
        else:
            cache_data = {}
        return cache_data

    def save_cache(self):
        if os.path.exists(self.cache_file_path) is False:
            Path(self.file_path).mkdir(parents=True, exist_ok=True)

        with open(self.cache_file_path, "w") as file:
            json.dump(self.cache_data, file, indent=2)

        self.cache_data = self.load_cache()

    def cache_get(self, key):
        if key is None:
            return None

        result = self.cache_data.get(key)
        if result is not None:
            result = convert_from_cache(result)
        return result

    def cache_set(self, key, value, ttl=None):
        print(f"Cache set: {key} = {value}")

        self.cache_data[key] = convert_to_cache(value)
        self.save_cache()

    def cache_delete(self, key):
        if key in self.cache_data:
            del self.cache_data[key]
            self.save_cache()
