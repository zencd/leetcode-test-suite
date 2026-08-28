# 214. Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome/
# Hard

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_string(self):
        self.assertEqual(self.sol.shortestPalindrome(""), "")

    def test_single_char(self):
        self.assertEqual(self.sol.shortestPalindrome("a"), "a")

    def test_already_palindrome(self):
        self.assertEqual(self.sol.shortestPalindrome("a"), "a")
        self.assertEqual(self.sol.shortestPalindrome("aba"), "aba")
        self.assertEqual(self.sol.shortestPalindrome("abba"), "abba")
        self.assertEqual(self.sol.shortestPalindrome("abcba"), "abcba")
        self.assertEqual(self.sol.shortestPalindrome("aa"), "aa")

    def test_example1(self):
        self.assertEqual(self.sol.shortestPalindrome("aacecaaa"), "aaacecaaa")

    def test_example2(self):
        self.assertEqual(self.sol.shortestPalindrome("abcd"), "dcbabcd")

    def test_all_same_chars(self):
        self.assertEqual(self.sol.shortestPalindrome("aaaa"), "aaaa")

    def test_no_palindromic_prefix(self):
        self.assertEqual(self.sol.shortestPalindrome("abcde"), "edcbabcde")

    def test_repeated_chars(self):
        self.assertEqual(self.sol.shortestPalindrome("aaaab"), "baaaab")

    def test_short_cases(self):
        self.assertEqual(self.sol.shortestPalindrome("ab"), "bab")
        self.assertEqual(self.sol.shortestPalindrome("ba"), "aba")
        self.assertEqual(self.sol.shortestPalindrome("aa"), "aa")
        self.assertEqual(self.sol.shortestPalindrome("abab"), "babab")

    def test_output_is_palindrome(self):
        cases = ["aacecaaa", "abcd", "abb", "cabca", "gkadbml"]
        for s in cases:
            out = self.sol.shortestPalindrome(s)
            self.assertEqual(out, out[::-1], f"not a palindrome: {out}")
            self.assertTrue(out.endswith(s), f"original not at the end: {out}")

    def test_optimality(self):
        def expected(s):
            n = len(s)
            longest = 0
            for i in range(n):
                if s[: i + 1] == s[: i + 1][::-1]:
                    longest = i + 1
            return (s[::-1][: n - longest]) + s

        cases = [
            "a",
            "ab",
            "aa",
            "aba",
            "abc",
            "ababa",
            "abba",
            "abb",
            "cbbd",
            "aaaaab",
            "ababab",
        ]
        for s in cases:
            self.assertEqual(self.sol.shortestPalindrome(s), expected(s))

    def test_long_string(self):
        s = "abcdefghijklmnopqrstuvwxyz" * 2083 + "a"
        s = s[:50000]
        out = self.sol.shortestPalindrome(s)
        self.assertEqual(len(out), len(s) + 50000 - 1)
        self.assertEqual(out, out[::-1])

    def test_long_all_same(self):
        s = "a" * 50000
        self.assertEqual(self.sol.shortestPalindrome(s), s)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Rolling Hash, String Matching, Hash Function, Manacher, Z Algorithm, Knuth–Morris–Pratt Algorithm
