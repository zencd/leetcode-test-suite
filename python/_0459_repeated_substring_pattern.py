# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/
# Easy

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.repeatedSubstringPattern("abab"))
        self.assertFalse(self.sol.repeatedSubstringPattern("aba"))
        self.assertTrue(self.sol.repeatedSubstringPattern("abcabcabcabc"))

    def test_single_character(self):
        self.assertFalse(self.sol.repeatedSubstringPattern("a"))

    def test_same_characters(self):
        self.assertTrue(self.sol.repeatedSubstringPattern("aa"))
        self.assertTrue(self.sol.repeatedSubstringPattern("aaaa"))
        self.assertFalse(self.sol.repeatedSubstringPattern("aaaab"))

    def test_two_copies(self):
        self.assertTrue(self.sol.repeatedSubstringPattern("abcabc"))
        self.assertFalse(self.sol.repeatedSubstringPattern("abca"))
        self.assertTrue(self.sol.repeatedSubstringPattern("ababab"))
        self.assertTrue(self.sol.repeatedSubstringPattern("xyzxyz"))
        self.assertFalse(self.sol.repeatedSubstringPattern("xyzxyzx"))

    def test_long_repeats(self):
        self.assertTrue(self.sol.repeatedSubstringPattern("abc" * 10))
        self.assertTrue(self.sol.repeatedSubstringPattern("ab" * 5))
        self.assertFalse(self.sol.repeatedSubstringPattern("abc" * 10 + "a"))

    def test_overlapping_patterns(self):
        self.assertTrue(self.sol.repeatedSubstringPattern("aaaaaaa"))
        self.assertTrue(self.sol.repeatedSubstringPattern("ababababab"))
        self.assertFalse(self.sol.repeatedSubstringPattern("abababa"))
        self.assertTrue(self.sol.repeatedSubstringPattern("bcbc"))
        self.assertFalse(self.sol.repeatedSubstringPattern("bcb"))

    def test_prime_length_strings(self):
        self.assertFalse(self.sol.repeatedSubstringPattern("abcdef"))
        self.assertFalse(self.sol.repeatedSubstringPattern("abcde"))
        self.assertTrue(self.sol.repeatedSubstringPattern("ab" * 7))

    def test_mixed_repeats(self):
        self.assertTrue(self.sol.repeatedSubstringPattern("abacabac"))
        self.assertEqual(
            self.sol.repeatedSubstringPattern("abaaba"),
            True,
        )

    def test_all_lowercase_constraint(self):
        for ch in "abcdefghijklmnopqrstuvwxyz":
            self.assertTrue(self.sol.repeatedSubstringPattern(ch * 3))

    def test_large_input(self):
        s = "a" * 10000
        self.assertTrue(self.sol.repeatedSubstringPattern(s))
        s = "".join(chr(ord("a") + (i % 26)) for i in range(9999))
        self.assertFalse(self.sol.repeatedSubstringPattern(s))


if __name__ == "__main__":
    unittest.main()

# Tags: String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm
