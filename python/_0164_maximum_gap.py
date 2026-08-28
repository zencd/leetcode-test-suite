# 164. Maximum Gap
# https://leetcode.com/problems/maximum-gap/
# Medium

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        self.assertEqual(self.solution.maximumGap([3, 6, 9, 1]), 3)

    def test_example_two(self):
        self.assertEqual(self.solution.maximumGap([10]), 0)

    def test_empty_list(self):
        self.assertEqual(self.solution.maximumGap([]), 0)

    def test_two_elements(self):
        self.assertEqual(self.solution.maximumGap([1, 2]), 1)

    def test_two_elements_same(self):
        self.assertEqual(self.solution.maximumGap([5, 5]), 0)

    def test_all_same(self):
        self.assertEqual(self.solution.maximumGap([3, 3, 3, 3]), 0)

    def test_two_same_elements(self):
        self.assertEqual(self.solution.maximumGap([7, 7]), 0)

    def test_zeros(self):
        self.assertEqual(self.solution.maximumGap([0, 0]), 0)

    def test_zero_and_max(self):
        self.assertEqual(self.solution.maximumGap([0, 10**9]), 10**9)

    def test_consecutive(self):
        self.assertEqual(self.solution.maximumGap([1, 2, 3, 4, 5]), 1)

    def test_reverse_sorted(self):
        self.assertEqual(self.solution.maximumGap([9, 6, 3, 1]), 3)

    def test_duplicates(self):
        self.assertEqual(self.solution.maximumGap([4, 7, 7, 7, 10]), 3)

    def test_gap_between_buckets(self):
        self.assertEqual(self.solution.maximumGap([0, 1000]), 1000)

    def test_randomish(self):
        self.assertEqual(self.solution.maximumGap([1, 3, 5, 100, 102, 103]), 95)

    def test_sorted_input(self):
        self.assertEqual(self.solution.maximumGap([1, 3, 7, 15]), 8)

    def test_big_values(self):
        big = 10**9
        self.assertEqual(self.solution.maximumGap([0, big // 2, big]), big // 2)

    def test_large_array(self):
        nums = list(range(0, 100000, 2))
        self.assertEqual(self.solution.maximumGap(nums), 2)

    def test_large_array_duplicates(self):
        nums = [1000] * 50000 + list(range(1001, 150001))
        self.assertEqual(self.solution.maximumGap(nums), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Sorting, Bucket Sort, Radix Sort, Pigeonhole Principle
