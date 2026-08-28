# 179. Largest Number
# https://leetcode.com/problems/largest-number/
# Medium

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.largestNumber([10, 2]), "210")

    def test_example2(self):
        self.assertEqual(self.sol.largestNumber([3, 30, 34, 5, 9]), "9534330")

    def test_all_zeros(self):
        self.assertEqual(self.sol.largestNumber([0, 0, 0]), "0")

    def test_single_zero(self):
        self.assertEqual(self.sol.largestNumber([0]), "0")

    def test_single_element(self):
        self.assertEqual(self.sol.largestNumber([7]), "7")

    def test_two_elements(self):
        self.assertEqual(self.sol.largestNumber([9, 1]), "91")
        self.assertEqual(self.sol.largestNumber([1, 9]), "91")

    def test_repeated_same_digits(self):
        self.assertEqual(self.sol.largestNumber([12, 12, 12]), "121212")

    def test_99_vs_9(self):
        self.assertEqual(self.sol.largestNumber([99, 9]), "999")

    def test_121_vs_12(self):
        self.assertEqual(self.sol.largestNumber([121, 12]), "12121")
        self.assertEqual(self.sol.largestNumber([12, 121]), "12121")

    def test_mixed_with_zeros(self):
        self.assertEqual(self.sol.largestNumber([0, 1]), "10")
        self.assertEqual(self.sol.largestNumber([1, 0]), "10")
        self.assertEqual(self.sol.largestNumber([5, 0, 3, 0]), "5300")

    def test_large_numbers(self):
        self.assertEqual(
            self.sol.largestNumber([1000000000, 1000000000]), "10000000001000000000"
        )

    def test_sort_of_powers_of_ten(self):
        self.assertEqual(self.sol.largestNumber([1, 10, 100]), "110100")

    def test_prefix_chain(self):
        self.assertEqual(self.sol.largestNumber([512, 5125, 12]), "512551212")
        self.assertEqual(
            self.sol.largestNumber([512, 5125, 12, 51250]), "51255125125012"
        )

    def test_two_digits(self):
        self.assertEqual(self.sol.largestNumber([98, 9]), "998")
        self.assertEqual(self.sol.largestNumber([9, 98]), "998")

    def test_11_vs_1(self):
        self.assertEqual(self.sol.largestNumber([11, 1]), "111")
        self.assertEqual(self.sol.largestNumber([1, 11]), "111")

    def test_known_hard_case_830(self):
        self.assertEqual(self.sol.largestNumber([8308, 830]), "8308830")

    def test_known_hard_case_343(self):
        self.assertEqual(self.sol.largestNumber([343, 34]), "34343")


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Greedy, Sorting
