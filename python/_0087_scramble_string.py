# 87. Scramble String
# https://leetcode.com/problems/scramble-string/
# Hard

from collections import Counter
from functools import lru_cache
from unittest import TestCase, main


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        raise Exception("Not solved yet")


class TestIsScramble(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.isScramble("great", "rgeat"))
        self.assertFalse(self.sol.isScramble("abcde", "caebd"))
        self.assertTrue(self.sol.isScramble("a", "a"))

    def test_single_character(self):
        self.assertTrue(self.sol.isScramble("z", "z"))
        self.assertFalse(self.sol.isScramble("a", "b"))
        self.assertFalse(self.sol.isScramble("q", "w"))

    def test_two_characters(self):
        self.assertTrue(self.sol.isScramble("ab", "ba"))
        self.assertTrue(self.sol.isScramble("xy", "yx"))
        self.assertTrue(self.sol.isScramble("tt", "tt"))
        self.assertTrue(self.sol.isScramble("ab", "ab"))
        self.assertFalse(self.sol.isScramble("ab", "aa"))
        self.assertFalse(self.sol.isScramble("xy", "xz"))
        self.assertFalse(self.sol.isScramble("ab", "cd"))

    def test_three_characters(self):
        self.assertTrue(self.sol.isScramble("abc", "bac"))
        self.assertTrue(self.sol.isScramble("abc", "bca"))
        self.assertTrue(self.sol.isScramble("abc", "cba"))
        self.assertTrue(self.sol.isScramble("abc", "cab"))
        self.assertTrue(self.sol.isScramble("abc", "acb"))
        self.assertTrue(self.sol.isScramble("aba", "aab"))
        self.assertTrue(self.sol.isScramble("aba", "baa"))
        self.assertFalse(self.sol.isScramble("abc", "abd"))
        self.assertFalse(self.sol.isScramble("aaa", "aab"))
        self.assertFalse(self.sol.isScramble("aab", "abb"))

    def test_repeated_characters(self):
        self.assertTrue(self.sol.isScramble("abb", "bba"))
        self.assertTrue(self.sol.isScramble("aaab", "baaa"))
        self.assertTrue(self.sol.isScramble("aaab", "abaa"))
        self.assertTrue(self.sol.isScramble("aaab", "aaba"))
        self.assertTrue(self.sol.isScramble("aaaa", "aaaa"))
        self.assertTrue(self.sol.isScramble("aalg", "gaal"))
        self.assertTrue(self.sol.isScramble("aabb", "bbaa"))
        self.assertFalse(self.sol.isScramble("aabb", "abbb"))
        self.assertFalse(self.sol.isScramble("aaab", "bbba"))

    def test_four_and_longer(self):
        self.assertTrue(self.sol.isScramble("abab", "baba"))
        self.assertTrue(self.sol.isScramble("same", "same"))
        self.assertTrue(self.sol.isScramble("banana", "banana"))
        self.assertTrue(self.sol.isScramble("great", "great"))
        self.assertTrue(self.sol.isScramble("same", "ames"))

    def test_different_lengths(self):
        self.assertFalse(self.sol.isScramble("ab", "a"))
        self.assertFalse(self.sol.isScramble("a", "ab"))
        self.assertFalse(self.sol.isScramble("abc", "abcd"))

    def test_large(self):
        s = "abcdef"
        self.assertTrue(self.sol.isScramble(s, s))
        self.assertTrue(self.sol.isScramble(s, "fedcba"))
        self.assertFalse(self.sol.isScramble("abcd", "cadb"))
        self.assertFalse(self.sol.isScramble("abcd", "bdac"))


if __name__ == "__main__":
    main()

# Tags: String, Dynamic Programming
