# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Easy

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.isSubsequence("abc", "ahbgdc"))

    def test_example2(self):
        self.assertFalse(self.sol.isSubsequence("axc", "ahbgdc"))

    def test_empty_s(self):
        self.assertTrue(self.sol.isSubsequence("", "abcde"))

    def test_empty_both(self):
        self.assertTrue(self.sol.isSubsequence("", ""))

    def test_empty_s_nonempty_t(self):
        self.assertTrue(self.sol.isSubsequence("", "a"))

    def test_empty_t_nonempty_s(self):
        self.assertFalse(self.sol.isSubsequence("a", ""))

    def test_s_equals_t(self):
        self.assertTrue(self.sol.isSubsequence("abc", "abc"))

    def test_s_is_prefix_of_t(self):
        self.assertTrue(self.sol.isSubsequence("ab", "abcd"))

    def test_s_is_suffix_of_t(self):
        self.assertTrue(self.sol.isSubsequence("cd", "abcd"))

    def test_single_char_found(self):
        self.assertTrue(self.sol.isSubsequence("a", "aaaa"))

    def test_single_char_not_found(self):
        self.assertFalse(self.sol.isSubsequence("b", "aaaa"))

    def test_wrong_order(self):
        self.assertFalse(self.sol.isSubsequence("cba", "abc"))

    def test_subsequence_with_duplicates(self):
        self.assertTrue(self.sol.isSubsequence("aa", "aabaa"))

    def test_too_many_needed(self):
        self.assertFalse(self.sol.isSubsequence("aa", "a"))

    def test_interleaved(self):
        self.assertTrue(self.sol.isSubsequence("ace", "abcde"))

    def test_interleaved_negative(self):
        self.assertFalse(self.sol.isSubsequence("aec", "abcde"))

    def test_all_same_chars(self):
        self.assertTrue(self.sol.isSubsequence("aaa", "aaaaa"))

    def test_long_t(self):
        t = "a" * 10000
        self.assertTrue(self.sol.isSubsequence("a", t))
        self.assertTrue(self.sol.isSubsequence("aa", t))

    def test_max_length_boundary(self):
        s = "a" * 100
        t = "a" * 101
        self.assertTrue(self.sol.isSubsequence(s, t))
        t = "a" * 99
        self.assertFalse(self.sol.isSubsequence(s, t))

    def test_single_letter_alphabet(self):
        self.assertTrue(self.sol.isSubsequence("z", "abczdef"))
        self.assertFalse(self.sol.isSubsequence("z", "abcdef"))

    def test_full_alphabet_in_order(self):
        t = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(self.sol.isSubsequence(t, t))
        self.assertTrue(self.sol.isSubsequence("a", t))
        self.assertTrue(self.sol.isSubsequence("z", t))
        self.assertFalse(self.sol.isSubsequence("za", t))

    def test_chars_at_end_of_t(self):
        self.assertTrue(self.sol.isSubsequence("cde", "abcde"))

    def test_chars_at_start_of_t(self):
        self.assertTrue(self.sol.isSubsequence("abc", "abcde"))

    def test_alternating_match(self):
        self.assertTrue(self.sol.isSubsequence("ab", "ababab"))
        self.assertTrue(self.sol.isSubsequence("ba", "ababab"))
        self.assertFalse(self.sol.isSubsequence("cc", "ababab"))

    def test_scattered_single_chars(self):
        self.assertTrue(self.sol.isSubsequence("ad", "abbcdd"))
        self.assertFalse(self.sol.isSubsequence("ae", "abbcdd"))


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String, Dynamic Programming
