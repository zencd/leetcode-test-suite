# 132. Palindrome Partitioning II
# https://leetcode.com/problems/palindrome-partitioning-ii/
# Hard

class Solution:
    def minCut(self, s: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_char(self):
        self.assertEqual(self.sol.minCut("a"), 0)

    def test_all_same_single(self):
        self.assertEqual(self.sol.minCut("z"), 0)

    def test_two_same_chars(self):
        self.assertEqual(self.sol.minCut("aa"), 0)

    def test_two_diff_chars(self):
        self.assertEqual(self.sol.minCut("ab"), 1)

    def test_example_aab(self):
        self.assertEqual(self.sol.minCut("aab"), 1)

    def test_whole_palindrome(self):
        self.assertEqual(self.sol.minCut("racecar"), 0)

    def test_single_char_palindromes(self):
        self.assertEqual(self.sol.minCut("abcd"), 3)

    def test_even_length_palindrome(self):
        self.assertEqual(self.sol.minCut("abba"), 0)

    def test_mixed(self):
        self.assertEqual(self.sol.minCut("aabbc"), 2)

    def test_all_same(self):
        self.assertEqual(self.sol.minCut("aaaa"), 0)

    def test_three_chars(self):
        self.assertEqual(self.sol.minCut("aba"), 0)
        self.assertEqual(self.sol.minCut("abb"), 1)
        self.assertEqual(self.sol.minCut("abc"), 2)

    def test_long_all_distinct(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.sol.minCut(s), len(s) - 1)

    def test_palindrome_with_suffix(self):
        self.assertEqual(self.sol.minCut("abacd"), 2)

    def test_double_palindrome(self):
        self.assertEqual(self.sol.minCut("aaabbb"), 1)

    def test_large_single_palindrome(self):
        s = "a" * 2000
        self.assertEqual(self.sol.minCut(s), 0)

    def test_large_alternating(self):
        self.assertEqual(self.sol.minCut("ab" * 999 + "a"), 0)
        self.assertEqual(self.sol.minCut("ab" * 1000), 1)

    def test_large_odd_palindrome(self):
        half = "abcdef"
        s = half + half[::-1]
        self.assertEqual(self.sol.minCut(s), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming
