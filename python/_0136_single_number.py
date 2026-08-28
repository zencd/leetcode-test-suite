# 136. Single Number
# https://leetcode.com/problems/single-number/
# Easy

class Solution:
    def singleNumber(self, nums):
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.singleNumber([2, 2, 1]), 1)

    def test_example2(self):
        self.assertEqual(self.sol.singleNumber([4, 1, 2, 1, 2]), 4)

    def test_example3(self):
        self.assertEqual(self.sol.singleNumber([1]), 1)

    def test_single_zero(self):
        self.assertEqual(self.sol.singleNumber([0]), 0)

    def test_single_negative(self):
        self.assertEqual(self.sol.singleNumber([-5]), -5)

    def test_single_positive(self):
        self.assertEqual(self.sol.singleNumber([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(self.sol.singleNumber([-1, -1, -2]), -2)

    def test_negative_single(self):
        self.assertEqual(self.sol.singleNumber([1, -1, 1]), -1)

    def test_mixed_signs(self):
        self.assertEqual(self.sol.singleNumber([-3, 3, -3]), 3)

    def test_zero_pairs(self):
        self.assertEqual(self.sol.singleNumber([0, 0, 5]), 5)

    def test_zero_is_single(self):
        self.assertEqual(self.sol.singleNumber([2, 2, 0]), 0)

    def test_boundary_values(self):
        self.assertEqual(self.sol.singleNumber([30000, 30000, -30000]), -30000)

    def test_single_at_start(self):
        self.assertEqual(self.sol.singleNumber([9, 1, 1]), 9)

    def test_single_at_end(self):
        self.assertEqual(self.sol.singleNumber([1, 1, 9]), 9)

    def test_single_in_middle(self):
        self.assertEqual(self.sol.singleNumber([1, 9, 1]), 9)

    def test_duplicates_adjacent(self):
        self.assertEqual(self.sol.singleNumber([3, 3, 7]), 7)

    def test_duplicates_separated(self):
        self.assertEqual(self.sol.singleNumber([3, 5, 7, 5, 3]), 7)

    def test_repeated_pairs(self):
        self.assertEqual(self.sol.singleNumber([1, 1, 2, 2, 3, 3, 4]), 4)

    def test_large_array(self):
        nums = [2, 2] * 15000
        nums.append(42)
        self.assertEqual(self.sol.singleNumber(nums), 42)

    def test_all_pairs_except_one(self):
        nums = []
        for i in range(1, 101):
            nums.append(i)
            nums.append(i)
        nums.append(-100)
        self.assertEqual(self.sol.singleNumber(nums), -100)

    def test_two_distinct_pairs(self):
        self.assertEqual(self.sol.singleNumber([5, 5, 6, 6, 6]), 6)

    def test_three_same_with_one(self):
        nums = [1, 1, 1]
        self.assertEqual(self.sol.singleNumber(nums), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Bit Manipulation
