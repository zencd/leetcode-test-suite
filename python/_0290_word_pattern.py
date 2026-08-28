# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/
# Easy

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.wordPattern("abba", "dog cat cat dog"))

    def test_example2(self):
        self.assertFalse(self.s.wordPattern("abba", "dog cat cat fish"))

    def test_example3(self):
        self.assertFalse(self.s.wordPattern("aaaa", "dog cat cat dog"))

    def test_simple_ab(self):
        self.assertTrue(self.s.wordPattern("ab", "dog cat"))

    def test_two_letters_same_word(self):
        self.assertFalse(self.s.wordPattern("abba", "dog dog dog dog"))

    def test_pattern_longer_than_words(self):
        self.assertFalse(self.s.wordPattern("abc", "dog cat"))

    def test_words_more_than_pattern(self):
        self.assertFalse(self.s.wordPattern("ab", "dog cat dog"))

    def test_single_char_pattern(self):
        self.assertTrue(self.s.wordPattern("a", "dog"))

    def test_single_char_mismatch(self):
        self.assertFalse(self.s.wordPattern("a", "dog cat"))

    def test_repeating_word_requires_repeating_char(self):
        self.assertFalse(self.s.wordPattern("ab", "dog dog"))

    def test_all_unique(self):
        self.assertTrue(self.s.wordPattern("abcd", "dog cat fish bird"))

    def test_all_same_char_same_word(self):
        self.assertTrue(self.s.wordPattern("aaaa", "dog dog dog dog"))

    def test_three_way_conflict(self):
        self.assertFalse(self.s.wordPattern("abc", "dog cat dog"))

    def test_long_pattern_single_words(self):
        pattern = "a" * 300
        self.assertTrue(self.s.wordPattern(pattern, "word " * 299 + "word"))

    def test_long_pattern_fail(self):
        pattern = "a" * 300
        self.assertFalse(self.s.wordPattern(pattern, ("word " * 299) + "other"))

    def test_single_long_word(self):
        self.assertTrue(self.s.wordPattern("a", "x" * 3000))

    def test_mixed_mapping_order(self):
        self.assertTrue(self.s.wordPattern("baab", "cat dog dog cat"))

    def test_word_reused_by_two_letters(self):
        self.assertFalse(self.s.wordPattern("abac", "dog cat fish dog"))

    def test_letter_reused_inconsistent_late(self):
        self.assertFalse(self.s.wordPattern("abcb", "dog cat fish bird"))


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String
