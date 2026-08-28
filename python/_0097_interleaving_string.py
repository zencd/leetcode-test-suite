# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/
# Medium

import unittest


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        raise Exception("Not solved yet")


class TestIsInterleave(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_basic_true(self):
        self.assertTrue(self.s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_basic_false(self):
        self.assertFalse(self.s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

    def test_all_empty(self):
        self.assertTrue(self.s.isInterleave("", "", ""))

    def test_one_empty(self):
        self.assertTrue(self.s.isInterleave("", "abc", "abc"))
        self.assertTrue(self.s.isInterleave("abc", "", "abc"))

    def test_one_empty_false(self):
        self.assertFalse(self.s.isInterleave("", "abc", "abd"))
        self.assertFalse(self.s.isInterleave("abc", "", "abd"))
        self.assertFalse(self.s.isInterleave("", "abc", "ab"))
        self.assertFalse(self.s.isInterleave("abc", "", "ab"))

    def test_single_chars(self):
        self.assertTrue(self.s.isInterleave("a", "b", "ab"))
        self.assertTrue(self.s.isInterleave("a", "b", "ba"))
        self.assertFalse(self.s.isInterleave("a", "b", "aa"))
        self.assertFalse(self.s.isInterleave("a", "b", "bb"))
        self.assertFalse(self.s.isInterleave("a", "b", "a"))
        self.assertFalse(self.s.isInterleave("a", "b", "abc"))

    def test_identical_chars(self):
        self.assertTrue(self.s.isInterleave("aa", "bb", "abab"))
        self.assertTrue(self.s.isInterleave("aa", "bb", "baab"))
        self.assertTrue(self.s.isInterleave("aa", "bb", "bbaa"))
        self.assertTrue(self.s.isInterleave("aa", "bb", "aabb"))
        self.assertTrue(self.s.isInterleave("aa", "bb", "abba"))
        self.assertTrue(self.s.isInterleave("aa", "bb", "baba"))
        self.assertFalse(self.s.isInterleave("aa", "bb", "aaab"))
        self.assertFalse(self.s.isInterleave("aa", "bb", "aabbcc"))
        self.assertFalse(self.s.isInterleave("a", "a", "a"))
        self.assertFalse(self.s.isInterleave("a", "a", "aaa"))
        self.assertTrue(self.s.isInterleave("a", "a", "aa"))

    def test_length_mismatch(self):
        self.assertFalse(self.s.isInterleave("ab", "cd", "abcdx"))
        self.assertFalse(self.s.isInterleave("ab", "cd", "abc"))
        self.assertFalse(self.s.isInterleave("abc", "def", "abcdefg"))
        self.assertFalse(self.s.isInterleave("abc", "def", "abcde"))

    def test_repeated_same_string(self):
        self.assertTrue(self.s.isInterleave("abc", "abc", "abcabc"))
        self.assertTrue(self.s.isInterleave("abc", "abc", "aabbcc"))
        self.assertTrue(self.s.isInterleave("abc", "abc", "ababcc"))
        self.assertTrue(self.s.isInterleave("abc", "abc", "aabcbc"))
        self.assertFalse(self.s.isInterleave("abc", "abc", "abccab"))
        self.assertFalse(self.s.isInterleave("ab", "ab", "ababx"))

    def test_interleave_patterns(self):
        self.assertTrue(self.s.isInterleave("a", "b", "ab"))
        self.assertFalse(self.s.isInterleave("aa", "ab", "aabb"))
        self.assertEqual(
            self.s.isInterleave("ab", "aa", "aabb"),
            self.s.isInterleave("aa", "ab", "aabb"),
        )
        self.assertTrue(self.s.isInterleave("ab", "aa", "aaba"))
        self.assertTrue(self.s.isInterleave("aa", "ab", "abaa"))
        self.assertTrue(self.s.isInterleave("ab", "aa", "aaab"))
        self.assertTrue(self.s.isInterleave("ab", "aa", "abaa"))
        self.assertFalse(self.s.isInterleave("ab", "aa", "baaa"[:3]))

    def test_s1_longer(self):
        self.assertTrue(self.s.isInterleave("abcd", "e", "abcde"))
        self.assertTrue(self.s.isInterleave("abcd", "e", "eabcd"))
        self.assertTrue(self.s.isInterleave("abcd", "e", "abecd"))
        self.assertTrue(self.s.isInterleave("abcd", "e", "abced"))
        self.assertTrue(self.s.isInterleave("abcd", "e", "abcde"))
        self.assertFalse(self.s.isInterleave("abcd", "e", "abcdf"))

    def test_s2_longer(self):
        self.assertTrue(self.s.isInterleave("e", "abcd", "abcde"))
        self.assertTrue(self.s.isInterleave("e", "abcd", "eabcd"))
        self.assertTrue(self.s.isInterleave("e", "abcd", "abecd"))
        self.assertTrue(self.s.isInterleave("e", "abcd", "abced"))
        self.assertFalse(self.s.isInterleave("e", "abcd", "abcdf"))

    def test_complex_true(self):
        self.assertTrue(self.s.isInterleave("zzz", "zzz", "zzzzzz"))
        self.assertTrue(self.s.isInterleave("xyx", "yxx", "xyxyxx"[:6]))
        self.assertTrue(self.s.isInterleave("a", "b", "ba"))
        self.assertTrue(self.s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_complex_false(self):
        self.assertFalse(self.s.isInterleave("zzz", "zzz", "zzzzz"))
        self.assertFalse(self.s.isInterleave("ab", "ab", "abba"))
        self.assertFalse(self.s.isInterleave("aab", "aab", "aababb"[:5]))
        self.assertFalse(self.s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

    def test_single_long(self):
        s1 = "a" * 50
        s2 = "b" * 50
        s3 = "ab" * 50
        self.assertTrue(self.s.isInterleave(s1, s2, s3))
        self.assertTrue(self.s.isInterleave(s1, s2, s2 + s1))
        self.assertTrue(self.s.isInterleave(s1, s2, s1 + s2))
        self.assertFalse(self.s.isInterleave(s1, s2, ("ab" * 48) + "a"))
        self.assertFalse(self.s.isInterleave(s1, s2, ("ab" * 49) + "b"))

    def test_no_common_interleave(self):
        self.assertTrue(self.s.isInterleave("ab", "cd", "abcd"))
        self.assertTrue(self.s.isInterleave("ab", "cd", "cdab"))
        self.assertTrue(self.s.isInterleave("ab", "cd", "acbd"))
        self.assertTrue(self.s.isInterleave("ab", "cd", "acdb"))
        self.assertFalse(self.s.isInterleave("ab", "cd", "adcb"))
        self.assertTrue(self.s.isInterleave("ab", "cd", "cabd"))
        self.assertTrue(self.s.isInterleave("ab", "cd", "cadb"))
        self.assertFalse(self.s.isInterleave("ab", "cd", "accd"))
        self.assertFalse(self.s.isInterleave("ab", "cd", "ccab"))

    def test_empty_s3(self):
        self.assertTrue(self.s.isInterleave("", "", ""))


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming
