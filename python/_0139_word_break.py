# 139. Word Break
# https://leetcode.com/problems/word-break/
# Medium

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1_leetcode(self):
        self.assertTrue(self.sol.wordBreak("leetcode", ["leet", "code"]))

    def test_example2_applepenapple(self):
        self.assertTrue(self.sol.wordBreak("applepenapple", ["apple", "pen"]))

    def test_example3_catsandog(self):
        self.assertFalse(
            self.sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        )

    def test_single_char_match(self):
        self.assertTrue(self.sol.wordBreak("a", ["a"]))

    def test_single_char_no_match(self):
        self.assertFalse(self.sol.wordBreak("a", ["b"]))

    def test_single_word_exact(self):
        self.assertTrue(self.sol.wordBreak("hello", ["hello"]))

    def test_single_word_not_exact(self):
        self.assertFalse(self.sol.wordBreak("hell", ["hello"]))

    def test_word_longer_than_s(self):
        self.assertFalse(self.sol.wordBreak("ab", ["abcd"]))

    def test_reuse_same_word(self):
        self.assertTrue(self.sol.wordBreak("aaaa", ["aaa", "aaaa"]))

    def test_reuse_word_multiple_times(self):
        self.assertTrue(self.sol.wordBreak("aaaaaa", ["aa"]))

    def test_empty_dict(self):
        self.assertFalse(self.sol.wordBreak("abc", []))

    def test_dict_with_only_empty_word(self):
        self.assertFalse(self.sol.wordBreak("abc", [""]))

    def test_all_single_chars(self):
        self.assertTrue(self.sol.wordBreak("abcdef", ["a", "b", "c", "d", "e", "f"]))

    def test_negative_all_single_chars(self):
        self.assertFalse(self.sol.wordBreak("abcdef", ["a", "b", "c", "d", "e"]))

    def test_one_char_segments(self):
        self.assertTrue(self.sol.wordBreak("b", ["b"]))

    def test_mixed_segmentation(self):
        self.assertTrue(self.sol.wordBreak("runtime", ["run", "time"]))

    def test_substring_trap(self):
        self.assertFalse(self.sol.wordBreak("abcdef", ["ab", "cd", "efg"]))

    def test_word_appearing_but_wrong_order(self):
        self.assertFalse(self.sol.wordBreak("abc", ["bc", "ab"]))

    def test_long_s_all_repeated(self):
        s = "a" * 294
        self.assertTrue(self.sol.wordBreak(s, ["a" * 7]))

    def test_long_s_no_break(self):
        s = "a" * 300
        self.assertFalse(self.sol.wordBreak(s, ["a" * 7] * 0 + ["b"]))

    def test_long_s_repeatable_pattern(self):
        s = "ab" * 150
        self.assertTrue(self.sol.wordBreak(s, ["ab"]))

    def test_long_s_mixed_lengths(self):
        s = "abc" * 100
        self.assertTrue(self.sol.wordBreak(s, ["a", "bc", "abc", "abcabc"]))

    def test_dict_dominates_s(self):
        self.assertTrue(self.sol.wordBreak("aaaa", ["a", "aa"]))

    def test_word_in_dict_not_prefix(self):
        self.assertTrue(self.sol.wordBreak("helloworld", ["hello", "world"]))

    def test_requires_intermediate_words(self):
        self.assertTrue(self.sol.wordBreak("aaaa", ["aa", "a"]))

    def test_only_partial_covers(self):
        self.assertFalse(self.sol.wordBreak("abcd", ["ab"]))

    def test_single_word_in_dict_covers_all(self):
        self.assertTrue(self.sol.wordBreak("z", ["z"]))

    def test_many_words_in_dict(self):
        words = [chr(ord("a") + i) * (i + 1) for i in range(26)]
        self.assertTrue(self.sol.wordBreak("abbccc", words))

    def test_false_with_many_words_in_dict(self):
        words = [chr(ord("a") + i) * (i + 1) for i in range(25)]
        self.assertFalse(self.sol.wordBreak("zzz", words))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, String, Dynamic Programming, Trie, Memoization, Brute-Force Search
