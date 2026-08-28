# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Medium

from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


class TestMaxSubArray(unittest.TestCase):
    def test_single_positive(self):
        self.assertEqual(Solution().maxSubArray([1]), 1)

    def test_single_negative(self):
        self.assertEqual(Solution().maxSubArray([-5]), -5)

    def test_single_zero(self):
        self.assertEqual(Solution().maxSubArray([0]), 0)

    def test_example1(self):
        self.assertEqual(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_example2(self):
        self.assertEqual(Solution().maxSubArray([1]), 1)

    def test_example3(self):
        self.assertEqual(Solution().maxSubArray([5, 4, -1, 7, 8]), 23)

    def test_all_negative(self):
        self.assertEqual(Solution().maxSubArray([-3, -2, -5, -1]), -1)

    def test_all_same_negative(self):
        self.assertEqual(Solution().maxSubArray([-7, -7, -7]), -7)

    def test_all_zeros(self):
        self.assertEqual(Solution().maxSubArray([0, 0, 0]), 0)

    def test_all_positive(self):
        self.assertEqual(Solution().maxSubArray([1, 2, 3, 4]), 10)

    def test_mixed(self):
        self.assertEqual(Solution().maxSubArray([-1, 2, -3, 4, -5]), 4)

    def test_positive_middle(self):
        self.assertEqual(Solution().maxSubArray([-2, -3, 5, -1, -2]), 5)

    def test_max_at_start(self):
        self.assertEqual(Solution().maxSubArray([10, -1, -2, -3]), 10)

    def test_max_at_end(self):
        self.assertEqual(Solution().maxSubArray([-3, -2, -1, 10]), 10)

    def test_all_negative_except_one(self):
        self.assertEqual(Solution().maxSubArray([-1, -2, 3, -4, -5]), 3)

    def test_two_elements(self):
        self.assertEqual(Solution().maxSubArray([-1, 2]), 2)
        self.assertEqual(Solution().maxSubArray([2, -1]), 2)
        self.assertEqual(Solution().maxSubArray([-1, -2]), -1)
        self.assertEqual(Solution().maxSubArray([3, 4]), 7)

    def test_zero_in_between(self):
        self.assertEqual(Solution().maxSubArray([-2, 0, -1]), 0)

    def test_zeros_around_positive(self):
        self.assertEqual(Solution().maxSubArray([0, 1, 0]), 1)

    def test_larger_values(self):
        self.assertEqual(Solution().maxSubArray([-10000, 10000]), 10000)

    def test_large_array(self):
        nums = [10000] * 100000
        self.assertEqual(Solution().maxSubArray(nums), 10000 * 100000)

    def test_alternating(self):
        self.assertEqual(Solution().maxSubArray([1, -1, 1, -1, 1]), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Divide and Conquer, Dynamic Programming
