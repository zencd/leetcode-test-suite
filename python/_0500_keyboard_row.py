# 500. Keyboard Row
# https://leetcode.com/problems/keyboard-row/
# Easy

from typing import List
import unittest

ROWS = [
    set("qwertyuiop"),
    set("asdfghjkl"),
    set("zxcvbnm"),
]
CHAR_ROW = {c: i for i, row in enumerate(ROWS) for c in row}


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])

    def test_example2(self):
        self.assertEqual(self.solution.findWords(["omk"]), [])

    def test_example3(self):
        self.assertEqual(self.solution.findWords(["adsdf", "sfd"]), ["adsdf", "sfd"])

    def test_empty_is_invalid_single_char(self):
        self.assertEqual(self.solution.findWords(["a"]), ["a"])

    def test_single_char_all_rows(self):
        self.assertEqual(self.solution.findWords(["a", "q", "z"]), ["a", "q", "z"])
        self.assertEqual(self.solution.findWords(["A", "Q", "Z"]), ["A", "Q", "Z"])

    def test_uppercase_row_words(self):
        self.assertEqual(self.solution.findWords(["ASDFGJKL", "QWERTYUIOP", "ZXCVBNM"]), ["ASDFGJKL", "QWERTYUIOP", "ZXCVBNM"])

    def test_mixed_case_valid(self):
        self.assertEqual(self.solution.findWords(["aDsFsDf", "QwErTy"]), ["aDsFsDf", "QwErTy"])

    def test_mixed_case_invalid(self):
        self.assertEqual(self.solution.findWords(["aDfSgHjKx", "abq"]), [])

    def test_cross_row_words_rejected(self):
        self.assertEqual(self.solution.findWords(["aQ", "Zs", "qz"]), [])

    def test_preserves_input_order_and_case(self):
        result = self.solution.findWords(["Zebra", "alaska", "dad", "PeAcea"])
        self.assertEqual(result, ["alaska", "dad"])

    def test_word_with_all_rows_present(self):
        self.assertEqual(self.solution.findWords(["qaz"]), [])
        self.assertEqual(self.solution.findWords(["QAZ"]), [])

    def test_long_single_row_word(self):
        self.assertIn("s" * 100, self.solution.findWords(["s" * 100]))

    def test_long_cross_row_word(self):
        self.assertEqual(self.solution.findWords(["a" * 99 + "b"]), [])

    def test_max_words(self):
        words = ["a" * 10 for _ in range(20)]
        self.assertEqual(self.solution.findWords(words), words)

    def test_all_letters_each_row(self):
        self.assertEqual(self.solution.findWords(["qwertyuiop"]), ["qwertyuiop"])
        self.assertEqual(self.solution.findWords(["asdfghjkl"]), ["asdfghjkl"])
        self.assertEqual(self.solution.findWords(["zxcvbnm"]), ["zxcvbnm"])
        self.assertEqual(
            self.solution.findWords(
                ["qwer"],
            ),
            ["qwer"],
        )

    def test_two_letters_different_rows(self):
        self.assertEqual(self.solution.findWords(["aq"]), [])
        self.assertEqual(self.solution.findWords(["qw"]), ["qw"])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, String
