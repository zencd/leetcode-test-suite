# 477. Total Hamming Distance
# https://leetcode.com/problems/total-hamming-distance/
# Medium

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.totalHammingDistance([4, 14, 2]), 6)

    def test_example_2(self):
        self.assertEqual(self.sol.totalHammingDistance([4, 14, 4]), 4)

    def test_single_element(self):
        self.assertEqual(self.sol.totalHammingDistance([5]), 0)

    def test_two_elements(self):
        self.assertEqual(self.sol.totalHammingDistance([1, 2]), 2)

    def test_identical_elements(self):
        self.assertEqual(self.sol.totalHammingDistance([7, 7, 7]), 0)

    def test_all_zeros(self):
        self.assertEqual(self.sol.totalHammingDistance([0, 0, 0]), 0)

    def test_zero_and_one(self):
        self.assertEqual(self.sol.totalHammingDistance([0, 1]), 1)

    def test_max_value_bits(self):
        self.assertEqual(self.sol.totalHammingDistance([0, 2**30]), 1)

    def test_two_max_values(self):
        self.assertEqual(self.sol.totalHammingDistance([10**9, 10**9]), 0)

    def test_mixed_values(self):
        self.assertEqual(self.sol.totalHammingDistance([1, 2, 3, 4, 5]), 18)

    def test_larger_range(self):
        nums = list(range(1000))
        expected = sum(bin(a ^ b).count("1") for i, a in enumerate(nums) for b in nums[i + 1 :])
        self.assertEqual(self.sol.totalHammingDistance(nums), expected)

    def test_dups_and_zeros(self):
        self.assertEqual(self.sol.totalHammingDistance([0, 0, 1, 1]), 4)

    def test_high_and_low_bits(self):
        self.assertEqual(self.sol.totalHammingDistance([1, 8]), 2)

    def test_bit30_only_difference(self):
        self.assertEqual(self.sol.totalHammingDistance([2**30, 0, 2**30]), 2)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Bit Manipulation
