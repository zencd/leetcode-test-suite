# 472. Concatenated Words
# https://leetcode.com/problems/concatenated-words/
# Hard

from typing import List
from functools import lru_cache


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def check(self, words, expected):
        self.assertEqual(
            sorted(self.sol.findAllConcatenatedWordsInADict(words)),
            sorted(expected),
        )

    def test_example_1(self):
        words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
        self.check(words, ["catsdogcats", "dogcatsdog", "ratcatdogcat"])

    def test_example_2(self):
        self.check(["cat", "dog", "catdog"], ["catdog"])

    def test_single_word(self):
        self.check(["hello"], [])

    def test_single_letter_word_not_concatenated(self):
        self.check(["a"], [])

    def test_two_letters_split_by_single_letter(self):
        self.check(["a", "aa"], ["aa"])

    def test_two_letters_split_by_single_letter_among_others(self):
        self.check(["b", "a", "aa"], ["aa"])

    def test_no_concatenated_words(self):
        self.check(["abc", "def"], [])

    def test_word_reused_multiple_times(self):
        self.check(["a", "b", "ab", "abab"], ["ab", "abab"])

    def test_triple_reuse(self):
        self.check(["a", "aaa"], ["aaa"])

    def test_word_is_itself_in_dict(self):
        self.check(["cat", "catcat"], ["catcat"])

    def test_partial_match_not_enough(self):
        self.check(["a", "b", "ab", "abc"], ["ab"])

    def test_longer_chain(self):
        self.check(["a", "ab", "abc", "abcd"], [])

    def test_multi_component_chain(self):
        self.check(["a", "aa", "aaa", "aaaa"], ["aa", "aaa", "aaaa"])

    def test_order_of_input_preserved(self):
        words = ["xy", "x", "y", "xyxy"]
        self.assertEqual(
            self.sol.findAllConcatenatedWordsInADict(words),
            ["xy", "xyxy"],
        )

    def test_all_words_concatenated(self):
        self.check(["a", "aa", "aaa", "aaaa"], ["aa", "aaa", "aaaa"])

    def test_none_when_only_long_words(self):
        self.check(["abcde", "fghij", "abcdefghij"], ["abcdefghij"])

    def test_dict_order_independent_duplicates_avoided(self):
        self.assertEqual(len(self.sol.findAllConcatenatedWordsInADict(["x", "y", "xy", "yx"])), 2)

    def test_large_perf(self):
        words = ["a" * i for i in range(1, 21)]
        words += ["ab", "a", "b"]
        result = self.sol.findAllConcatenatedWordsInADict(words)
        expected = ["a" * i for i in range(2, 21)] + ["ab"]
        self.assertEqual(sorted(result), sorted(expected))

    def test_mixed_valid_invalid(self):
        words = ["cat", "car", "dog", "pea", "peacat", "catdog", "dogcat", "carcat"]
        self.check(words, ["peacat", "catdog", "dogcat", "carcat"])

    def test_single_char_reuse_needed(self):
        self.check(["a", "b", "abba"], ["abba"])

    def test_empty_like_input_single_long_word(self):
        self.check(["abcdefghij"], [])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Dynamic Programming, Depth-First Search, Trie, Sorting
