# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/
# Easy

class Solution:
    def longestPalindrome(self, s: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.longestPalindrome("abccccdd"), 7)

    def test_example2(self):
        self.assertEqual(self.sol.longestPalindrome("a"), 1)

    def test_all_same(self):
        self.assertEqual(self.sol.longestPalindrome("aaaa"), 4)

    def test_all_distinct(self):
        self.assertEqual(self.sol.longestPalindrome("abcd"), 1)

    def test_all_palindromic(self):
        self.assertEqual(self.sol.longestPalindrome("abba"), 4)

    def test_case_sensitive(self):
        self.assertEqual(self.sol.longestPalindrome("Aa"), 1)

    def test_case_sensitive_mixed(self):
        self.assertEqual(self.sol.longestPalindrome("AaBbCc"), 1)

    def test_single_odd(self):
        self.assertEqual(self.sol.longestPalindrome("aab"), 3)

    def test_two_odds(self):
        self.assertEqual(self.sol.longestPalindrome("aabb"), 4)

    def test_multiple_odds(self):
        self.assertEqual(self.sol.longestPalindrome("abc"), 1)

    def test_two_chars_odd(self):
        self.assertEqual(self.sol.longestPalindrome("aabbc"), 5)

    def test_all_even_counts(self):
        self.assertEqual(self.sol.longestPalindrome("abcabc"), 6)

    def test_larger_palindromic_string(self):
        self.assertEqual(self.sol.longestPalindrome("aba"), 3)

    def test_large_even_counts(self):
        self.assertEqual(self.sol.longestPalindrome("a" * 2000), 2000)

    def test_large_mixed(self):
        s = "a" * 1999 + "b"
        self.assertEqual(self.sol.longestPalindrome(s), 1999)

    def test_all_odds_large(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.sol.longestPalindrome(s), 1)

    def test_upper_lower_pairs(self):
        self.assertEqual(self.sol.longestPalindrome("aAaA"), 4)

    def test_pairs_plus_one_odd(self):
        self.assertEqual(self.sol.longestPalindrome("aabbccdde"), 9)

    def test_triples_each(self):
        self.assertEqual(self.sol.longestPalindrome("xyzxyzxyz"), 7)

    def test_triples(self):
        self.assertEqual(self.sol.longestPalindrome("aaabbb"), 5)

    def test_four_odds(self):
        self.assertEqual(self.sol.longestPalindrome("aabbccdd"), 8)

    def test_one_char_pairs_only(self):
        self.assertEqual(self.sol.longestPalindrome("aa"), 2)

    def test_odd_dominant(self):
        self.assertEqual(self.sol.longestPalindrome("aaabc"), 3)

    def test_alternating_pairs(self):
        self.assertEqual(self.sol.longestPalindrome("abab"), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Greedy
