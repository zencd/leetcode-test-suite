# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/
# Hard

from typing import List


class _TrieNode:
    __slots__ = ("children", "word")

    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def assertWords(self, board, words, expected):
        b = [list(row) for row in board]
        ws = list(words)
        self.assertEqual(sorted(Solution().findWords(b, ws)), sorted(expected))

    def test_example_1(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        self.assertWords(board, ["oath", "pea", "eat", "rain"], ["eat", "oath"])

    def test_example_2(self):
        board = [["a", "b"], ["c", "d"]]
        self.assertWords(board, ["abcb"], [])

    def test_single_cell_board_match(self):
        self.assertWords([["a"]], ["a"], ["a"])

    def test_single_cell_board_no_match(self):
        self.assertWords([["a"]], ["b"], [])

    def test_single_cell_word_too_long(self):
        self.assertWords([["a"]], ["aa"], [])

    def test_single_letter_words(self):
        board = [["a", "b"], ["c", "d"]]
        self.assertWords(board, ["a", "c", "z"], ["a", "c"])

    def test_word_found_once_despite_multiple_positions(self):
        board = [["a", "a"], ["a", "a"]]
        self.assertWords(board, ["a"], ["a"])

    def test_word_found_once_despite_multiple_paths(self):
        board = [
            ["a", "b"],
            ["b", "a"],
        ]
        self.assertWords(board, ["ab"], ["ab"])

    def test_full_board_serpentine_word(self):
        board = [
            ["a", "b"],
            ["c", "d"],
        ]
        self.assertWords(board, ["abcd", "abdc", "dcba"], ["abdc"])

    def test_word_longer_than_board_area(self):
        board = [["a", "b"], ["c", "d"]]
        self.assertWords(board, ["abcdx", "abcdef"], [])

    def test_repeated_letters_needing_distinct_cells(self):
        board = [["a", "a"], ["a", "a"]]
        self.assertWords(board, ["aaaa"], ["aaaa"])

    def test_repeated_letters_impossible(self):
        board = [["a", "b"], ["c", "d"]]
        self.assertWords(board, ["aa"], [])

    def test_no_cell_reuse_within_word(self):
        board = [["a", "b"], ["c", "d"]]
        self.assertWords(board, ["abcb", "ababc"], [])

    def test_prefix_family_of_words(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        self.assertWords(board, ["e", "ea", "eat", "eats"], ["e", "ea", "eat"])

    def test_mixed_found_and_not_found(self):
        board = [["a", "b"], ["c", "d"]]
        self.assertWords(
            board,
            ["ab", "cd", "dc", "zz", "abcd", "dcba", "abdc"],
            ["ab", "cd", "dc", "abdc"],
        )

    def test_1x2_board_horizontal_word(self):
        board = [["a", "b"]]
        self.assertWords(board, ["ab", "ba", "a", "b", "abb"], ["ab", "ba", "a", "b"])

    def test_2x1_board_vertical_word(self):
        board = [["a"], ["b"]]
        self.assertWords(board, ["ab", "ba", "aabb"], ["ab", "ba"])

    def test_3x3_cross_shaped_word(self):
        board = [
            ["a", "a", "a"],
            ["a", "b", "a"],
            ["a", "a", "a"],
        ]
        self.assertWords(board, ["ab", "ba", "abba"], ["ab", "ba"])

    def test_word_needing_backtracking(self):
        board = [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
        ]
        self.assertWords(board, ["abc", "def", "cfe", "afeb", "abcx"], ["abc", "def", "cfe"])

    def test_long_word_serpentine_path(self):
        board = [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
        ]
        self.assertWords(board, ["abc", "jkl", "abcdefghijkl"], ["abc", "jkl"])

    def test_no_valid_words_at_all(self):
        board = [["a", "b"], ["c", "d"]]
        self.assertWords(board, ["zz", "xy", "abcxz"], [])

    def test_many_words_single_word_board_repeats_in_list_of_words(self):
        board = [["a"]]
        self.assertWords(board, ["a", "ab", "b", "baa"], ["a"])

    def test_word_uses_non_adjacent_letters(self):
        board = [["a", "x", "b"]]
        self.assertWords(board, ["ab", "axb"], ["axb"])

    def test_result_not_mutated_between_calls(self):
        sol = Solution()
        board = [["a", "b"], ["c", "d"]]
        first = sol.findWords([list(r) for r in board], ["ab"])
        second = sol.findWords([list(r) for r in board], ["cd"])
        self.assertEqual(first, ["ab"])
        self.assertEqual(second, ["cd"])

    def test_board_not_mutated(self):
        board = [["a", "b"], ["c", "d"]]
        original = [list(r) for r in board]
        Solution().findWords(board, ["ab", "cd"])
        self.assertEqual(board, original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Backtracking, Trie, Matrix
