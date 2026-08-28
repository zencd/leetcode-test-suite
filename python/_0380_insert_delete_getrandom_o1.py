# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Medium

import random


class RandomizedSet:
    def __init__(self):
        raise Exception("Not solved yet")

    def insert(self, val: int) -> bool:
        raise Exception("Not solved yet")

    def remove(self, val: int) -> bool:
        raise Exception("Not solved yet")

    def getRandom(self) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_insert_new_value_returns_true(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))

    def test_insert_duplicate_returns_false(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.insert(1))

    def test_remove_existing_returns_true(self):
        rs = RandomizedSet()
        rs.insert(1)
        self.assertTrue(rs.remove(1))

    def test_remove_nonexistent_returns_false(self):
        rs = RandomizedSet()
        self.assertFalse(rs.remove(1))

    def test_insert_after_remove_returns_true(self):
        rs = RandomizedSet()
        rs.insert(1)
        rs.remove(1)
        self.assertTrue(rs.insert(1))

    def test_get_random_only_element(self):
        rs = RandomizedSet()
        rs.insert(42)
        self.assertEqual(rs.getRandom(), 42)

    def test_get_random_returns_member(self):
        rs = RandomizedSet()
        for v in [1, 2, 3, 4, 5]:
            rs.insert(v)
        for _ in range(100):
            self.assertIn(rs.getRandom(), [1, 2, 3, 4, 5])

    def test_get_random_uniform_distribution(self):
        rs = RandomizedSet()
        for v in [1, 2, 3, 4]:
            rs.insert(v)
        counts = {v: 0 for v in [1, 2, 3, 4]}
        n = 4000
        for _ in range(n):
            counts[rs.getRandom()] += 1
        for v in counts:
            self.assertTrue(n * 0.1 < counts[v] < n * 0.4)

    def test_leetcode_example(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.remove(2))
        self.assertTrue(rs.insert(2))
        self.assertIn(rs.getRandom(), [1, 2])
        self.assertTrue(rs.remove(1))
        self.assertFalse(rs.insert(2))
        self.assertEqual(rs.getRandom(), 2)

    def test_remove_middle_element(self):
        rs = RandomizedSet()
        for v in [10, 20, 30]:
            rs.insert(v)
        self.assertTrue(rs.remove(20))
        self.assertIn(rs.getRandom(), [10, 30])
        self.assertFalse(rs.remove(20))
        self.assertTrue(rs.insert(20))

    def test_reinsert_removed_values(self):
        rs = RandomizedSet()
        rs.insert(1)
        rs.insert(2)
        rs.insert(3)
        rs.remove(1)
        rs.remove(2)
        self.assertEqual(rs.getRandom(), 3)
        self.assertTrue(rs.insert(99))
        self.assertIn(rs.getRandom(), [3, 99])

    def test_negative_values(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(-5))
        self.assertTrue(rs.insert(0))
        self.assertTrue(rs.insert(-2147483648))
        self.assertIn(rs.getRandom(), [-5, 0, -2147483648])
        self.assertFalse(rs.insert(-5))

    def test_int_extremes(self):
        rs = RandomizedSet()
        lo = -2147483648
        hi = 2147483647
        self.assertTrue(rs.insert(lo))
        self.assertTrue(rs.insert(hi))
        self.assertTrue(rs.remove(lo))
        self.assertEqual(rs.getRandom(), hi)
        self.assertTrue(rs.insert(lo))

    def test_remove_last_element(self):
        rs = RandomizedSet()
        rs.insert(7)
        rs.insert(8)
        self.assertTrue(rs.remove(8))
        self.assertEqual(rs.getRandom(), 7)
        self.assertTrue(rs.remove(7))
        self.assertFalse(rs.remove(7))

    def test_sequential_swaps_preserve_membership(self):
        rs = RandomizedSet()
        for v in range(10):
            self.assertTrue(rs.insert(v))
        for v in [9, 7, 3, 1]:
            self.assertTrue(rs.remove(v))
        expected = {0, 2, 4, 5, 6, 8}
        for _ in range(100):
            self.assertIn(rs.getRandom(), expected)

    def test_many_insert_remove_cycles(self):
        rs = RandomizedSet()
        for i in range(500):
            self.assertTrue(rs.insert(i))
        for i in range(0, 500, 2):
            self.assertTrue(rs.remove(i))
        for _ in range(100):
            self.assertIn(rs.getRandom(), range(1, 500, 2))
        self.assertFalse(rs.remove(498))
        self.assertFalse(rs.insert(499))
        self.assertTrue(rs.insert(1000))

    def test_randomized_stress(self):
        rs = RandomizedSet()
        reference = set()
        rng = random.Random(12345)
        for _ in range(20000):
            op = rng.randrange(3)
            if op == 0:
                v = rng.randint(-100, 100)
                expected = v not in reference
                self.assertEqual(rs.insert(v), expected)
                if expected:
                    reference.add(v)
            elif op == 1:
                v = rng.randint(-100, 100)
                expected = v in reference
                self.assertEqual(rs.remove(v), expected)
                if expected:
                    reference.discard(v)
            else:
                if reference:
                    self.assertIn(rs.getRandom(), reference)
        self.assertTrue(reference)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Math, Design, Randomized
