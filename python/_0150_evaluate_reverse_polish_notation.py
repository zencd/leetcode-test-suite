# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Medium

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def evaluate(self, tokens):
        return self.sol.evalRPN(tokens)

    def test_single_number(self):
        self.assertEqual(self.evaluate(["42"]), 42)

    def test_single_negative_number(self):
        self.assertEqual(self.evaluate(["-200"]), -200)

    def test_single_zero(self):
        self.assertEqual(self.evaluate(["0"]), 0)

    def test_addition(self):
        self.assertEqual(self.evaluate(["2", "3", "+"]), 5)

    def test_subtraction(self):
        self.assertEqual(self.evaluate(["5", "2", "-"]), 3)

    def test_multiplication(self):
        self.assertEqual(self.evaluate(["3", "4", "*"]), 12)

    def test_division(self):
        self.assertEqual(self.evaluate(["10", "2", "/"]), 5)

    def test_division_truncates_toward_zero_positive(self):
        self.assertEqual(self.evaluate(["13", "5", "/"]), 2)

    def test_division_truncates_toward_zero_negative(self):
        self.assertEqual(self.evaluate(["6", "-3", "/"]), -2)

    def test_division_by_larger_number_gives_zero(self):
        self.assertEqual(self.evaluate(["2", "-3", "/"]), 0)

    def test_division_negative_into_positive(self):
        self.assertEqual(self.evaluate(["7", "2", "/"]), 3)

    def test_division_result_negative_with_remainder(self):
        self.assertEqual(self.evaluate(["-7", "2", "/"]), -3)

    def test_division_result_positive_with_remainder(self):
        self.assertEqual(self.evaluate(["7", "-2", "/"]), -3)

    def test_negative_operands_addition(self):
        self.assertEqual(self.evaluate(["-1", "-1", "+"]), -2)

    def test_negative_operands_subtraction(self):
        self.assertEqual(self.evaluate(["-1", "-1", "-"]), 0)

    def test_negative_operands_multiplication(self):
        self.assertEqual(self.evaluate(["-2", "-3", "*"]), 6)

    def test_negative_multiplication(self):
        self.assertEqual(self.evaluate(["-2", "3", "*"]), -6)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.evaluate(["999", "0", "*"]), 0)

    def test_addition_with_negative_result(self):
        self.assertEqual(self.evaluate(["5", "-10", "+"]), -5)

    def test_subtraction_to_negative(self):
        self.assertEqual(self.evaluate(["-1", "5", "-"]), -6)

    def test_example_1(self):
        self.assertEqual(self.evaluate(["2", "1", "+", "3", "*"]), 9)

    def test_example_2(self):
        self.assertEqual(self.evaluate(["4", "13", "5", "/", "+"]), 6)

    def test_example_3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(self.evaluate(tokens), 22)

    def test_nested_all_operators(self):
        self.assertEqual(self.evaluate(["2", "3", "+", "4", "5", "+", "*"]), 45)

    def test_chained_additions(self):
        self.assertEqual(self.evaluate(["1", "2", "+", "3", "+", "4", "+"]), 10)

    def test_chained_subtractions(self):
        self.assertEqual(self.evaluate(["10", "3", "-", "2", "-", "1", "-"]), 4)

    def test_chained_multiplications(self):
        self.assertEqual(self.evaluate(["2", "3", "*", "4", "*"]), 24)

    def test_chained_divisions(self):
        self.assertEqual(self.evaluate(["8", "2", "/", "2", "/"]), 2)

    def test_mixed_operators_order(self):
        self.assertEqual(
            self.evaluate(["1", "2", "*", "3", "+", "4", "*", "5", "-"]), 15
        )

    def test_zero_subtracted(self):
        self.assertEqual(self.evaluate(["0", "0", "-"]), 0)

    def test_zero_divided(self):
        self.assertEqual(self.evaluate(["0", "5", "/"]), 0)

    def test_operands_at_limits(self):
        self.assertEqual(self.evaluate(["200", "200", "*"]), 40000)

    def test_subtract_limits_to_negative(self):
        self.assertEqual(self.evaluate(["-200", "-200", "-"]), 0)

    def test_expression_using_subexpression_results(self):
        self.assertEqual(self.evaluate(["2", "3", "*", "4", "5", "*", "+"]), 26)

    def test_deeply_nested(self):
        tokens = ["1", "2", "+"]
        for i in range(3, 12):
            tokens += [str(i), "+"]
        self.assertEqual(self.evaluate(tokens), sum(range(1, 12)))

    def test_intermediate_division_zero_times(self):
        self.assertEqual(self.evaluate(["5", "8", "/", "100", "*"]), 0)

    def test_division_chain_truncation(self):
        self.assertEqual(self.evaluate(["17", "5", "/", "2", "/"]), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Stack
