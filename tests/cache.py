import time
import unittest
import sys
import os

sys.path.append(os.getcwd())  # APP is one level up
from APP.config.cachemanager import create_cache

# cache_manager = CacheManager()
cache_manager = create_cache()


class TestRedisCacheFunctions(unittest.TestCase):
    def test_cache_set_and_get(self):
        key = "test_key"
        value = [1, 2, 3, "four", {"five": 5}]

        # Test cache_set
        cache_manager.cache_set(key, value)

        # Test cache_get
        result = cache_manager.cache_get(key)
        # Memastikan bahwa nilai yang diambil kembali setelah disimpan sama dengan nilai yang disimpan
        # self.assertEqual(json.loads(result), value, "Cache set and get failed")  # type: ignore
        self.assertEqual(result, value, "Cache set and get failed")  # type: ignore

    def test_cachedelete(self):
        key = "test_key"
        value = [1, 2, 3, "four", {"five": 5}]

        # Set nilai ke dalam cache
        cache_manager.cache_set(key, value)

        # Test cache_delete
        cache_manager.cache_delete(key)

        # Memastikan bahwa nilai telah dihapus dari cache
        result = cache_manager.cache_get(key)
        self.assertIsNone(result, "Cache delete failed")

    def test_cache_get_missing(self):
        key = "missingkey"
        self.assertIsNone(
            cache_manager.cache_get(key), "cache_get for missing key failed"
        )

    def test_cache_set(self):
        key = "testkey"
        value = "testvalue"
        cache_manager.cache_set(key, value)
        self.assertEqual(cache_manager.cache_get(key), value, "Cache set failed")

    def test_cache_delete(self):
        key = "testkey"
        value = "testvalue"
        cache_manager.cache_set(key, value)
        cache_manager.cache_delete(key)

        # Menggunakan self.assertIsNone dengan benar
        result = cache_manager.cache_get(key)
        self.assertIsNone(result, "Cache delete failed")

    def test_cache_set_string(self):
        key = "test"
        value = "value"
        cache_manager.cache_set(key, value)
        self.assertEqual(cache_manager.cache_get(key), value)

    def test_cache_set_int(self):
        key = "test"
        value = 123
        cache_manager.cache_set(key, value)
        self.assertEqual(cache_manager.cache_get(key), value)

    def test_cache_set_list(self):
        key = "test"
        value = [1, 2, 3]
        cache_manager.cache_set(key, value)
        self.assertEqual(cache_manager.cache_get(key), value)

    def test_cache_set_ttl(self):
        key = "test"
        value = "value"
        ttl = 1
        cache_manager.cache_set(key, value, ttl)
        self.assertEqual(cache_manager.cache_get(key), value)
        time.sleep(ttl + 2)
        self.assertIsNone(cache_manager.cache_get(key))

    def test_cache_delete_missing(self):
        cache_manager.cache_delete("missing")  # should not raise error


if __name__ == "__main__":
    unittest.main()
