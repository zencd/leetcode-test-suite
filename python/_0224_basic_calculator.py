# 224. Basic Calculator
# https://leetcode.com/problems/basic-calculator/
# Hard

class Solution:
    def calculate(self, s: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_number(self):
        self.assertEqual(self.sol.calculate("7"), 7)

    def test_single_big_number(self):
        self.assertEqual(self.sol.calculate("2147483647"), 2147483647)

    def test_example1(self):
        self.assertEqual(self.sol.calculate("1 + 1"), 2)

    def test_example2(self):
        self.assertEqual(self.sol.calculate(" 2-1 + 2 "), 3)

    def test_example3(self):
        self.assertEqual(self.sol.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_simple_subtraction(self):
        self.assertEqual(self.sol.calculate("1-2"), -1)

    def test_negative_result(self):
        self.assertEqual(self.sol.calculate("1 - 5"), -4)

    def test_multi_digit_terms(self):
        self.assertEqual(self.sol.calculate("10 + 20 + 30"), 60)

    def test_no_spaces(self):
        self.assertEqual(self.sol.calculate("2+3-4"), 1)

    def test_excess_spaces(self):
        self.assertEqual(self.sol.calculate(" 1   +   1 "), 2)

    def test_unary_minus_start(self):
        self.assertEqual(self.sol.calculate("-1"), -1)

    def test_unary_minus_parens(self):
        self.assertEqual(self.sol.calculate("-(2 + 3)"), -5)

    def test_unary_inside_parens(self):
        self.assertEqual(self.sol.calculate("(-1)"), -1)

    def test_unary_parenthesized_parens(self):
        self.assertEqual(self.sol.calculate("-(-1)"), 1)

    def test_triple_unary(self):
        self.assertEqual(self.sol.calculate("-(-(-1))"), -1)

    def test_unary_multi_digit(self):
        self.assertEqual(self.sol.calculate("-(12+3)"), -15)

    def test_unary_after_operator(self):
        self.assertEqual(self.sol.calculate("1+(-2)"), -1)

    def test_deeply_nested_same_value(self):
        self.assertEqual(self.sol.calculate("((((1))))"), 1)

    def test_deeply_nested_arithmetic(self):
        self.assertEqual(self.sol.calculate("((1+2))+((3+4))-3"), 7)

    def test_parens_wrap_all(self):
        self.assertEqual(self.sol.calculate("((1))"), 1)

    def test_chained_subtractions(self):
        self.assertEqual(self.sol.calculate("10-2-3"), 5)

    def test_inner_parens_between_terms(self):
        self.assertEqual(self.sol.calculate("2-(3)+(4)"), 3)

    def test_mixed_nested(self):
        self.assertEqual(self.sol.calculate("1+2-(3+4-(5+6))"), 7)

    def test_result_negative_deep(self):
        self.assertEqual(self.sol.calculate("-(1-2)"), 1)

    def test_zero(self):
        self.assertEqual(self.sol.calculate("0"), 0)

    def test_zero_arithmetic(self):
        self.assertEqual(self.sol.calculate("0+0-(0)"), 0)

    def test_sign_flips_in_sequence(self):
        self.assertEqual(self.sol.calculate("5-(3-1)"), 3)

    def test_long_expression(self):
        s = "0"
        for i in range(1, 1000):
            s += f"+{i}" if i % 2 == 1 else f"-{i}"
        expected = sum(i for i in range(1, 1000, 2)) - sum(i for i in range(2, 1000, 2))
        self.assertEqual(self.sol.calculate(s), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Stack, Recursion
