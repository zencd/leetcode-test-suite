# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Medium

import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        raise Exception("Not solved yet")


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def check_example(self, s: str, expected: str) -> None:
        result = self.solution.longestPalindrome(s)
        self.assertEqual(
            len(result),
            len(expected),
            f"input={s!r}, got={result!r}, expected length={len(expected)}",
        )
        self.assertTrue(
            self.is_palindrome(result), f"input={s!r}, got non-palindrome {result!r}"
        )
        self.assertIn(result, s, f"input={s!r}, substring {result!r} not found")
        if result != expected:
            self.assertEqual(len(result), len(expected))

    def test_example1_babad(self):
        self.check_example("babad", "bab")

    def test_example2_cbbd(self):
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")

    def test_single_character(self):
        self.assertEqual(self.solution.longestPalindrome("a"), "a")

    def test_all_same_characters(self):
        self.assertEqual(self.solution.longestPalindrome("aaaa"), "aaaa")

    def test_all_different_characters(self):
        self.assertEqual(self.solution.longestPalindrome("abcde"), "a")

    def test_full_palindrome_odd(self):
        self.assertEqual(self.solution.longestPalindrome("abcba"), "abcba")

    def test_full_palindrome_even(self):
        self.assertEqual(self.solution.longestPalindrome("abba"), "abba")

    def test_palindrome_at_start(self):
        self.assertEqual(self.solution.longestPalindrome("abaxyz"), "aba")

    def test_palindrome_at_end(self):
        self.assertEqual(self.solution.longestPalindrome("xyzzu"), "zz")

    def test_two_character_palindrome(self):
        self.assertEqual(self.solution.longestPalindrome("ab"), "a")

    def test_even_length_no_palindrome(self):
        result = self.solution.longestPalindrome("abcd")
        self.assertEqual(len(result), 1)
        self.assertIn(result, "abcd")

    def test_digits_only(self):
        self.assertEqual(self.solution.longestPalindrome("123454321"), "123454321")

    def test_mixed_digits_and_letters(self):
        result = self.solution.longestPalindrome("a1b2c2b1a")
        self.assertEqual(result, "a1b2c2b1a")

    def test_uppercase_letters(self):
        result = self.solution.longestPalindrome("AbB")
        self.assertEqual(len(result), 1)
        self.assertIn(result, "AbB")

    def test_case_sensitive(self):
        result = self.solution.longestPalindrome("aBc")
        self.assertEqual(len(result), 1)
        self.assertIn(result, "aBc")

    def test_nested_palindromes(self):
        self.assertEqual(self.solution.longestPalindrome("abacdfgdcaba"), "aba")

    def test_longest_in_middle(self):
        self.assertEqual(self.solution.longestPalindrome("xabcba"), "abcba")

    def test_repeating_pattern(self):
        result = self.solution.longestPalindrome("abababab")
        self.assertEqual(len(result), 7)
        self.assertTrue(self.is_palindrome(result))
        self.assertIn(result, "abababab")

    def test_boundary_palindromes(self):
        result = self.solution.longestPalindrome("baab")
        self.assertEqual(len(result), 4)
        self.assertTrue(self.is_palindrome(result))
        self.assertIn(result, "baab")

    def test_length_1000(self):
        s = "a" * 999 + "b"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(len(result), 999)
        self.assertEqual(result, "a" * 999)

    def test_alternating_two_chars(self):
        s = "ab" * 25
        result = self.solution.longestPalindrome(s)
        self.assertTrue(self.is_palindrome(result))
        self.assertIn(result, s)
        self.assertGreaterEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String, Dynamic Programming, Manacher
