# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/
# Medium

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.findPeakElement([1, 2, 3, 1]), 2)

    def test_example_2(self):
        result = self.sol.findPeakElement([1, 2, 1, 3, 5, 6, 4])
        self.assertIn(result, (1, 5))

    def test_single_element(self):
        self.assertEqual(self.sol.findPeakElement([5]), 0)
        self.assertEqual(self.sol.findPeakElement([0]), 0)
        self.assertEqual(self.sol.findPeakElement([-100]), 0)

    def test_two_elements_left_peak(self):
        self.assertEqual(self.sol.findPeakElement([5, 1]), 0)

    def test_two_elements_right_peak(self):
        self.assertEqual(self.sol.findPeakElement([1, 5]), 1)

    def test_peak_at_left_edge(self):
        self.assertEqual(self.sol.findPeakElement([5, 4, 3, 2, 1]), 0)

    def test_peak_at_right_edge(self):
        self.assertEqual(self.sol.findPeakElement([1, 2, 3, 4, 5]), 4)

    def assert_valid_peak(self, nums):
        result = self.sol.findPeakElement(nums)
        left_ok = result == 0 or nums[result] > nums[result - 1]
        right_ok = result == len(nums) - 1 or nums[result] > nums[result + 1]
        self.assertTrue(left_ok and right_ok)

    def test_two_peaks(self):
        self.assert_valid_peak([1, 3, 1, 3, 1])
        self.assert_valid_peak([3, 1, 3, 1, 3])

    def test_valley(self):
        self.assert_valid_peak([3, 1, 2, 1, 3])

    def test_negative_numbers(self):
        self.assertEqual(self.sol.findPeakElement([-3, -1, -2, -5]), 1)

    def test_negative_left_positive_right(self):
        self.assertEqual(self.sol.findPeakElement([-5, -2, 3, 1]), 2)

    def test_extreme_int_values(self):
        self.assertEqual(self.sol.findPeakElement([2**31 - 1, -(2**31)]), 0)
        self.assertEqual(self.sol.findPeakElement([-(2**31), 2**31 - 2]), 1)

    def test_zigzag(self):
        self.assertEqual(self.sol.findPeakElement([1, 5, 2, 6, 3, 7, 4]), 1)

    def test_larger_array(self):
        nums = [i % 17 + 1 for i in range(1000)]
        self.assert_valid_peak(nums)

    def test_length_three_variants(self):
        for arr, expected in [([3, 2, 1], 0), ([1, 2, 3], 2), ([2, 3, 1], 1)]:
            self.assertEqual(self.sol.findPeakElement(arr), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search
