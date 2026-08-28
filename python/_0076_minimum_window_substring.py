# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# Hard

from collections import Counter
import unittest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        raise Exception("Not solved yet")


class TestMinWindow(unittest.TestCase):
    def test_example_1(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_example_2(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("a", "a"), "a")

    def test_example_3(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("a", "aa"), "")

    def test_empty_result(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("ab", "d"), "")

    def test_t_longer_than_s(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("ab", "abc"), "")

    def test_single_char_match(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("abc", "b"), "b")

    def test_duplicates_in_t(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("aabbabbaab", "aab"), "aab")

    def test_window_at_start(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("bancABC", "ABC"), "ABC")

    def test_window_at_end(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("ABabc", "abc"), "abc")

    def test_all_same_chars(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("aaaa", "aa"), "aa")

    def test_identical_strings(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("abcdef", "abcdef"), "abcdef")

    def test_case_sensitivity(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("AaAbBb", "ab"), "aAb")

    def test_case_sensitivity_no_match(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("abc", "ABC"), "")

    def test_interleaved(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("ADOBECODEBANC", "AABC"), "ADOBECODEBA")

    def test_repeated_target_chars(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("AAAB", "AAB"), "AAB")

    def test_single_char_s_single_char_t_mismatch(self):
        sol = Solution()
        self.assertEqual(sol.minWindow("a", "b"), "")

    def test_unicode_free_alphabetic_long(self):
        sol = Solution()
        s = "a" * 50 + "b" + "a" * 50
        self.assertEqual(sol.minWindow(s, "ab"), "ab")

    def test_t_of_many_unique(self):
        sol = Solution()
        self.assertEqual(
            sol.minWindow("zyxwvutsrqponmlkjihgfedcba", "az"),
            "zyxwvutsrqponmlkjihgfedcba",
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Sliding Window
