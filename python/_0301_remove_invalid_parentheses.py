# 301. Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/
# Hard

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def call_s(self, s: str):
        return sorted(self.sol.removeInvalidParentheses(s))

    def test_example_1(self):
        self.assertEqual(self.call_s("()())()"), ["(())()", "()()()"])

    def test_example_2(self):
        self.assertEqual(self.call_s("(a)())()"), ["(a())()", "(a)()()"])

    def test_example_3(self):
        self.assertEqual(self.sol.removeInvalidParentheses(")("), [""])

    def test_empty_string(self):
        self.assertEqual(self.sol.removeInvalidParentheses(""), [""])

    def test_single_open(self):
        self.assertEqual(self.sol.removeInvalidParentheses("("), [""])

    def test_single_close(self):
        self.assertEqual(self.sol.removeInvalidParentheses(")"), [""])

    def test_single_pair(self):
        self.assertEqual(self.sol.removeInvalidParentheses("()"), ["()"])

    def test_nested_valid(self):
        self.assertEqual(self.sol.removeInvalidParentheses("(())"), ["(())"])

    def test_letters_only(self):
        self.assertEqual(self.sol.removeInvalidParentheses("abc"), ["abc"])

    def test_all_open(self):
        self.assertEqual(self.sol.removeInvalidParentheses("((("), [""])

    def test_all_close(self):
        self.assertEqual(self.sol.removeInvalidParentheses(")))"), [""])

    def test_valid_sequential(self):
        self.assertEqual(self.sol.removeInvalidParentheses("()()()"), ["()()()"])

    def test_letters_between_parens(self):
        self.assertEqual(self.call_s("a()b)()c"), ["a()b()c", "a(b)()c"])

    def test_excess_close_in_middle(self):
        self.assertEqual(self.call_s("())"), ["()"])

    def test_excess_open_in_middle(self):
        self.assertEqual(self.call_s("(()"), ["()"])

    def test_two_removes_required(self):
        self.assertEqual(self.call_s("((()"), ["()"])

    def test_two_removes_different_types(self):
        self.assertEqual(self.call_s(")()("), ["()"])

    def test_interleaved_dedup(self):
        self.assertEqual(self.call_s("())()("), ["()()"])

    def test_dedup_repeated_chars(self):
        r = self.sol.removeInvalidParentheses("))(")
        self.assertEqual(r, [""])
        self.assertEqual(len(r), 1)

    def test_result_is_valid_subsequence(self):
        for s in ["()())()", "(a)())()", ")", "(((", "a(b)c(d(e)f)"]:
            ans = self.sol.removeInvalidParentheses(s)
            for t in ans:

                def ok(x: str) -> bool:
                    b = 0
                    for c in x:
                        if c == "(":
                            b += 1
                        elif c == ")":
                            b -= 1
                            if b < 0:
                                return False
                    return b == 0

                self.assertTrue(ok(t), f"{t!r} from {s!r} is not valid")

    def test_minimum_removals_count(self):
        def invalid(t: str) -> int:
            bal = extra = 0
            for ch in t:
                if ch == "(":
                    bal += 1
                elif ch == ")" and bal:
                    bal -= 1
                elif ch == ")":
                    extra += 1
            return bal + extra

        for s in ["()())()", "(a)())()", "a(b)c(d(e)f)"]:
            ans = self.sol.removeInvalidParentheses(s)
            target = invalid(s)
            for t in ans:
                self.assertIsNotNone(t)
                self.assertGreaterEqual(len(s), len(t))
            for t in ans:
                self.assertEqual(
                    len(t), len(s) - target, f"{t!r} from {s!r} not minimal removal"
                )

    def test_with_many_letters(self):
        r = self.sol.removeInvalidParentheses("a" * 20 + "(")
        self.assertEqual(r, ["a" * 20])

    def test_no_duplicates_in_output(self):
        r = self.sol.removeInvalidParentheses("())()(")
        self.assertEqual(len(r), len(set(r)))


if __name__ == "__main__":
    unittest.main()

# Tags: String, Backtracking, Breadth-First Search
