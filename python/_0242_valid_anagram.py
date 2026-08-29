# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Easy

import unittest
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1_true(self):
        self.assertTrue(self.sol.isAnagram("anagram", "nagaram"))

    def test_example2_false(self):
        self.assertFalse(self.sol.isAnagram("rat", "car"))

    def test_single_char_same(self):
        self.assertTrue(self.sol.isAnagram("a", "a"))

    def test_single_char_diff(self):
        self.assertFalse(self.sol.isAnagram("a", "b"))

    def test_two_chars_anagram(self):
        self.assertTrue(self.sol.isAnagram("ab", "ba"))

    def test_two_chars_not_anagram(self):
        self.assertFalse(self.sol.isAnagram("ab", "aa"))

    def test_same_string(self):
        self.assertTrue(self.sol.isAnagram("zzz", "zzz"))

    def test_different_lengths(self):
        self.assertFalse(self.sol.isAnagram("abc", "abcd"))

    def test_all_same_letters(self):
        self.assertTrue(self.sol.isAnagram("aaaa", "aaaa"))

    def test_repeated_letters_anagram(self):
        self.assertTrue(self.sol.isAnagram("abab", "baba"))

    def test_repeated_letters_not_anagram(self):
        self.assertFalse(self.sol.isAnagram("aab", "abb"))

    def test_substring_anagram_false(self):
        self.assertFalse(self.sol.isAnagram("anagram", "nagram"))

    def test_one_char_subset_other(self):
        self.assertFalse(self.sol.isAnagram("ab", "abab"))

    def test_no_common_chars(self):
        self.assertFalse(self.sol.isAnagram("abc", "xyz"))

    def test_long_anagram(self):
        s = "a" * 50000
        t = "a" * 50000
        self.assertTrue(self.sol.isAnagram(s, t))

    def test_long_not_anagram(self):
        s = "a" * 49999 + "b"
        t = "a" * 50000
        self.assertFalse(self.sol.isAnagram(s, t))

    def test_custom(self):
        self.assertFalse(self.sol.isAnagram("aa", "bb"))


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Sorting
