# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/
# Hard

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
            5,
        )

    def test_example2_endword_not_in_list(self):
        self.assertEqual(
            self.sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
            0,
        )

    def test_shortest_path(self):
        self.assertEqual(
            self.sol.ladderLength("hit", "hot", ["hot"]),
            2,
        )

    def test_direct_one_step(self):
        self.assertEqual(
            self.sol.ladderLength("hot", "dot", ["dot"]),
            2,
        )

    def test_no_path(self):
        self.assertEqual(
            self.sol.ladderLength("hit", "cog", ["dog"]),
            0,
        )

    def test_begin_not_in_list(self):
        self.assertEqual(
            self.sol.ladderLength("red", "tax", ["ted", "tex", "tax"]),
            4,
        )

    def test_single_letter_words(self):
        self.assertEqual(
            self.sol.ladderLength("a", "c", ["b", "c"]),
            2,
        )

    def test_single_letter_unreachable(self):
        self.assertEqual(
            self.sol.ladderLength("a", "c", ["b"]),
            0,
        )

    def test_long_words(self):
        self.assertEqual(
            self.sol.ladderLength(
                "aaaaaaaaaa",
                "bbbbbbbbbb",
                ["b" * k + "a" * (10 - k) for k in range(1, 10)] + ["bbbbbbbbbb"],
            ),
            11,
        )

    def test_large_word_list(self):
        words = []
        base = ["a"] * 9 + ["b"]
        for c in "abcdefghijklmnopqrstuvwxyz":
            words.append("a" * 9 + c)
        self.assertEqual(
            self.sol.ladderLength("b" * 10, "c" * 10, words),
            0,
        )

    def test_middle_bridge(self):
        self.assertEqual(
            self.sol.ladderLength("cat", "dog", ["bat", "bet", "bot", "bag", "bog", "dog"]),
            5,
        )

    def test_endword_in_list_only(self):
        self.assertEqual(
            self.sol.ladderLength("hot", "dog", ["dog"]),
            0,
        )

    def test_begin_in_list_is_ignored(self):
        self.assertEqual(
            self.sol.ladderLength("hit", "cog", ["hit", "hot", "dot", "dog", "lot", "log", "cog"]),
            5,
        )

    def test_cycle_avoidance(self):
        self.assertEqual(
            self.sol.ladderLength("aa", "zz", ["bb", "zz"]),
            0,
        )

    def test_returns_int_type(self):
        result = self.sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Breadth-First Search, Bidirectional Search
