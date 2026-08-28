# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Easy

import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        raise Exception("Not solved yet")


class TestStrStr(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(Solution().strStr("sadbutsad", "sad"), 0)

    def test_example2(self):
        self.assertEqual(Solution().strStr("leetcode", "leeto"), -1)

    def test_needle_at_start(self):
        self.assertEqual(Solution().strStr("hello world", "hello"), 0)

    def test_needle_at_end(self):
        self.assertEqual(Solution().strStr("hello world", "world"), 6)

    def test_needle_in_middle(self):
        self.assertEqual(Solution().strStr("hello world", "lo wo"), 3)

    def test_single_char_found(self):
        self.assertEqual(Solution().strStr("abcdef", "c"), 2)

    def test_single_char_not_found(self):
        self.assertEqual(Solution().strStr("abcdef", "z"), -1)

    def test_needle_equals_haystack(self):
        self.assertEqual(Solution().strStr("abc", "abc"), 0)

    def test_needle_longer_than_haystack(self):
        self.assertEqual(Solution().strStr("abc", "abcd"), -1)

    def test_repeated_characters(self):
        self.assertEqual(Solution().strStr("aaaaa", "aaa"), 0)

    def test_repeated_with_offset(self):
        self.assertEqual(Solution().strStr("aaaaab", "aab"), 3)

    def test_repeated_not_found(self):
        self.assertEqual(Solution().strStr("aaaa", "aabb"), -1)

    def test_first_occurrence_returned(self):
        self.assertEqual(Solution().strStr("aaabababab", "abab"), 2)

    def test_needle_one_char_same_as_haystack(self):
        self.assertEqual(Solution().strStr("a", "a"), 0)

    def test_single_chars_not_found(self):
        self.assertEqual(Solution().strStr("a", "b"), -1)

    def test_long_haystack(self):
        haystack = "a" * 10000
        self.assertEqual(Solution().strStr(haystack, "b"), -1)
        self.assertEqual(Solution().strStr(haystack, "a" * 10000), 0)

    def test_long_needle_middle(self):
        haystack = "a" * 5000 + "b" + "a" * 5000
        self.assertEqual(Solution().strStr(haystack, "b"), 5000)


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm, Boyer–Moore String-Search Algorithm
