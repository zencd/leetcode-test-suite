# 260. Single Number III
# https://leetcode.com/problems/single-number-iii/
# Medium

from typing import List
import unittest


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assertSingleNumbers(self, nums, expected):
        self.assertEqual(sorted(self.sol.singleNumber(nums)), sorted(expected))

    def test_example_1(self):
        self.assertSingleNumbers([1, 2, 1, 3, 2, 5], [3, 5])

    def test_example_2(self):
        self.assertSingleNumbers([-1, 0], [-1, 0])

    def test_example_3(self):
        self.assertSingleNumbers([0, 1], [1, 0])

    def test_min_length_two_uniques(self):
        self.assertSingleNumbers([4, 7], [4, 7])

    def test_pairs_plus_two_uniques(self):
        self.assertSingleNumbers([5, 5, 5, 5, 6, 6, 7, 7, 8, 9], [8, 9])

    def test_many_pairs_plus_two_uniques(self):
        self.assertSingleNumbers([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7], [6, 7])

    def test_negative_numbers(self):
        self.assertSingleNumbers([-2, -2, -1, -1, -3, -4], [-4, -3])

    def test_mixed_signs(self):
        self.assertSingleNumbers([1, 1, -1, -1, 2, 2, -2, -2, 4, 5], [4, 5])

    def test_zeros_with_pairs(self):
        self.assertSingleNumbers([0, 0, 1, 1, 2, 2, 3, 3, 4, 5], [4, 5])

    def test_zero_and_one_only(self):
        self.assertSingleNumbers([0, 1], [0, 1])

    def test_max_value(self):
        big = (1 << 31) - 1
        self.assertSingleNumbers([big, big, 1, 1, big - 1, -big], [-big, big - 1])

    def test_min_value(self):
        neg_min = -(1 << 31)
        self.assertSingleNumbers(
            [neg_min, neg_min, 1, 1, neg_min + 1, 2], [2, neg_min + 1]
        )

    def test_adjacent_pair_values(self):
        self.assertSingleNumbers([8, 9, 8, 9, 10, 11], [10, 11])

    def test_result_shape(self):
        result = self.sol.singleNumber([1, 1, 2])
        self.assertEqual(len(result), 2)
        self.assertNotEqual(result[0], result[1])

    def test_result_set_match(self):
        result = self.sol.singleNumber([1, 2, 1, 3, 2, 5])
        self.assertEqual(set(result), {3, 5})

    def test_uniques_differ_in_high_bits(self):
        self.assertSingleNumbers([2, 2, 4, 4, 3, 7], [3, 7])

    def test_uniques_differ_in_low_bit(self):
        self.assertSingleNumbers([5, 5, 6, 6, 1, 2], [1, 2])

    def test_uniques_same_low_half(self):
        self.assertSingleNumbers([100, 100, 200, 200, 101, 102], [101, 102])

    def test_large_input(self):
        nums = [7, 7] * 10000 + [1, 2]
        self.assertSingleNumbers(nums, [1, 2])

    def test_uniques_equal_to_pair_values_not_allowed(self):
        self.assertSingleNumbers([13, 13, 42, 42, 137, 999], [137, 999])

    def test_three_pair_groups(self):
        self.assertSingleNumbers([10, 10, 20, 20, 30, 30, 41, 42], [41, 42])

    def test_duplicates_appear_four_times_like(self):
        self.assertSingleNumbers([3, 3, 3, 3, 5, 5, 6, 6, 7, 8], [7, 8])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Bit Manipulation
