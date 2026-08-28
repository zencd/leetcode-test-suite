# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/
# Hard

import unittest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        raise Exception("Not solved yet")


class TestRegularExpressionMatching(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def _check(self, s, p, expected):
        self.assertEqual(self.sol.isMatch(s, p), expected)

    def test_example1(self):
        self._check("aa", "a", False)

    def test_example2(self):
        self._check("aa", "a*", True)

    def test_example3(self):
        self._check("ab", ".*", True)

    def test_star_zero_occurrences(self):
        self._check("", "a*", True)
        self._check("b", "a*b", True)

    def test_star_one_or_more(self):
        self._check("aaa", "a*", True)
        self._check("aaa", "aa*", True)

    def test_dot_any_char(self):
        self._check("ac", "a.", True)
        self._check("bcd", "a.c", False)
        self._check("bc", "a.c", False)
        self._check("z", ".", True)
        self._check("az", ".", False)

    def test_dot_star(self):
        self._check("", ".*", True)
        self._check("abc", ".*", True)
        self._check("anything", ".*", True)

    def test_star_after_dot(self):
        self._check("abbbc", "a.*c", True)
        self._check("ac", "a.*c", True)
        self._check("abbbc", "a.*z", False)

    def test_multiple_stars(self):
        self._check("aab", "c*a*b", True)
        self._check("b", "c*b", True)
        self._check("ab", "c*a*b", True)

    def test_mismatch(self):
        self._check("a", "ab", False)
        self._check("ab", "a", False)
        self._check("a", "b", False)
        self._check("abc", "a*c", False)
        self._check("abab", "ab*", False)

    def test_star_does_not_skip(self):
        self._check("abbbcd", "a*b*c", False)
        self._check("abbbc", "a*b*c", True)

    def test_repeated_star_patterns(self):
        self._check("aaa", "a*a*a", True)
        self._check("a", "a*a*a*a*a*", True)
        self._check("b", "a*a*a*a*a*b", True)
        self._check("ab", "a*a*a*a*a*b", True)
        self._check("acb", "a*a*a*a*a*b", False)

    def test_consecutive_dot_star(self):
        self._check("abc", ".*.*", True)
        self._check("", ".*.*", True)

    def test_pattern_ends_with_star(self):
        self._check("aaaa", "a*", True)
        self._check("aaab", "a*b", True)
        self._check("baab", "a*b", False)

    def test_alternation_like(self):
        self._check("ab", "a*b*", True)
        self._check("aab", "a*b*", True)
        self._check("bbb", "a*b*", True)
        self._check("abab", "a*b*", False)

    def test_single_char(self):
        self._check("a", "a", True)
        self._check("a", "b", False)
        self._check("a", ".", True)
        self._check("ab", "a*", False)

    def test_longer_sequences(self):
        self._check("abcabc", "a.*c.*c", True)
        self._check("abcabc", "a.*c.*d", False)
        self._check("cbabcbbc", ".*cbbc", True)
        self._check("cbabcbbc", ".*cbbc.*", True)
        self._check("aaaabbbbaaaabbbab", "a*b*a*b*a*b", True)
        self._check("mississippi", "mis*is*ip*.", True)

    def test_star_repeating_mixed(self):
        self._check("ababbbab", "a*b*b*a*b*", False)
        self._check("ababbbab", "a*b*b*a*c*", False)

    def test_greedy_backtracking(self):
        self._check("aaab", "a*a*a*a*a*a*a*a*a*a*a*b", True)
        self._check("aaac", "a*a*a*a*a*a*a*a*a*a*a*b", False)

    def test_only_star_chars(self):
        self._check("", "a*a*a*", True)
        self._check("aaa", "a*a*", True)

    def test_mixed_dot_star_and_literals(self):
        self._check("xyzz", ".*zz", True)
        self._check("xyzz", ".*zz.*", True)
        self._check("xyzz", ".*yy", False)
        self._check("abc", "b.*", False)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming, Recursion
