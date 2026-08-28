# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/
# Medium

class _Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        raise Exception("Not solved yet")

    def get(self, key: int) -> int:
        raise Exception("Not solved yet")

    def put(self, key: int, value: int) -> None:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example_from_description(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_get_missing_key(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(1), -1)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(1, 100)
        self.assertEqual(cache.get(1), 100)

    def test_update_does_not_increase_size(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)
        self.assertEqual(len(cache.cache), 2)

    def test_get_promotes_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)

    def test_put_existing_key_promotes(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 11)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 11)
        self.assertEqual(cache.get(3), 3)

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)

    def test_capacity_one_update(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        cache.put(1, 2)
        self.assertEqual(cache.get(1), 2)
        self.assertEqual(len(cache.cache), 1)

    def test_values_and_keys_zero(self):
        cache = LRUCache(2)
        cache.put(0, 0)
        self.assertEqual(cache.get(0), 0)
        cache.put(5, 0)
        self.assertEqual(cache.get(5), 0)

    def test_frequent_gets_do_not_evict(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        for _ in range(10):
            self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 1)

    def test_many_keys_eviction_order(self):
        cache = LRUCache(3)
        for i in range(10):
            cache.put(i, i * 10)
        self.assertEqual(cache.get(7), 70)
        self.assertEqual(cache.get(8), 80)
        self.assertEqual(cache.get(9), 90)
        self.assertEqual(cache.get(6), -1)
        self.assertEqual(cache.get(5), -1)

    def test_eviction_of_lru_after_get_order(self):
        cache = LRUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), 2)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_reinsert_evicted_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        self.assertEqual(cache.get(1), -1)
        cache.put(2, 20)
        self.assertEqual(cache.get(2), 20)
        self.assertEqual(cache.get(3), 3)
        cache.put(4, 4)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_max_capacity_stress(self):
        cache = LRUCache(3000)
        for i in range(3000):
            cache.put(i, i)
        for i in range(3000):
            self.assertEqual(cache.get(i), i)
        cache.put(3000, 3000)
        self.assertEqual(cache.get(0), -1)
        self.assertEqual(cache.get(3000), 3000)

    def test_put_after_many_gets(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(2)
        cache.get(2)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(len(cache.cache), 2)

    def test_alternating_puts_gets(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(2, 22)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 22)
        cache.put(3, 33)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 22)
        self.assertEqual(cache.get(3), 33)

    def test_size_never_exceeds_capacity(self):
        cache = LRUCache(3)
        for i in range(100):
            cache.put(i % 5, i)
            self.assertLessEqual(len(cache.cache), 3)
        for i in range(100):
            cache.get(i % 7)
            self.assertLessEqual(len(cache.cache), 3)

    def test_negative_result_only_for_missing(self):
        cache = LRUCache(1)
        cache.put(9, 9)
        self.assertEqual(cache.get(8), -1)
        self.assertEqual(cache.get(9), 9)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Linked List, Design, Doubly-Linked List
