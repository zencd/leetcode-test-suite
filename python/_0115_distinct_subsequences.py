# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# Hard

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.numDistinct("rabbbit", "rabbit"), 3)

    def test_example2(self):
        self.assertEqual(self.sol.numDistinct("babgbag", "bag"), 5)

    def test_empty_t(self):
        self.assertEqual(self.sol.numDistinct("abc", ""), 1)

    def test_empty_s(self):
        self.assertEqual(self.sol.numDistinct("", "a"), 0)

    def test_both_empty(self):
        self.assertEqual(self.sol.numDistinct("", ""), 1)

    def test_single_chars_match(self):
        self.assertEqual(self.sol.numDistinct("a", "a"), 1)

    def test_single_chars_no_match(self):
        self.assertEqual(self.sol.numDistinct("a", "b"), 0)

    def test_t_longer_than_s(self):
        self.assertEqual(self.sol.numDistinct("ab", "abc"), 0)

    def test_exact_match(self):
        self.assertEqual(self.sol.numDistinct("abc", "abc"), 1)

    def test_s_subsequence_of_t(self):
        self.assertEqual(self.sol.numDistinct("ab", "ba"), 0)

    def test_repeated_s_chars(self):
        self.assertEqual(self.sol.numDistinct("aaaa", "aa"), 6)

    def test_repeated_both(self):
        self.assertEqual(self.sol.numDistinct("aaaa", "aaa"), 4)

    def test_all_chars_identical(self):
        self.assertEqual(self.sol.numDistinct("aa", "a"), 2)

    def test_multiple_match_positions(self):
        self.assertEqual(self.sol.numDistinct("aaa", "a"), 3)

    def test_non_matching_chars(self):
        self.assertEqual(self.sol.numDistinct("abc", "d"), 0)

    def test_interleaved_matches(self):
        self.assertEqual(self.sol.numDistinct("ababc", "abc"), 3)

    def test_single_char_each(self):
        self.assertEqual(self.sol.numDistinct("z", "z"), 1)

    def test_large_s_small_t(self):
        self.assertEqual(self.sol.numDistinct("a" * 1000, "b"), 0)

    def test_large_strings(self):
        s = "a" * 500 + "b" * 500
        t = "ab" * 10
        self.assertEqual(self.sol.numDistinct(s, t), 0)

    def test_uppercase_letters(self):
        self.assertEqual(self.sol.numDistinct("AABB", "AB"), 4)

    def test_mixed_case(self):
        self.assertEqual(self.sol.numDistinct("AaAa", "Aa"), 3)

    def test_result_fits_int(self):
        self.assertEqual(self.sol.numDistinct("abcdefghijklmnopqrstuvwxyz", "z"), 1)

    def test_no_valid_subsequence(self):
        self.assertEqual(self.sol.numDistinct("abcabc", "defg"), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming
