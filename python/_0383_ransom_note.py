# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/
# Easy

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertFalse(self.sol.canConstruct("a", "b"))

    def test_example_2(self):
        self.assertFalse(self.sol.canConstruct("aa", "ab"))

    def test_example_3(self):
        self.assertTrue(self.sol.canConstruct("aa", "aab"))

    def test_exact_match(self):
        self.assertTrue(self.sol.canConstruct("abc", "abc"))

    def test_reorder(self):
        self.assertTrue(self.sol.canConstruct("cba", "abc"))

    def test_note_longer_than_magazine(self):
        self.assertFalse(self.sol.canConstruct("aaa", "aa"))

    def test_single_char_true(self):
        self.assertTrue(self.sol.canConstruct("a", "a"))

    def test_single_char_false(self):
        self.assertFalse(self.sol.canConstruct("a", "b"))

    def test_all_letters_needed(self):
        self.assertTrue(
            self.sol.canConstruct(
                "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"
            )
        )

    def test_missing_one_letter(self):
        self.assertFalse(
            self.sol.canConstruct(
                "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxy"
            )
        )

    def test_duplicate_letters_sufficient(self):
        self.assertTrue(self.sol.canConstruct("aaaa", "aaaa"))

    def test_duplicate_letters_insufficient(self):
        self.assertFalse(self.sol.canConstruct("aaaa", "aaa"))

    def test_magazine_has_extra_letters(self):
        self.assertTrue(self.sol.canConstruct("le", "hello"))

    def test_case_sensitive_distinct(self):
        self.assertTrue(self.sol.canConstruct("zz", "zzz"))

    def test_long_note_covered_by_long_magazine(self):
        magazine = "abc" * 40000
        note = "abc" * 39999
        self.assertTrue(self.sol.canConstruct(note, magazine))

    def test_repetition_exceeds_magazine(self):
        self.assertFalse(self.sol.canConstruct("a" * 100, "a" * 99))

    def test_note_equals_magazine_length(self):
        self.assertTrue(self.sol.canConstruct("aba", "aab"))

    def test_magazine_empty_note_nonempty(self):
        self.assertFalse(self.sol.canConstruct("a", ""))

    def test_note_empty(self):
        self.assertTrue(self.sol.canConstruct("", "a"))


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Counting
