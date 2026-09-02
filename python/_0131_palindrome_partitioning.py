# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/
# Medium

from typing import List
import unittest


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.partition("aab"), [["a", "a", "b"], ["aa", "b"]])

    def test_example_2(self):
        self.assertEqual(self.solution.partition("a"), [["a"]])

    def test_all_same_chars(self):
        self.assertEqual(self.solution.partition("aaa"), [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]])

    def test_all_distinct(self):
        self.assertEqual(self.solution.partition("abc"), [["a", "b", "c"]])

    def test_single_palindrome(self):
        self.assertEqual(self.solution.partition("aba"), [["a", "b", "a"], ["aba"]])

    def test_full_palindrome(self):
        self.assertEqual(self.solution.partition("abba"), [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]])

    def test_two_palindromes(self):
        self.assertEqual(self.solution.partition("abab"), [["a", "b", "a", "b"], ["a", "bab"], ["aba", "b"]])

    def test_empty_like_constraint_edge(self):
        self.assertEqual(self.solution.partition("b"), [["b"]])

    def test_two_chars_same(self):
        self.assertEqual(self.solution.partition("aa"), [["a", "a"], ["aa"]])

    def test_two_chars_diff(self):
        self.assertEqual(self.solution.partition("ab"), [["a", "b"]])

    def test_three_distinct(self):
        self.assertEqual(self.solution.partition("abcd"), [["a", "b", "c", "d"]])

    def test_mixed_longer(self):
        expected = [
            ["a", "a", "b", "a"],
            ["a", "aba"],
            ["aa", "b", "a"],
        ]
        self.assertEqual(self.solution.partition("aaba"), expected)

    def test_all_results_are_valid_partitions(self):
        s = "aabbc"
        for part in self.solution.partition(s):
            self.assertEqual("".join(part), s)
            for sub in part:
                self.assertEqual(sub, sub[::-1])

    def test_order_independent_result(self):
        s = "ababa"
        result = self.solution.partition(s)
        self.assertEqual(
            sorted(map(tuple, result)),
            sorted(
                map(
                    tuple,
                    [
                        ["a", "b", "a", "b", "a"],
                        ["a", "b", "aba"],
                        ["a", "bab", "a"],
                        ["aba", "b", "a"],
                        ["ababa"],
                    ],
                )
            ),
        )

    def test_longest_allowed_string(self):
        s = "a" * 16
        result = self.solution.partition(s)
        self.assertEqual(len(result), 2**15)
        for part in result:
            self.assertEqual("".join(part), s)

    def test_returns_lists_not_shared_refs(self):
        result = self.solution.partition("aa")
        result[0].append("extra")
        self.assertEqual(self.solution.partition("aa"), [["a", "a"], ["aa"]])


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming, Backtracking
