# 44. Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/
# Hard

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertFalse(self.sol.isMatch("aa", "a"))

    def test_example2(self):
        self.assertTrue(self.sol.isMatch("aa", "*"))

    def test_example3(self):
        self.assertFalse(self.sol.isMatch("cb", "?a"))

    def test_trailing_star(self):
        self.assertTrue(self.sol.isMatch("adceb", "*a*b"))

    def test_star_between(self):
        self.assertTrue(self.sol.isMatch("abc", "a*c"))

    def test_star_middle(self):
        self.assertTrue(self.sol.isMatch("abc", "a?c"))

    def test_question_marks(self):
        self.assertTrue(self.sol.isMatch("abc", "??c"))

    def test_question_marks_mismatch(self):
        self.assertFalse(self.sol.isMatch("abc", "??a"))

    def test_empty_pattern_nonempty_string(self):
        self.assertFalse(self.sol.isMatch("a", ""))

    def test_empty_string_empty_pattern(self):
        self.assertTrue(self.sol.isMatch("", ""))

    def test_empty_string_star_pattern(self):
        self.assertTrue(self.sol.isMatch("", "*"))

    def test_empty_string_question_pattern(self):
        self.assertFalse(self.sol.isMatch("", "?"))

    def test_multiple_stars(self):
        self.assertTrue(self.sol.isMatch("abc", "**a**c**"))

    def test_consecutive_stars(self):
        self.assertTrue(self.sol.isMatch("abcd", "****"))

    def test_star_anchored(self):
        self.assertTrue(self.sol.isMatch("hello", "h*o"))

    def test_star_anchored_mismatch(self):
        self.assertFalse(self.sol.isMatch("hello", "h*x"))

    def test_only_star(self):
        self.assertTrue(self.sol.isMatch("anything at all", "*"))

    def test_question_count_mismatch(self):
        self.assertTrue(self.sol.isMatch("a", "?"))
        self.assertFalse(self.sol.isMatch("a", "??"))

    def test_star_question_star(self):
        self.assertTrue(self.sol.isMatch("ab", "*?b"))
        self.assertFalse(self.sol.isMatch("ab", "*?c"))

    def test_prefix_star_mismatch(self):
        self.assertFalse(self.sol.isMatch("abc", "*d"))

    def test_char_then_star_char(self):
        self.assertTrue(self.sol.isMatch("abc", "a*bc"))
        self.assertFalse(self.sol.isMatch("abc", "a*z"))

    def test_exact_match(self):
        self.assertTrue(self.sol.isMatch("abcdef", "abcdef"))
        self.assertFalse(self.sol.isMatch("abcdef", "abcdf"))

    def test_star_matches_empty(self):
        self.assertTrue(self.sol.isMatch("ac", "a*c"))

    def test_star_matches_long(self):
        self.assertTrue(self.sol.isMatch("a" * 100 + "b", "a*b"))

    def test_complex(self):
        self.assertFalse(self.sol.isMatch("aaabbabbababb", "?aa?bb*a*bb*b?"))

    def test_long_strings(self):
        s = "a" * 1000
        p = "a" * 1000
        self.assertTrue(self.sol.isMatch(s, p))
        s = "a" * 1000
        p = "a" * 999
        self.assertFalse(self.sol.isMatch(s, p))

    def test_all_questions(self):
        self.assertTrue(self.sol.isMatch("xyz", "???"))
        self.assertFalse(self.sol.isMatch("xyz", "??"))
        self.assertFalse(self.sol.isMatch("xy", "???"))

    def test_star_repetition_case(self):
        self.assertTrue(self.sol.isMatch("aa", "a*"))
        self.assertFalse(self.sol.isMatch("", "a*"))
        self.assertFalse(self.sol.isMatch("ddaig", "*ag"))
        self.assertTrue(self.sol.isMatch("ddag", "*ag"))


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming, Greedy, Recursion
