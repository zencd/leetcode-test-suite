# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Easy

from typing import List
import unittest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        raise Exception("Not solved yet")


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.longestCommonPrefix(["flower", "flow", "flight"]), "fl"
        )

    def test_example2(self):
        self.assertEqual(self.sol.longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_identical_strings(self):
        self.assertEqual(self.sol.longestCommonPrefix(["abc", "abc", "abc"]), "abc")

    def test_no_common_prefix(self):
        self.assertEqual(self.sol.longestCommonPrefix(["abc", "def"]), "")

    def test_single_string(self):
        self.assertEqual(self.sol.longestCommonPrefix(["abc"]), "abc")

    def test_single_character_strings(self):
        self.assertEqual(self.sol.longestCommonPrefix(["a", "a", "a"]), "a")

    def test_single_character_no_match(self):
        self.assertEqual(self.sol.longestCommonPrefix(["a", "b", "c"]), "")

    def test_empty_list(self):
        self.assertEqual(self.sol.longestCommonPrefix([]), "")

    def test_empty_string_in_list(self):
        self.assertEqual(self.sol.longestCommonPrefix(["abc", "", "def"]), "")

    def test_all_empty_strings(self):
        self.assertEqual(self.sol.longestCommonPrefix(["", "", ""]), "")

    def test_one_empty_string(self):
        self.assertEqual(self.sol.longestCommonPrefix(["", "abc"]), "")

    def test_common_prefix_is_full_short_string(self):
        self.assertEqual(self.sol.longestCommonPrefix(["abc", "ab", "a"]), "a")

    def test_prefix_at_end_of_list_order(self):
        self.assertEqual(
            self.sol.longestCommonPrefix(["f", "fl", "flow", "flower"]), "f"
        )

    def test_prefix_not_contiguous(self):
        self.assertEqual(self.sol.longestCommonPrefix(["abab", "aba", "abz"]), "ab")

    def test_differs_in_middle(self):
        self.assertEqual(self.sol.longestCommonPrefix(["abcdef", "abXdef"]), "ab")

    def test_differs_at_second_char(self):
        self.assertEqual(self.sol.longestCommonPrefix(["aa", "ab"]), "a")

    def test_differs_at_first_char(self):
        self.assertEqual(self.sol.longestCommonPrefix(["aa", "ba"]), "")

    def test_repeated_chars(self):
        self.assertEqual(self.sol.longestCommonPrefix(["aaa", "aaab", "aaaa"]), "aaa")

    def test_mixed_lengths_shared_prefix(self):
        self.assertEqual(
            self.sol.longestCommonPrefix(["prefix", "pre", "pr", "p"]), "p"
        )

    def test_all_lowercase_lowercase_boundary(self):
        self.assertEqual(
            self.sol.longestCommonPrefix(["a" * 200, "a" * 199 + "b", "a" * 198]),
            "a" * 198,
        )

    def test_two_hundred_strings(self):
        strs = ["common"] * 199 + ["commxyz"]
        self.assertEqual(self.sol.longestCommonPrefix(strs), "comm")

    def test_unicode_lowercase_only_allowed_bypass(self):
        self.assertEqual(self.sol.longestCommonPrefix(["élf", "élm"]), "él")

    def test_case_sensitive(self):
        self.assertEqual(self.sol.longestCommonPrefix(["ABC", "abc"]), "")

    def test_uppercase_common_prefix(self):
        self.assertEqual(self.sol.longestCommonPrefix(["ABC", "ABCX"]), "ABC")

    def test_mixed_case_no_common(self):
        self.assertEqual(self.sol.longestCommonPrefix(["Foo", "Boo", "Moo"]), "")

    def test_mixed_case_prefix(self):
        self.assertEqual(self.sol.longestCommonPrefix(["Foobar", "Foobaz"]), "Fooba")

    def test_whitespace_like_strings(self):
        self.assertEqual(self.sol.longestCommonPrefix([" a", " ab"]), " a")

    def test_first_string_is_shortest(self):
        self.assertEqual(self.sol.longestCommonPrefix(["ab", "abcdef", "abc"]), "ab")

    def test_first_string_differs_early(self):
        self.assertEqual(self.sol.longestCommonPrefix(["zxcv", "abcdef", "abc"]), "")

    def test_only_empty_first(self):
        self.assertEqual(self.sol.longestCommonPrefix(["", "a", "aa"]), "")


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Trie
