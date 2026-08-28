# 318. Maximum Product of Word Lengths
# https://leetcode.com/problems/maximum-product-of-word-lengths/
# Medium

from typing import List
import unittest


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def max_product(self, words: List[str]) -> int:
        return self.solution.maxProduct(words)

    def test_example_1(self):
        self.assertEqual(
            16, self.max_product(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
        )

    def test_example_2(self):
        self.assertEqual(
            4, self.max_product(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
        )

    def test_example_3(self):
        self.assertEqual(0, self.max_product(["a", "aa", "aaa", "aaaa"]))

    def test_no_disjoint_pair(self):
        self.assertEqual(0, self.max_product(["ab", "bc", "ca"]))

    def test_two_words_disjoint(self):
        self.assertEqual(4, self.max_product(["ab", "cd"]))

    def test_two_words_overlap(self):
        self.assertEqual(0, self.max_product(["ab", "bc"]))

    def test_single_letter_disjoint(self):
        self.assertEqual(1, self.max_product(["a", "b"]))

    def test_single_letter_same(self):
        self.assertEqual(0, self.max_product(["a", "a"]))

    def test_all_same_letter(self):
        self.assertEqual(0, self.max_product(["a", "aa", "aaa", "aaaa"]))

    def test_overlapping_pair_beats_single_letters(self):
        self.assertEqual(4, self.max_product(["ab", "bc", "cd", "abcd", "a", "b"]))

    def test_disjoint_long_words(self):
        self.assertEqual(64, self.max_product(["abcdefgh", "ijklmnop"]))

    def test_duplicate_words_disjoint_other(self):
        self.assertEqual(2, self.max_product(["ab", "ab", "c", "d"]))

    def test_best_pair_not_last(self):
        self.assertEqual(
            16, self.max_product(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
        )

    def test_three_letter_disjoint_triples(self):
        self.assertEqual(9, self.max_product(["abc", "def", "ghi", "jkl"]))

    def test_pair_selection_between_several(self):
        self.assertEqual(3, self.max_product(["abc", "d", "e", "f", "ab", "c"]))

    def test_long_words_constraint_like(self):
        self.assertEqual(1000000, self.max_product(["a" * 1000, "b" * 1000]))

    def test_repeated_letters_inside_word(self):
        self.assertEqual(6, self.max_product(["aab", "cc"]))

    def test_only_two_words(self):
        self.assertEqual(4, self.max_product(["ab", "cd"]))

    def test_z_and_a(self):
        self.assertEqual(1, self.max_product(["z", "a"]))

    def test_full_alphabet_and_complement_split(self):
        self.assertEqual(
            48,
            self.max_product(
                ["abcdefghijklmnopqrstuvwx", "yz", "abcdefghijklmnopqrstuvwxyz"]
            ),
        )

    def test_no_valid_pair_returns_zero(self):
        self.assertEqual(0, self.max_product(["hello", "world"]))

    def test_identical_words(self):
        self.assertEqual(0, self.max_product(["test", "test"]))

    def test_anagram_words_overlap(self):
        self.assertEqual(0, self.max_product(["ab", "ba"]))

    def test_max_lengths_disjoint_words(self):
        w1 = "a" * 500
        w2 = "b" * 500
        self.assertEqual(300000, self.max_product([w1, w2, "a" * 600, "ab"]))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Bit Manipulation
