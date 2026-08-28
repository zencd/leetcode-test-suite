# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/
# Medium

class Solution:
    def calculate(self, s: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.calculate("3+2*2"), 7)

    def test_example_2(self):
        self.assertEqual(self.sol.calculate(" 3/2 "), 1)

    def test_example_3(self):
        self.assertEqual(self.sol.calculate(" 3+5 / 2 "), 5)

    def test_single_number(self):
        self.assertEqual(self.sol.calculate("5"), 5)

    def test_zero(self):
        self.assertEqual(self.sol.calculate("0"), 0)

    def test_simple_addition(self):
        self.assertEqual(self.sol.calculate("1+2"), 3)

    def test_simple_subtraction(self):
        self.assertEqual(self.sol.calculate("5-3"), 2)

    def test_simple_multiplication(self):
        self.assertEqual(self.sol.calculate("2*3"), 6)

    def test_simple_division(self):
        self.assertEqual(self.sol.calculate("10/2"), 5)

    def test_division_truncation(self):
        self.assertEqual(self.sol.calculate("7/2"), 3)

    def test_precedence_add_before_mul(self):
        self.assertEqual(self.sol.calculate("2+3*4"), 14)

    def test_precedence_mul_before_div(self):
        self.assertEqual(self.sol.calculate("6/2*3"), 9)

    def test_left_associativity_division(self):
        self.assertEqual(self.sol.calculate("9/3/3"), 1)

    def test_mixed_operators(self):
        self.assertEqual(self.sol.calculate("1+2*3-4/2"), 5)

    def test_subtraction_chain(self):
        self.assertEqual(self.sol.calculate("10-2-3"), 5)

    def test_negative_intermediate_result(self):
        self.assertEqual(self.sol.calculate("2-10"), -8)

    def test_negative_times_positive(self):
        self.assertEqual(self.sol.calculate("2-3*4"), -10)

    def test_negative_times_negative(self):
        self.assertEqual(self.sol.calculate("2-3*3"), -7)

    def test_division_of_negative_intermediate(self):
        self.assertEqual(self.sol.calculate("5-8/2"), 1)

    def test_division_truncation_toward_zero(self):
        self.assertEqual(self.sol.calculate("3-10/4"), 1)

    def test_division_precedence_with_subtraction(self):
        self.assertEqual(self.sol.calculate("2-6/2"), -1)

    def test_division_of_negative_by_positive(self):
        self.assertEqual(self.sol.calculate("1-7/2"), -2)

    def test_multiply_by_zero(self):
        self.assertEqual(self.sol.calculate("100*0+5"), 5)

    def test_division_by_single_digit_in_long_context(self):
        self.assertEqual(self.sol.calculate("1000000000/1"), 1000000000)

    def test_large_numbers(self):
        self.assertEqual(self.sol.calculate("2147483647/1"), 2147483647)

    def test_many_spaces(self):
        self.assertEqual(self.sol.calculate("  1  +  2  "), 3)

    def test_leading_zero_number(self):
        self.assertEqual(self.sol.calculate("007+1"), 8)

    def test_multidigit_operands(self):
        self.assertEqual(self.sol.calculate("12+34*5"), 182)

    def test_all_addition(self):
        self.assertEqual(self.sol.calculate("1+2+3+4+5"), 15)

    def test_long_expression(self):
        self.assertEqual(self.sol.calculate("1+2*3+4*5-6/2"), 24)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Stack
