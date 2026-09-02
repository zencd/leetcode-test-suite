# 460. LFU Cache
# https://leetcode.com/problems/lfu-cache/
# Hard

from collections import OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        raise Exception("Not solved yet")

    def get(self, key: int) -> int:
        raise Exception("Not solved yet")

    def put(self, key: int, value: int) -> None:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_get_missing_key(self):
        cache = LFUCache(2)
        self.assertEqual(cache.get(1), -1)

    def test_basic_put_get(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

    def test_capacity_zero(self):
        cache = LFUCache(0)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), -1)

    def test_capacity_one(self):
        cache = LFUCache(1)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)

    def test_update_existing_key(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(1, 2)
        self.assertEqual(cache.get(1), 2)

    def test_put_updates_frequency(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(1, 2)
        cache.put(2, 3)
        cache.put(3, 4)
        self.assertEqual(cache.get(1), 2)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 4)

    def test_lfu_eviction(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(2), 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_tie_broken_by_lru(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_value_zero_and_key_zero(self):
        cache = LFUCache(2)
        cache.put(0, 0)
        cache.put(100000, 1000000000)
        self.assertEqual(cache.get(0), 0)
        self.assertEqual(cache.get(100000), 1000000000)

    def test_reinsert_evicted_key(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)

    def test_leetcode_example(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_many_insertions_single_capacity(self):
        cache = LFUCache(1)
        for i in range(1000):
            cache.put(i, i)
        self.assertEqual(cache.get(999), 999)
        self.assertEqual(cache.get(998), -1)

    def test_repeated_get_keeps_key_alive(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        for _ in range(5):
            cache.get(1)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Linked List, Design, Doubly-Linked List
