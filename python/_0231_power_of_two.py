# 231. Power of Two
# https://leetcode.com/problems/power-of-two/
# Easy

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zero(self):
        self.assertFalse(self.sol.isPowerOfTwo(0))

    def test_one_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(1))

    def test_two_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(2))

    def test_three_not_power_of_two(self):
        self.assertFalse(self.sol.isPowerOfTwo(3))

    def test_four_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(4))

    def test_sixteen_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(16))

    def test_sixteen_plus_one(self):
        self.assertFalse(self.sol.isPowerOfTwo(17))

    def test_eight_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(8))

    def test_twenty_seven_not_power_of_two(self):
        self.assertFalse(self.sol.isPowerOfTwo(27))

    def test_sixty_four_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(64))

    def test_sixty_three_not_power_of_two(self):
        self.assertFalse(self.sol.isPowerOfTwo(63))

    def test_sixty_five_not_power_of_two(self):
        self.assertFalse(self.sol.isPowerOfTwo(65))

    def test_twelve_eight_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(128))

    def test_two_fifty_six_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(256))

    def test_five_twelve_eight_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(512))

    def test_one_thousand_twenty_four_is_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(1024))

    def test_min_int_not_power_of_two(self):
        self.assertFalse(self.sol.isPowerOfTwo(-2147483648))

    def test_max_int_not_power_of_two(self):
        self.assertFalse(self.sol.isPowerOfTwo(2147483647))

    def test_max_int_minus_one_not_power_of_two(self):
        self.assertFalse(self.sol.isPowerOfTwo(2147483646))

    def test_negative_one(self):
        self.assertFalse(self.sol.isPowerOfTwo(-1))

    def test_negative_two(self):
        self.assertFalse(self.sol.isPowerOfTwo(-2))

    def test_negative_power_of_two(self):
        self.assertFalse(self.sol.isPowerOfTwo(-8))

    def test_large_power_of_two(self):
        self.assertTrue(self.sol.isPowerOfTwo(1 << 62))

    def test_large_power_of_two_plus_one(self):
        self.assertFalse(self.sol.isPowerOfTwo((1 << 62) + 1))

    def test_even_non_power(self):
        self.assertFalse(self.sol.isPowerOfTwo(372))

    def test_seven_hundred_seventy_six_plus_one(self):
        self.assertFalse(self.sol.isPowerOfTwo(778))

    def test_powers_of_two_range(self):
        for i in range(0, 33):
            self.assertTrue(self.sol.isPowerOfTwo(1 << i))

    def test_non_powers_near_powers(self):
        for i in range(1, 32):
            base = 1 << i
            if i > 1:
                self.assertFalse(self.sol.isPowerOfTwo(base - 1))
            self.assertFalse(self.sol.isPowerOfTwo(base + 1))


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Bit Manipulation, Recursion
