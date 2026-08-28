# 282. Expression Add Operators
# https://leetcode.com/problems/expression-add-operators/
# Hard

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        raise Exception("Not solved yet")


import ast
import unittest


def _eval_expr(expr: str) -> int:
    assert set(expr) <= set("0123456789+-*")
    node = ast.parse(expr, mode="eval").body
    allowed_asts = (ast.Expression, ast.BinOp, ast.Constant, ast.Add, ast.Sub, ast.Mult)
    for sub in ast.walk(node):
        assert type(sub) in allowed_asts, f"unexpected node {type(sub)}"
        if isinstance(sub, ast.Constant):
            assert isinstance(sub.value, int), "only integers allowed"
            assert sub.value >= 0, "only non-negative integers allowed"
    return eval(
        compile(ast.Expression(body=node), "<expr>", "eval"), {"__builtins__": {}}, {}
    )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assertSolutions(self, num: str, target: int, expected: set):
        got = self.sol.addOperators(num, target)
        self.assertEqual(set(got), expected)
        for expr in got:
            self.assertEqual(_eval_expr(expr), target)
            self.assertTrue(self._no_leading_zero(expr), msg=expr)

    @staticmethod
    def _no_leading_zero(expr: str) -> bool:
        ops = {"+", "-", "*"}
        for token in "".join(c if c in ops else " " for c in expr).split():
            if len(token) > 1 and token[0] == "0":
                return False
        return True

    def test_example_1(self):
        self.assertSolutions("123", 6, {"1*2*3", "1+2+3"})

    def test_example_2(self):
        self.assertSolutions("232", 8, {"2*3+2", "2+3*2"})

    def test_example_3_no_solution(self):
        self.assertSolutions("3456237490", 9191, set())

    def test_single_digit_match(self):
        self.assertSolutions("0", 0, {"0"})

    def test_single_digit_no_match(self):
        self.assertSolutions("0", 1, set())

    def test_single_digit_match_5(self):
        self.assertSolutions("5", 5, {"5"})

    def test_single_digit_negative_target(self):
        self.assertSolutions("1", -1, set())

    def test_zero_handling(self):
        self.assertSolutions("00", 0, {"0+0", "0-0", "0*0"})

    def test_zero_handling_no_match(self):
        self.assertSolutions("00", 2, set())

    def test_zero_interior(self):
        self.assertSolutions("005", 5, {"0+0+5", "0-0+5", "0*0+5"})

    def test_leading_zero_rejected(self):
        self.assertSolutions("105", 2, set())

    def test_leading_zero_interior_valid(self):
        self.assertSolutions("01", 1, {"0+1"})

    def test_mixed_operators_105(self):
        self.assertSolutions("105", 5, {"1*0+5", "10-5"})

    def test_multi_digit_operand(self):
        self.assertSolutions("999", 999, {"999"})

    def test_multiplication_chain(self):
        self.assertSolutions("125", 10, {"1*2*5"})

    def test_negative_result_expression(self):
        self.assertSolutions("123", 0, {"1+2-3"})

    def test_negative_target(self):
        self.assertSolutions("23", -1, {"2-3"})

    def test_precedence_multiplication(self):
        self.assertSolutions("123", 7, {"1+2*3"})

    def test_no_solution_53(self):
        self.assertSolutions("53", 0, set())

    def test_large_target(self):
        self.assertSolutions("12", 2147483647, set())

    def test_min_target(self):
        self.assertSolutions("12", -2147483648, set())

    def test_returns_list(self):
        self.assertIsInstance(self.sol.addOperators("123", 6), list)

    def test_deterministic_order(self):
        first = self.sol.addOperators("123", 6)
        second = self.sol.addOperators("123", 6)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Backtracking
