# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Medium

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findAnagrams("cbaebabacd", "abc"), [0, 6])

    def test_example_2(self):
        self.assertEqual(self.solution.findAnagrams("abab", "ab"), [0, 1, 2])

    def test_no_match(self):
        self.assertEqual(self.solution.findAnagrams("aaaaa", "abc"), [])

    def test_p_longer_than_s(self):
        self.assertEqual(self.solution.findAnagrams("ab", "abc"), [])

    def test_p_equal_to_s(self):
        self.assertEqual(self.solution.findAnagrams("abc", "cba"), [0])

    def test_p_equal_to_s_no_match(self):
        self.assertEqual(self.solution.findAnagrams("abc", "ab"), [0])

    def test_single_char_match(self):
        self.assertEqual(self.solution.findAnagrams("aaa", "a"), [0, 1, 2])

    def test_single_char_no_match(self):
        self.assertEqual(self.solution.findAnagrams("bbb", "a"), [])

    def test_all_same_chars(self):
        self.assertEqual(self.solution.findAnagrams("aaaa", "aa"), [0, 1, 2])

    def test_repeated_pattern(self):
        self.assertEqual(self.solution.findAnagrams("abababa", "abab"), [0, 1, 2, 3])

    def test_duplicate_chars_in_p(self):
        self.assertEqual(self.solution.findAnagrams("aa", "aa"), [0])

    def test_mixed_matches(self):
        self.assertEqual(self.solution.findAnagrams("abcabc", "cab"), [0, 1, 2, 3])

    def test_only_end_matches(self):
        self.assertEqual(self.solution.findAnagrams("xxcab", "abc"), [2])

    def test_only_start_matches(self):
        self.assertEqual(self.solution.findAnagrams("abcxx", "bca"), [0])

    def test_single_char_s_and_p_match(self):
        self.assertEqual(self.solution.findAnagrams("a", "a"), [0])

    def test_single_char_s_and_p_no_match(self):
        self.assertEqual(self.solution.findAnagrams("a", "b"), [])

    def test_p_with_three_same_chars(self):
        self.assertEqual(self.solution.findAnagrams("aaab", "aaa"), [0])

    def test_p_chars_absent_from_s(self):
        self.assertEqual(self.solution.findAnagrams("xyz", "abc"), [])

    def test_multiple_distinct_anagrams(self):
        self.assertEqual(self.solution.findAnagrams("aaaabbb", "ab"), [3])

    def test_large_input_performance(self):
        s = "a" * 30000
        p = "a" * 100
        self.assertEqual(self.solution.findAnagrams(s, p), list(range(29901)))

    def test_large_input_no_match(self):
        import time

        s = "ab" * 15000
        p = "a" * 200
        start = time.time()
        self.assertEqual(self.solution.findAnagrams(s, p), [])
        self.assertLess(time.time() - start, 5)

    def test_result_order_increasing(self):
        result = self.solution.findAnagrams("cbaebabacd", "abc")
        self.assertEqual(result, sorted(result))


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Sliding Window
