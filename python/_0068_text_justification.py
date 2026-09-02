# 68. Text Justification
# https://leetcode.com/problems/text-justification/
# Hard

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  ",
        ]
        self.assertEqual(self.sol.fullJustify(words, 16), expected)

    def test_example2(self):
        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        ",
        ]
        self.assertEqual(self.sol.fullJustify(words, 16), expected)

    def test_example3(self):
        words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ]
        self.assertEqual(self.sol.fullJustify(words, 20), expected)

    def test_single_word(self):
        words = ["hello"]
        expected = ["hello      "]
        self.assertEqual(self.sol.fullJustify(words, 11), expected)

    def test_single_word_exact_width(self):
        words = ["hello"]
        expected = ["hello"]
        self.assertEqual(self.sol.fullJustify(words, 5), expected)

    def test_all_words_fit_one_line(self):
        words = ["ab", "cd"]
        expected = ["ab cd  "]
        self.assertEqual(self.sol.fullJustify(words, 7), expected)

    def test_all_words_fit_one_line_last_left_justified(self):
        words = ["a", "b", "c"]
        expected = ["a b c  "]
        self.assertEqual(self.sol.fullJustify(words, 7), expected)

    def test_one_word_per_line(self):
        words = ["ab", "cd", "ef"]
        expected = ["ab  ", "cd  ", "ef  "]
        self.assertEqual(self.sol.fullJustify(words, 4), expected)

    def test_single_char_words(self):
        words = ["a", "b", "c", "d", "e"]
        expected = ["a b c", "d e  "]
        out = self.sol.fullJustify(words, 5)
        self.assertEqual(out, expected)

    def test_even_distribution(self):
        words = ["a", "b", "c", "de"]
        expected = ["a  b  c", "de     "]
        out = self.sol.fullJustify(words, 7)
        self.assertEqual(out, expected)

    def test_left_gap_gets_more(self):
        words = ["a", "bc", "def", "xyzw"]
        out = self.sol.fullJustify(words, 12)
        self.assertEqual(out, ["a   bc   def", "xyzw        "])
        out2 = self.sol.fullJustify(words, 11)
        self.assertEqual(out2, ["a   bc  def", "xyzw       "])

    def test_maxwidth_equals_sum_and_spaces(self):
        words = ["ab", "c"]
        expected = ["ab c "]
        self.assertEqual(self.sol.fullJustify(words, 5), expected)

    def test_lines_have_exact_width(self):
        words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        out = self.sol.fullJustify(words, 9)
        for line in out:
            self.assertEqual(len(line), 9)

    def test_two_words_fully_justified(self):
        words = ["ab", "cd", "ef"]
        out = self.sol.fullJustify(words, 7)
        self.assertEqual(out, ["ab   cd", "ef     "])

    def test_word_same_length_as_maxwidth(self):
        words = ["xyzwv", "ab"]
        out = self.sol.fullJustify(words, 5)
        self.assertEqual(out, ["xyzwv", "ab   "])

    def test_last_line_single_word(self):
        words = ["a", "b", "c"]
        out = self.sol.fullJustify(words, 4)
        self.assertEqual(out, ["a  b", "c   "])

    def test_symbols_in_words(self):
        words = ["a!", "b?"]
        out = self.sol.fullJustify(words, 6)
        self.assertEqual(out, ["a! b? "])

    def test_empty_lines_count(self):
        words = ["a", "b", "c", "d", "e"]
        out = self.sol.fullJustify(words, 3)
        self.assertEqual(out, ["a b", "c d", "e  "])

    def test_return_type(self):
        words = ["a", "b"]
        out = self.sol.fullJustify(words, 4)
        self.assertIsInstance(out, list)
        for line in out:
            self.assertIsInstance(line, str)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Simulation
