# 126. Word Ladder II
# https://leetcode.com/problems/word-ladder-ii/
# Hard

from collections import defaultdict
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        raise Exception("Not solved yet")


import unittest


def normalize(paths):
    return [list(p) for p in sorted(["".join(p) for p in paths])]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def check(self, begin, end, word_list, expected):
        actual = self.sol.findLadders(begin, end, word_list)
        self.assertEqual(normalize(actual), normalize(expected))
        for p in actual:
            self.assertEqual(p[0], begin)
            self.assertEqual(p[-1], end)
            self.assertEqual(len(set(p)), len(p))
            for a, b in zip(p, p[1:]):
                self.assertEqual(sum(x != y for x, y in zip(a, b)), 1)

    def test_example_one(self):
        self.check(
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
        )

    def test_example_two_end_word_missing(self):
        self.check("hit", "cog", ["hot", "dot", "dog", "lot", "log"], [])

    def test_no_path(self):
        self.check("hit", "cog", ["hot", "dot", "dog"], [])

    def test_single_step(self):
        self.check("ab", "cb", ["ab", "cb", "ac"], [["ab", "cb"]])

    def test_one_letter_direct(self):
        self.check("a", "c", ["b", "c"], [["a", "c"]])

    def test_begin_in_wordlist(self):
        self.check("hot", "dog", ["hot", "dot", "dog"], [["hot", "dot", "dog"]])

    def test_diamond_two_paths(self):
        self.check(
            "ab", "cd", ["cb", "ad", "cd"], [["ab", "cb", "cd"], ["ab", "ad", "cd"]]
        )

    def test_parallel_paths(self):
        self.check(
            "aa",
            "cc",
            ["ac", "ca", "bc", "cb", "cc"],
            [["aa", "ac", "cc"], ["aa", "ca", "cc"]],
        )

    def test_only_shortest_returned(self):
        self.check("ab", "cb", ["cb", "ac", "cd"], [["ab", "cb"]])

    def test_cycle_not_revisited(self):
        self.check(
            "aa", "bb", ["ab", "ba", "bb"], [["aa", "ab", "bb"], ["aa", "ba", "bb"]]
        )

    def test_end_word_not_reachable(self):
        self.check("hit", "cog", ["hot", "cog"], [])

    def test_begin_word_not_in_list_still_fails(self):
        self.check("hit", "cog", ["dot", "dog", "lot", "log", "cog"], [])

    def test_empty_wordlist(self):
        self.assertEqual(self.sol.findLadders("a", "b", []), [])

    def test_direct_step_among_many_words(self):
        words = [f + g for f in "ab" for g in "cde"]
        self.check("ac", "ad", words, [["ac", "ad"]])

    def test_single_middle_path(self):
        self.check("ac", "cb", ["ab", "cb"], [["ac", "ab", "cb"]])

    def test_no_duplicate_paths_in_output(self):
        words = ["hot", "dot", "dog", "lot", "log", "cog"]
        res = self.sol.findLadders("hit", "cog", words)
        self.assertEqual(len(res), len({tuple(r) for r in res}))

    def test_input_order_irrelevant(self):
        words = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(
            self.sol.findLadders("hit", "cog", words),
            self.sol.findLadders("hit", "cog", list(reversed(words))),
        )


def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Backtracking, Breadth-First Search, Bidirectional Search
