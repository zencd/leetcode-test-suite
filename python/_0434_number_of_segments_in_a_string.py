# 434. Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/
# Easy

class Solution:
    def countSegments(self, s: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.countSegments("Hello, my name is John"), 5)

    def test_example_2(self):
        self.assertEqual(self.sol.countSegments("Hello"), 1)

    def test_empty_string(self):
        self.assertEqual(self.sol.countSegments(""), 0)

    def test_single_space(self):
        self.assertEqual(self.sol.countSegments(" "), 0)

    def test_single_character(self):
        self.assertEqual(self.sol.countSegments("a"), 1)

    def test_leading_trailing_and_multiple_spaces(self):
        self.assertEqual(self.sol.countSegments("  a  b  c  "), 3)

    def test_many_spaces_between_segments(self):
        self.assertEqual(self.sol.countSegments("a    b    c"), 3)

    def test_only_spaces(self):
        self.assertEqual(self.sol.countSegments("      "), 0)

    def test_punctuation_segments(self):
        self.assertEqual(self.sol.countSegments("!@#$%^&*()_+-=',.:"), 1)

    def test_digits_and_mixed_characters(self):
        self.assertEqual(self.sol.countSegments("abc123 456def"), 2)

    def test_single_word_after_spaces(self):
        self.assertEqual(self.sol.countSegments("     hello"), 1)

    def test_word_then_trailing_spaces(self):
        self.assertEqual(self.sol.countSegments("hello     "), 1)

    def test_punctuation_around_spaces(self):
        self.assertEqual(self.sol.countSegments(", ."), 2)

    def test_all_single_char_segments(self):
        self.assertEqual(self.sol.countSegments("a b c d e"), 5)

    def test_max_length_string(self):
        self.assertEqual(self.sol.countSegments("a " * 150), 150)

    def test_max_length_single_segment(self):
        self.assertEqual(self.sol.countSegments("a" * 300), 1)

    def test_max_length_all_spaces(self):
        self.assertEqual(self.sol.countSegments(" " * 300), 0)

    def test_alternating_char_space(self):
        self.assertEqual(self.sol.countSegments("a b c d"), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: String
