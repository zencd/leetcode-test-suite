# 381. Insert Delete GetRandom O(1) - Duplicates allowed
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# Hard

import random as _random


class RandomizedCollection:
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
    def test_example_from_description(self):
        c = RandomizedCollection()
        self.assertTrue(c.insert(1))
        self.assertFalse(c.insert(1))
        self.assertTrue(c.insert(2))
        self.assertIn(c.getRandom(), (1, 2))
        self.assertTrue(c.remove(1))
        self.assertIn(c.getRandom(), (1, 2))

    def test_insert_first_and_duplicate(self):
        c = RandomizedCollection()
        self.assertTrue(c.insert(7))
        self.assertFalse(c.insert(7))
        self.assertFalse(c.insert(7))

    def test_remove_nonexistent(self):
        c = RandomizedCollection()
        self.assertFalse(c.remove(10))
        c.insert(5)
        self.assertFalse(c.remove(10))

    def test_insert_after_remove(self):
        c = RandomizedCollection()
        self.assertTrue(c.insert(3))
        self.assertTrue(c.remove(3))
        self.assertFalse(c.remove(3))
        self.assertTrue(c.insert(3))
        self.assertFalse(c.insert(3))
        self.assertFalse(c.remove(99))

    def test_remove_all_duplicates_one_by_one(self):
        c = RandomizedCollection()
        for i in range(5):
            c.insert(42)
        for i in range(4):
            self.assertTrue(c.remove(42))
        self.assertTrue(c.remove(42))
        self.assertFalse(c.remove(42))

    def test_remove_middle_element(self):
        c = RandomizedCollection()
        c.insert(1)
        c.insert(2)
        c.insert(3)
        c.insert(4)
        self.assertTrue(c.remove(2))
        self.assertTrue(c.remove(4))
        self.assertFalse(c.remove(2))
        self.assertTrue(c.remove(1))
        self.assertTrue(c.remove(3))

    def test_remove_last_element(self):
        c = RandomizedCollection()
        c.insert(1)
        c.insert(2)
        c.insert(3)
        self.assertTrue(c.remove(3))
        self.assertFalse(c.remove(3))
        self.assertTrue(c.remove(1))
        self.assertTrue(c.remove(2))

    def test_negative_values(self):
        c = RandomizedCollection()
        self.assertTrue(c.insert(-(2**31)))
        self.assertFalse(c.insert(-(2**31)))
        self.assertTrue(c.insert(2**31 - 1))
        self.assertTrue(c.remove(-(2**31)))
        self.assertTrue(c.remove(-(2**31)))
        self.assertTrue(c.remove(2**31 - 1))
        self.assertFalse(c.remove(-(2**31)))

    def test_zero_value(self):
        c = RandomizedCollection()
        self.assertTrue(c.insert(0))
        self.assertFalse(c.insert(0))
        self.assertTrue(c.remove(0))
        self.assertTrue(c.remove(0))
        self.assertFalse(c.remove(0))

    def test_random_returns_existing_elements(self):
        c = RandomizedCollection()
        for v in (1, 1, 2, 2, 2, 3):
            c.insert(v)
        for _ in range(100):
            self.assertIn(c.getRandom(), (1, 2, 3))

    def test_random_distribution(self):
        c = RandomizedCollection()
        c.insert(1)
        c.insert(1)
        c.insert(1)
        c.insert(2)
        counts = {1: 0, 2: 0}
        for _ in range(9000):
            counts[c.getRandom()] += 1
        self.assertAlmostEqual(counts[1] / counts[2], 3, delta=0.3)

    def test_getrandom_single_element(self):
        c = RandomizedCollection()
        c.insert(9)
        for _ in range(20):
            self.assertEqual(c.getRandom(), 9)

    def test_interleaved_operations_consistency(self):
        c = RandomizedCollection()
        expected_multiset = {}
        ops = [
            ("insert", 1),
            ("insert", 2),
            ("insert", 1),
            ("remove", 1),
            ("insert", 3),
            ("remove", 2),
            ("remove", 1),
            ("insert", 2),
            ("insert", 4),
            ("remove", 4),
            ("insert", 4),
            ("remove", 3),
            ("remove", 4),
            ("insert", 5),
        ]
        for op, v in ops:
            if op == "insert":
                result = c.insert(v)
                expected_multiset[v] = expected_multiset.get(v, 0) + 1
                self.assertEqual(result, expected_multiset[v] == 1)
            else:
                result = c.remove(v)
                count = expected_multiset.get(v, 0)
                self.assertEqual(result, count > 0)
                if count > 0:
                    expected_multiset[v] = count - 1
        for _ in range(50):
            self.assertIn(c.getRandom(), expected_multiset.keys())

    def test_remove_single_occurrence(self):
        c = RandomizedCollection()
        self.assertTrue(c.insert(11))
        self.assertTrue(c.remove(11))
        self.assertFalse(c.remove(11))
        self.assertTrue(c.insert(11))
        self.assertFalse(c.insert(11) is None)

    def test_many_values(self):
        c = RandomizedCollection()
        vals = list(range(100))
        for v in vals:
            self.assertTrue(c.insert(v))
        for v in range(0, 100, 2):
            self.assertTrue(c.remove(v))
        self.assertEqual(len(c.values), 50)
        for _ in range(50):
            val = c.getRandom()
            self.assertIn(val, vals)
            self.assertNotIn(val, set(range(0, 100, 2)))

    def test_reinsert_after_full_removal(self):
        c = RandomizedCollection()
        c.insert(1)
        c.insert(2)
        c.remove(1)
        c.remove(2)
        self.assertTrue(c.insert(1))
        self.assertFalse(c.insert(1))
        self.assertTrue(c.insert(2))
        self.assertTrue(c.remove(1))
        self.assertTrue(c.remove(2))
        self.assertTrue(c.insert(7))
        self.assertEqual(c.getRandom(), 7)

    def test_internal_structure_invariant(self):
        c = RandomizedCollection()
        import random

        random.seed(1234)
        ops = []
        for _ in range(2000):
            v = random.randint(0, 5)
            if random.random() < 0.5:
                c.insert(v)
                ops.append("insert")
            else:
                c.remove(v)
                ops.append("remove")
        for _ in range(50):
            self.assertIn(c.getRandom(), range(6))
        total = sum(len(s) for s in c.val_to_indices.values())
        self.assertEqual(total, len(c.values))
        for v, idxs in c.val_to_indices.items():
            for i in idxs:
                self.assertEqual(c.values[i], v)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Math, Design, Randomized
