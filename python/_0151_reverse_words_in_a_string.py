# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
# Medium

class Solution:
    def reverseWords(self, s: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic(self):
        self.assertEqual(self.sol.reverseWords("the sky is blue"), "blue is sky the")

    def test_single_word(self):
        self.assertEqual(self.sol.reverseWords("hello"), "hello")

    def test_leading_trailing_spaces(self):
        self.assertEqual(self.sol.reverseWords("  hello world  "), "world hello")

    def test_multiple_spaces_between_words(self):
        self.assertEqual(self.sol.reverseWords("a good   example"), "example good a")

    def test_only_spaces_around_single_word(self):
        self.assertEqual(self.sol.reverseWords("   a   "), "a")

    def test_two_words(self):
        self.assertEqual(self.sol.reverseWords("abc def"), "def abc")

    def test_mixed_spaces(self):
        self.assertEqual(self.sol.reverseWords("  foo   bar baz  "), "baz bar foo")

    def test_digits_in_words(self):
        self.assertEqual(self.sol.reverseWords("a1 b2 c3"), "c3 b2 a1")

    def test_uppercase_words(self):
        self.assertEqual(self.sol.reverseWords("HELLO WORLD"), "WORLD HELLO")

    def test_single_character(self):
        self.assertEqual(self.sol.reverseWords("a"), "a")

    def test_adjacent_words_reversed_identical(self):
        self.assertEqual(self.sol.reverseWords("ab ab ab"), "ab ab ab")

    def test_no_spaces_at_all(self):
        self.assertEqual(self.sol.reverseWords("abcdefgh"), "abcdefgh")

    def test_many_spaces(self):
        s = "a" + " " * 10 + "b" + " " * 10 + "c"
        self.assertEqual(self.sol.reverseWords(s), "c b a")

    def test_long_input(self):
        s = " ".join(str(i) for i in range(100))
        expected = " ".join(str(i) for i in range(99, -1, -1))
        self.assertEqual(self.sol.reverseWords("   " + s + "   "), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String
