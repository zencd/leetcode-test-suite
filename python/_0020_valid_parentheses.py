# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Easy

class Solution:
    def isValid(self, s: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_string(self):
        self.assertTrue(self.sol.isValid(""))

    def test_simple_pairs(self):
        self.assertTrue(self.sol.isValid("()"))
        self.assertTrue(self.sol.isValid("[]"))
        self.assertTrue(self.sol.isValid("{}"))

    def test_multiple_pairs(self):
        self.assertTrue(self.sol.isValid("()[]{}"))
        self.assertTrue(self.sol.isValid("()()"))
        self.assertTrue(self.sol.isValid("{}{}{}"))

    def test_nested(self):
        self.assertTrue(self.sol.isValid("([])"))
        self.assertTrue(self.sol.isValid("({[]})"))
        self.assertTrue(self.sol.isValid("[{()}]"))
        self.assertTrue(self.sol.isValid("((()))"))
        deep = "(" * 20 + ")" * 20
        self.assertTrue(self.sol.isValid(deep))

    def test_unmatched_types(self):
        self.assertFalse(self.sol.isValid("(]"))
        self.assertFalse(self.sol.isValid("([)]"))
        self.assertFalse(self.sol.isValid("{]"))
        self.assertFalse(self.sol.isValid("([}])"))
        self.assertFalse(self.sol.isValid("([]){"))

    def test_unclosed(self):
        self.assertFalse(self.sol.isValid("("))
        self.assertFalse(self.sol.isValid("(()"))
        self.assertFalse(self.sol.isValid("((()))("))
        self.assertFalse(self.sol.isValid("((()))[("))
        self.assertFalse(self.sol.isValid("}("))

    def test_unopened(self):
        self.assertFalse(self.sol.isValid(")"))
        self.assertFalse(self.sol.isValid("())"))
        self.assertFalse(self.sol.isValid(")()"))
        self.assertFalse(self.sol.isValid("]["))
        self.assertFalse(self.sol.isValid("]"))
        self.assertFalse(self.sol.isValid("}"))

    def test_wrong_order(self):
        self.assertFalse(self.sol.isValid("([{])"))
        self.assertFalse(self.sol.isValid("[(]){]"))

    def test_long_valid(self):
        s = "()" * 5000
        self.assertTrue(self.sol.isValid(s))

    def test_long_invalid(self):
        s = "(" * 5000 + ")" * 4999
        self.assertFalse(self.sol.isValid(s))


if __name__ == "__main__":
    unittest.main()

# Tags: String, Stack, Bracket Sequences
