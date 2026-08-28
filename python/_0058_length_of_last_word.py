# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Easy

import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        raise Exception("Not solved yet")


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)

    def test_example2(self):
        self.assertEqual(
            self.solution.lengthOfLastWord("   fly me   to   the moon  "), 4
        )

    def test_example3(self):
        self.assertEqual(self.solution.lengthOfLastWord("luffy is still joyboy"), 6)

    def test_single_word_no_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello"), 5)

    def test_single_character(self):
        self.assertEqual(self.solution.lengthOfLastWord("a"), 1)

    def test_single_word_trailing_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello   "), 5)

    def test_single_word_leading_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("   Hello"), 5)

    def test_single_word_surrounded_by_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("  Hello  "), 5)

    def test_single_char_word_with_spaces(self):
        self.assertEqual(self.solution.lengthOfLastWord("a b c "), 1)

    def test_words_of_length_one(self):
        self.assertEqual(self.solution.lengthOfLastWord("a b c d"), 1)

    def test_multiple_spaces_between_words(self):
        self.assertEqual(self.solution.lengthOfLastWord("a    b     c"), 1)

    def test_many_spaces_between_words(self):
        self.assertEqual(self.solution.lengthOfLastWord("word1     word2  "), 5)

    def test_leading_spaces_only_before_last_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("   abc"), 3)

    def test_trailing_spaces_only_after_last_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("abc     "), 3)

    def test_last_word_single_char(self):
        self.assertEqual(self.solution.lengthOfLastWord("abcdefghijk 1"), 1)

    def test_uppercase_letters(self):
        self.assertEqual(self.solution.lengthOfLastWord("FOO BAR"), 3)

    def test_mixed_case(self):
        self.assertEqual(self.solution.lengthOfLastWord("hELLO wORLD"), 5)

    def test_two_words(self):
        self.assertEqual(self.solution.lengthOfLastWord("one two"), 3)

    def test_long_last_word(self):
        s = " " + "a" * 999
        self.assertEqual(self.solution.lengthOfLastWord(s), 999)

    def test_long_string_with_trailing_spaces(self):
        s = "word " * 500 + "final" + " " * 100
        self.assertEqual(self.solution.lengthOfLastWord(s), 5)

    def test_long_string_all_spaces_then_word(self):
        s = " " * 1000 + "word"
        self.assertEqual(self.solution.lengthOfLastWord(s), 4)

    def test_alternating_spaces_and_letters(self):
        self.assertEqual(self.solution.lengthOfLastWord("a b a b a"), 1)

    def test_result_is_int(self):
        self.assertIsInstance(self.solution.lengthOfLastWord("test"), int)


if __name__ == "__main__":
    unittest.main()

# Tags: String
