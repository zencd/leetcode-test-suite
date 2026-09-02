# 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/
# Hard

import unittest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        raise Exception("Not solved yet")


class TestLongestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def call(self, s):
        return self.solution.longestValidParentheses(s)

    def test_empty_string(self):
        self.assertEqual(self.call(""), 0)

    def test_only_open_parenthesis(self):
        self.assertEqual(self.call("("), 0)

    def test_only_close_parenthesis(self):
        self.assertEqual(self.call(")"), 0)

    def test_single_pair(self):
        self.assertEqual(self.call("()"), 2)

    def test_nested_pair(self):
        self.assertEqual(self.call("(())"), 4)

    def test_consecutive_pairs(self):
        self.assertEqual(self.call("()()"), 4)

    def test_trailing_open(self):
        self.assertEqual(self.call("(()"), 2)

    def test_leading_close(self):
        self.assertEqual(self.call(")()"), 2)

    def test_leading_close_with_interior(self):
        self.assertEqual(self.call(")()())"), 4)

    def test_all_open(self):
        self.assertEqual(self.call("((("), 0)

    def test_all_close(self):
        self.assertEqual(self.call(")))"), 0)

    def test_mixed_invalid(self):
        self.assertEqual(self.call("())"), 2)

    def test_deeply_nested(self):
        s = "(" * 100 + ")" * 100
        self.assertEqual(self.call(s), 200)

    def test_deeply_nested_with_trailing(self):
        s = "(" * 100 + ")" * 100 + "(("
        self.assertEqual(self.call(s), 200)

    def test_deeply_nested_with_leading(self):
        s = ")))" + "(" * 100 + ")" * 100
        self.assertEqual(self.call(s), 200)

    def test_multiple_segments(self):
        self.assertEqual(self.call("())()()"), 4)

    def test_valid_then_nested(self):
        self.assertEqual(self.call("()((()))"), 8)

    def test_interleaved(self):
        self.assertEqual(self.call(")()())()("), 4)

    def test_alternating(self):
        self.assertEqual(self.call("()()()"), 6)

    def test_unclosed_in_middle(self):
        self.assertEqual(self.call("()())()"), 4)

    def test_unclosed_between_pairs(self):
        self.assertEqual(self.call("()(("), 2)

    def test_close_between_pairs(self):
        self.assertEqual(self.call("())()"), 2)

    def test_long_mixed(self):
        s = "(()())(())"
        self.assertEqual(self.call(s), 10)

    def test_larger_valid_run(self):
        s = "((()))(())()"
        self.assertEqual(self.call(s), 12)

    def test_performance_boundary_size(self):
        s = "(" * 15000 + ")" * 15000
        self.assertEqual(self.call(s), 30000)

    def test_performance_boundary_invalid(self):
        s = ")(" * 15000
        self.assertEqual(self.call(s), 29998)

    def test_performance_boundary_consecutive_pairs(self):
        s = "()" * 15000
        self.assertEqual(self.call(s), 30000)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming, Stack, Bracket Sequences
