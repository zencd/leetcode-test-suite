# 344. Reverse String
# https://leetcode.com/problems/reverse-string/
# Easy

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        s = ["h", "e", "l", "l", "o"]
        self.sol.reverseString(s)
        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_example2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        self.sol.reverseString(s)
        self.assertEqual(s, ["h", "a", "n", "n", "a", "H"])

    def test_single_character(self):
        s = ["a"]
        self.sol.reverseString(s)
        self.assertEqual(s, ["a"])

    def test_two_characters(self):
        s = ["a", "b"]
        self.sol.reverseString(s)
        self.assertEqual(s, ["b", "a"])

    def test_already_reversed_palindrome(self):
        s = ["a", "b", "a"]
        self.sol.reverseString(s)
        self.assertEqual(s, ["a", "b", "a"])

    def test_all_same_characters(self):
        s = ["x", "x", "x", "x"]
        self.sol.reverseString(s)
        self.assertEqual(s, ["x", "x", "x", "x"])

    def test_digits(self):
        s = ["1", "2", "3", "4", "5"]
        self.sol.reverseString(s)
        self.assertEqual(s, ["5", "4", "3", "2", "1"])

    def test_spaces_and_punctuation(self):
        s = ["a", " ", "b", "!", "c"]
        self.sol.reverseString(s)
        self.assertEqual(s, ["c", "!", "b", " ", "a"])

    def test_full_printable_ascii(self):
        s = [chr(c) for c in range(32, 127)]
        original = list(s)
        self.sol.reverseString(s)
        self.assertEqual(s, original[::-1])

    def test_modifies_in_place(self):
        s = ["a", "b", "c", "d"]
        self.sol.reverseString(s)
        self.assertEqual(s, ["d", "c", "b", "a"])

    def test_returns_none(self):
        s = ["a", "b", "c"]
        self.assertIsNone(self.sol.reverseString(s))

    def test_reversal_is_involution(self):
        s = ["x", "y", "z", "w"]
        original = list(s)
        self.sol.reverseString(s)
        self.sol.reverseString(s)
        self.assertEqual(s, original)
        self.assertIsNot(s, original)

    def test_larger_even_length(self):
        s = [chr(65 + i % 26) for i in range(1000)]
        original = list(s)
        self.sol.reverseString(s)
        self.assertEqual(s, original[::-1])

    def test_larger_odd_length_matches_reverse(self):
        s = [chr(97 + i % 26) for i in range(999)]
        expected = list(s)
        self.sol.reverseString(s)
        self.assertEqual(s, expected[::-1])


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String
