# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Easy

class Solution:
    def isPalindrome(self, s: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1_palindrome_with_punctuation(self):
        self.assertTrue(self.sol.isPalindrome("A man, a plan, a canal: Panama"))

    def test_example2_not_palindrome(self):
        self.assertFalse(self.sol.isPalindrome("race a car"))

    def test_example3_only_whitespace(self):
        self.assertTrue(self.sol.isPalindrome(" "))

    def test_single_alnum_character(self):
        self.assertTrue(self.sol.isPalindrome("a"))

    def test_single_digit(self):
        self.assertTrue(self.sol.isPalindrome("1"))

    def test_single_non_alnum(self):
        self.assertTrue(self.sol.isPalindrome("!"))

    def test_empty_after_strip(self):
        self.assertTrue(self.sol.isPalindrome("!!!!"))

    def test_two_same_characters(self):
        self.assertTrue(self.sol.isPalindrome("aa"))

    def test_two_different_characters(self):
        self.assertFalse(self.sol.isPalindrome("ab"))

    def test_case_insensitive_palindrome(self):
        self.assertTrue(self.sol.isPalindrome("Aa"))

    def test_case_insensitive_not_palindrome(self):
        self.assertFalse(self.sol.isPalindrome("Ab"))

    def test_numbers_only_palindrome(self):
        self.assertTrue(self.sol.isPalindrome("12321"))

    def test_numbers_only_not_palindrome(self):
        self.assertFalse(self.sol.isPalindrome("12345"))

    def test_mixed_letters_numbers_palindrome(self):
        self.assertTrue(self.sol.isPalindrome("a1a"))

    def test_mixed_letters_numbers_not_palindrome(self):
        self.assertFalse(self.sol.isPalindrome("a1b"))

    def test_punctuation_ignored(self):
        self.assertTrue(self.sol.isPalindrome(".,"))

    def test_leading_trailing_punctuation(self):
        self.assertTrue(self.sol.isPalindrome("!ab a!"))

    def test_inner_spaces_ignored(self):
        self.assertTrue(self.sol.isPalindrome("a b c d c b a"))

    def test_symbols_interleaved(self):
        self.assertTrue(self.sol.isPalindrome("A@B#B$A"))

    def test_all_lowercase_palindrome(self):
        self.assertTrue(self.sol.isPalindrome("level"))

    def test_all_lowercase_not_palindrome(self):
        self.assertFalse(self.sol.isPalindrome("levelz"))

    def test_uppercase_palindrome(self):
        self.assertTrue(self.sol.isPalindrome("LEVEL"))

    def test_tab_and_special_whitespace(self):
        self.assertTrue(self.sol.isPalindrome("a\tb a"))

    def test_long_palindrome(self):
        s = "a" * 100000 + "b" + "a" * 100000
        self.assertTrue(self.sol.isPalindrome(s))

    def test_long_not_palindrome(self):
        s = "a" * 100001 + "b"
        self.assertFalse(self.sol.isPalindrome(s))

    def test_non_alnum_in_middle(self):
        self.assertTrue(self.sol.isPalindrome("a!a"))

    def test_digits_and_punctuation(self):
        self.assertTrue(self.sol.isPalindrome("1, 2, 2, 1"))

    def test_not_palindrome_with_digits(self):
        self.assertFalse(self.sol.isPalindrome("1, 2, 3, 1"))

    def test_question_bang(self):
        self.assertTrue(self.sol.isPalindrome("N!N"))

    def test_odd_even_mirroring(self):
        self.assertFalse(self.sol.isPalindrome("0P"))
        self.assertTrue(self.sol.isPalindrome("0P0"))


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String
