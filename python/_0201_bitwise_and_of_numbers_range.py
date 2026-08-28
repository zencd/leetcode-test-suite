# 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Medium

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(5, 7), 4)

    def test_example_2(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(0, 0), 0)

    def test_example_3(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(1, 2147483647), 0)

    def test_left_equals_right(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(10, 10), 10)

    def test_single_zero(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(0, 5), 0)

    def test_small_range(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(2, 3), 2)

    def test_full_ones_range(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(7, 9), 0)

    def test_large_range(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(2147483646, 2147483647), 2147483646)

    def test_max_range(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(0, 2147483647), 0)

    def test_powers_of_two(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(8, 16), 0)

    def test_same_bit_length_range(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(20, 23), 20)

    def test_single_element_zero_to_one(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(0, 1), 0)

    def test_moderate_range(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(100, 113), 96)

    def test_bit_boundary(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(4, 8), 0)

    def test_max_values_equal(self):
        self.assertEqual(self.sol.rangeBitwiseAnd(2147483647, 2147483647), 2147483647)


if __name__ == "__main__":
    unittest.main()

# Tags: Bit Manipulation
