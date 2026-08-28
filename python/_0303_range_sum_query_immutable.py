# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/
# Easy

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        raise Exception("Not solved yet")

    def sumRange(self, left: int, right: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        obj = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(obj.sumRange(0, 2), 1)
        self.assertEqual(obj.sumRange(2, 5), -1)
        self.assertEqual(obj.sumRange(0, 5), -3)

    def test_single_element(self):
        obj = NumArray([42])
        self.assertEqual(obj.sumRange(0, 0), 42)

    def test_single_element_negative(self):
        obj = NumArray([-7])
        self.assertEqual(obj.sumRange(0, 0), -7)

    def test_single_element_zero(self):
        obj = NumArray([0])
        self.assertEqual(obj.sumRange(0, 0), 0)

    def test_full_range(self):
        obj = NumArray([1, 2, 3, 4, 5])
        self.assertEqual(obj.sumRange(0, 4), 15)

    def test_sub_ranges(self):
        obj = NumArray([1, 2, 3, 4, 5])
        self.assertEqual(obj.sumRange(1, 3), 9)
        self.assertEqual(obj.sumRange(2, 2), 3)
        self.assertEqual(obj.sumRange(0, 0), 1)
        self.assertEqual(obj.sumRange(4, 4), 5)

    def test_all_negative(self):
        obj = NumArray([-1, -2, -3, -4])
        self.assertEqual(obj.sumRange(0, 3), -10)
        self.assertEqual(obj.sumRange(1, 2), -5)

    def test_mixed_positive_negative(self):
        obj = NumArray([-10, 5, 3, -2, 7])
        self.assertEqual(obj.sumRange(0, 4), 3)
        self.assertEqual(obj.sumRange(2, 3), 1)
        self.assertEqual(obj.sumRange(1, 1), 5)

    def test_two_elements(self):
        obj = NumArray([8, -8])
        self.assertEqual(obj.sumRange(0, 1), 0)
        self.assertEqual(obj.sumRange(0, 0), 8)
        self.assertEqual(obj.sumRange(1, 1), -8)

    def test_repeated_elements(self):
        obj = NumArray([3, 3, 3, 3])
        self.assertEqual(obj.sumRange(0, 3), 12)
        self.assertEqual(obj.sumRange(1, 2), 6)

    def test_zeros(self):
        obj = NumArray([0, 0, 0])
        self.assertEqual(obj.sumRange(0, 2), 0)
        self.assertEqual(obj.sumRange(1, 1), 0)

    def test_large_values(self):
        obj = NumArray([-(10**5), 10**5, 10**5, -(10**5)])
        self.assertEqual(obj.sumRange(0, 3), 0)
        self.assertEqual(obj.sumRange(1, 2), 2 * 10**5)
        self.assertEqual(obj.sumRange(0, 2), 10**5)

    def test_many_queries(self):
        obj = NumArray(list(range(1, 101)))
        total = sum(range(1, 101))
        self.assertEqual(obj.sumRange(0, 99), total)
        self.assertEqual(obj.sumRange(50, 99), sum(range(51, 101)))
        self.assertEqual(obj.sumRange(0, 49), sum(range(1, 51)))
        for i in range(100):
            self.assertEqual(obj.sumRange(i, i), i + 1)

    def test_many_queries_large(self):
        import random

        random.seed(1234)
        n = 10**4
        nums = [random.randint(-(10**5), 10**5) for _ in range(n)]
        obj = NumArray(nums)
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v
        for _ in range(1000):
            left = random.randrange(n)
            right = random.randrange(left, n)
            self.assertEqual(
                obj.sumRange(left, right), prefix[right + 1] - prefix[left]
            )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Design, Prefix Sum
