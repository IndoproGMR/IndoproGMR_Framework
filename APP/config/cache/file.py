import os
import json
from .converter_Cache import convert_from_cache, convert_to_cache


class FileCache:
    def __init__(self, cache_file_path):
        self.cache_file_path = cache_file_path
        self.cache_data = self.load_cache()

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
        with open(self.cache_file_path, "w") as file:
            json.dump(self.cache_data, file, indent=2)

    def cache_get(self, key):
        result = self.cache_data.get(key)
        if result is not None:
            result = convert_from_cache(result)
        return result

    def cache_set(self, key, value, ttl=None):
        self.cache_data[key] = convert_to_cache(value)
        self.save_cache()

    def cache_delete(self, key):
        if key in self.cache_data:
            del self.cache_data[key]
            self.save_cache()

    # def _convert_to_cache(self, value):
    #     # Mengonversi nilai ke dalam bentuk yang sesuai untuk disimpan di cache
    #     return json.dumps(value)

    # def _convert_from_cache(self, value):
    #     # Mengonversi nilai dari bentuk yang disimpan di cache ke bentuk semula
    #     return json.loads(value)
