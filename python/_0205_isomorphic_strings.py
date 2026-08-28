# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# Easy

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertTrue(self.solution.isIsomorphic("egg", "add"))
        self.assertFalse(self.solution.isIsomorphic("f11", "b23"))
        self.assertTrue(self.solution.isIsomorphic("paper", "title"))

    def test_single_characters(self):
        self.assertTrue(self.solution.isIsomorphic("a", "a"))
        self.assertTrue(self.solution.isIsomorphic("a", "b"))
        self.assertFalse(self.solution.isIsomorphic("a", ""))

    def test_identical_strings(self):
        self.assertTrue(self.solution.isIsomorphic("abc", "abc"))
        self.assertTrue(self.solution.isIsomorphic("aaaa", "aaaa"))
        self.assertTrue(self.solution.isIsomorphic("paper", "paper"))

    def test_distinct_characters_both_sides(self):
        self.assertTrue(self.solution.isIsomorphic("abc", "xyz"))
        self.assertTrue(self.solution.isIsomorphic("abcd", "wxyz"))

    def test_length_mismatch(self):
        self.assertFalse(self.solution.isIsomorphic("abc", "ab"))
        self.assertFalse(self.solution.isIsomorphic("ab", "abc"))
        self.assertFalse(self.solution.isIsomorphic("", "a"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isIsomorphic("", ""))

    def test_conflicting_mapping_forward(self):
        self.assertFalse(self.solution.isIsomorphic("ab", "aa"))
        self.assertFalse(self.solution.isIsomorphic("aa", "ab"))

    def test_conflicting_mapping_backward(self):
        self.assertFalse(self.solution.isIsomorphic("abb", "bab"))
        self.assertTrue(self.solution.isIsomorphic("aba", "bab"))
        self.assertTrue(self.solution.isIsomorphic("ab", "ba"))

    def test_valid_self_mapping(self):
        self.assertTrue(self.solution.isIsomorphic("a", "a"))
        self.assertTrue(self.solution.isIsomorphic("xyz", "xyz"))
        self.assertTrue(self.solution.isIsomorphic("aba", "cdc"))

    def test_numeric_and_symbols(self):
        self.assertTrue(self.solution.isIsomorphic("12!!$", "34%%&"))
        self.assertFalse(self.solution.isIsomorphic("12!!$", "34%%4"))

    def test_repeated_pattern(self):
        self.assertTrue(self.solution.isIsomorphic("abab", "cdcd"))
        self.assertFalse(self.solution.isIsomorphic("abab", "cdce"))
        self.assertTrue(self.solution.isIsomorphic("abba", "baab"))

    def test_unicode_characters(self):
        self.assertTrue(self.solution.isIsomorphic("éé", "zz"))
        self.assertFalse(self.solution.isIsomorphic("éé", "zy"))

    def test_spaces(self):
        self.assertTrue(self.solution.isIsomorphic("a b", "c d"))
        self.assertFalse(self.solution.isIsomorphic("a b", "cdd"))

    def test_case_sensitivity(self):
        self.assertFalse(self.solution.isIsomorphic("Aa", "bb"))
        self.assertTrue(self.solution.isIsomorphic("Aa", "Bb"))

    def test_large_input(self):
        s = "a" * 50000
        t = "b" * 50000
        self.assertTrue(self.solution.isIsomorphic(s, t))


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String
