# 307. Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/
# Medium

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        raise Exception("Not solved yet")

    def update(self, index: int, val: int) -> None:
        raise Exception("Not solved yet")

    def sumRange(self, left: int, right: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example(self):
        obj = NumArray([1, 3, 5])
        self.assertEqual(obj.sumRange(0, 2), 9)
        obj.update(1, 2)
        self.assertEqual(obj.sumRange(0, 2), 8)

    def test_single_element(self):
        obj = NumArray([42])
        self.assertEqual(obj.sumRange(0, 0), 42)
        obj.update(0, -100)
        self.assertEqual(obj.sumRange(0, 0), -100)

    def test_sum_single_index(self):
        obj = NumArray([1, 2, 3, 4, 5])
        for i in range(5):
            self.assertEqual(obj.sumRange(i, i), i + 1)

    def test_update_to_same_value(self):
        obj = NumArray([1, 2, 3])
        obj.update(1, 2)
        self.assertEqual(obj.sumRange(0, 2), 6)

    def test_update_negative_values(self):
        obj = NumArray([0, 0, 0])
        obj.update(0, -100)
        obj.update(2, 100)
        self.assertEqual(obj.sumRange(0, 2), 0)

    def test_all_ones(self):
        obj = NumArray([1] * 10)
        self.assertEqual(obj.sumRange(0, 9), 10)
        self.assertEqual(obj.sumRange(2, 7), 6)

    def test_update_multiple_updates_same_index(self):
        obj = NumArray([1, 1, 1])
        obj.update(0, 10)
        obj.update(0, 20)
        obj.update(0, 30)
        self.assertEqual(obj.sumRange(0, 0), 30)
        self.assertEqual(obj.sumRange(0, 2), 32)

    def test_update_all_elements(self):
        obj = NumArray([1, 2, 3, 4])
        vals = [10, 20, 30, 40]
        for i, v in enumerate(vals):
            obj.update(i, v)
        self.assertEqual(obj.sumRange(0, 3), 100)
        self.assertEqual(obj.sumRange(1, 2), 50)

    def test_interleaved_updates_and_queries(self):
        obj = NumArray([5, 5, 5, 5, 5])
        seq = [
            ("sum", 0, 4, 25),
            ("upd", 2, 7, None),
            ("sum", 1, 3, 17),
            ("upd", 0, 1, None),
            ("sum", 2, 4, 17),
            ("upd", 4, 0, None),
            ("sum", 0, 4, 18),
            ("sum", 4, 4, 0),
            ("upd", 4, 100, None),
            ("sum", 3, 4, 105),
        ]
        for op, a, b, expected in seq:
            if op == "sum":
                self.assertEqual(obj.sumRange(a, b), expected)
            else:
                obj.update(a, b)

    def test_larger_array(self):
        arr = [i % 7 - 3 for i in range(50)]
        obj = NumArray(arr)
        self.assertEqual(obj.sumRange(0, 49), sum(arr))
        self.assertEqual(obj.sumRange(10, 20), sum(arr[10:21]))
        obj.update(25, 999)
        self.assertEqual(obj.sumRange(0, 49), sum(arr) + 999 - (25 % 7 - 3))

    def test_powers_of_two_boundaries(self):
        n = 16
        arr = [1] * n
        obj = NumArray(arr)
        for i in range(n):
            self.assertEqual(obj.sumRange(i, n - 1), n - i)
            self.assertEqual(obj.sumRange(0, i), i + 1)
            self.assertEqual(obj.sumRange(i, i), 1)
        for i in range(n):
            obj.update(i, -1)
            expected_total = (-1) * (i + 1) + 1 * (n - i - 1)
            self.assertEqual(obj.sumRange(0, n - 1), expected_total)
            self.assertEqual(obj.sumRange(i, i), -1)

    def test_two_elements(self):
        obj = NumArray([10, -20])
        self.assertEqual(obj.sumRange(0, 1), -10)
        obj.update(1, 30)
        self.assertEqual(obj.sumRange(0, 1), 40)
        obj.update(0, -1)
        self.assertEqual(obj.sumRange(1, 1), 30)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Divide and Conquer, Design, Binary Indexed Tree, Segment Tree, Sqrt Decomposition
