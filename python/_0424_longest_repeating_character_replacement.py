# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Medium

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.characterReplacement("ABAB", 2), 4)
        self.assertEqual(self.sol.characterReplacement("AABABBA", 1), 4)

    def test_single_char(self):
        self.assertEqual(self.sol.characterReplacement("A", 0), 1)
        self.assertEqual(self.sol.characterReplacement("A", 1), 1)

    def test_k_zero(self):
        self.assertEqual(self.sol.characterReplacement("ABBB", 0), 3)
        self.assertEqual(self.sol.characterReplacement("AABBC", 0), 2)
        self.assertEqual(self.sol.characterReplacement("ABC", 0), 1)
        self.assertEqual(self.sol.characterReplacement("ABAB", 0), 1)

    def test_k_large_covers_all(self):
        self.assertEqual(self.sol.characterReplacement("ABC", 3), 3)
        self.assertEqual(self.sol.characterReplacement("ABAB", 2), 4)
        self.assertEqual(self.sol.characterReplacement("AABABBA", 100), 7)
        self.assertEqual(self.sol.characterReplacement("ABCB", 3), 4)

    def test_all_same_chars(self):
        self.assertEqual(self.sol.characterReplacement("AAAA", 0), 4)
        self.assertEqual(self.sol.characterReplacement("AAAA", 2), 4)

    def test_alternating(self):
        self.assertEqual(self.sol.characterReplacement("AABABBA", 1), 4)
        self.assertEqual(self.sol.characterReplacement("ABA", 1), 3)
        self.assertEqual(self.sol.characterReplacement("BABA", 1), 3)
        self.assertEqual(self.sol.characterReplacement("BABA", 2), 4)

    def test_single_replacement_needed(self):
        self.assertEqual(self.sol.characterReplacement("ABCB", 1), 3)
        self.assertEqual(self.sol.characterReplacement("BACCBA", 2), 4)

    def test_baccba(self):
        self.assertEqual(self.sol.characterReplacement("BACCBA", 2), 4)

    def test_leetcode_case_abcb(self):
        self.assertEqual(self.sol.characterReplacement("ABCB", 2), 4)

    def test_replacement_in_middle(self):
        self.assertEqual(self.sol.characterReplacement("AABBB", 1), 4)
        self.assertEqual(self.sol.characterReplacement("BBBAA", 1), 4)

    def test_result_not_dependent_on_latest_max(self):
        self.assertEqual(self.sol.characterReplacement("AAABBB", 2), 5)

    def test_long_string_performance(self):
        s = "AB" * 50000
        self.assertLessEqual(self.sol.characterReplacement(s, 50), len(s))
        self.assertEqual(self.sol.characterReplacement("AB" * 50000, 50000), 100000)

    def test_single_char_repeated(self):
        self.assertEqual(self.sol.characterReplacement("BBBB", 0), 4)

    def test_distinct_all(self):
        self.assertEqual(self.sol.characterReplacement("ABCDEF", 0), 1)
        self.assertEqual(self.sol.characterReplacement("ABCDEF", 1), 2)
        self.assertEqual(self.sol.characterReplacement("ABCDEF", 5), 6)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Sliding Window
