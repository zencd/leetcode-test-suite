# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Easy

import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        raise Exception("Not solved yet")


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(121))

    def test_single_digit(self):
        for d in range(10):
            self.assertTrue(self.solution.isPalindrome(d))

    def test_negative_numbers(self):
        for x in (-1, -10, -121, -12321):
            self.assertFalse(self.solution.isPalindrome(x))

    def test_negative_zero_absurd(self):
        self.assertTrue(self.solution.isPalindrome(0))

    def test_multiples_of_ten(self):
        for x in (10, 100, 120, 100100, 1010):
            self.assertFalse(self.solution.isPalindrome(x))

    def test_not_palindrome(self):
        for x in (12, 123, 1232, 90, 1234, 987654321):
            self.assertFalse(self.solution.isPalindrome(x))

    def test_two_digit_palindromes(self):
        for d in range(1, 10):
            self.assertTrue(self.solution.isPalindrome(d * 11))
        self.assertFalse(self.solution.isPalindrome(10))

    def test_even_length_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(1221))
        self.assertTrue(self.solution.isPalindrome(123321))
        self.assertFalse(self.solution.isPalindrome(1231))

    def test_odd_length_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(12321))
        self.assertTrue(self.solution.isPalindrome(10011001))
        self.assertFalse(self.solution.isPalindrome(1234320))

    def test_boundary_values(self):
        self.assertFalse(self.solution.isPalindrome(2147483647))
        self.assertFalse(self.solution.isPalindrome(-2147483648))

    def test_large_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(10000001))
        self.assertTrue(self.solution.isPalindrome(1234554321))
        self.assertFalse(self.solution.isPalindrome(1234567898))

    def test_zero(self):
        self.assertTrue(self.solution.isPalindrome(0))


if __name__ == "__main__":
    unittest.main()

# Tags: Math
