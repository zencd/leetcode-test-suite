# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Medium

from typing import List
import unittest


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        raise Exception("Not solved yet")


class TestGenerateParenthesis(unittest.TestCase):
    def test_n_1(self):
        self.assertEqual(Solution().generateParenthesis(1), ["()"])

    def test_n_2(self):
        self.assertEqual(
            sorted(Solution().generateParenthesis(2)),
            ["(())", "()()"],
        )

    def test_n_3(self):
        self.assertEqual(
            sorted(Solution().generateParenthesis(3)),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )

    def test_n_4_expected_count(self):
        self.assertEqual(len(Solution().generateParenthesis(4)), 14)

    def test_n_8_expected_count(self):
        self.assertEqual(len(Solution().generateParenthesis(8)), 1430)

    def test_result_type(self):
        result = Solution().generateParenthesis(3)
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, str)

    def test_unique_results(self):
        result = Solution().generateParenthesis(5)
        self.assertEqual(len(result), len(set(result)))

    def test_all_well_formed(self):
        for n in range(1, 8):
            for s in Solution().generateParenthesis(n):
                balance = 0
                for ch in s:
                    balance += 1 if ch == "(" else -1
                    self.assertGreaterEqual(balance, 0, f"invalid string {s}")
                self.assertEqual(balance, 0, f"unbalanced string {s}")
                self.assertEqual(len(s), 2 * n)

    def test_catalan_count(self):
        for n in range(1, 7):
            binom = 1
            for i in range(1, n + 1):
                binom = binom * (2 * n - i + 1) // i
            catalan = binom // (n + 1)
            self.assertEqual(len(Solution().generateParenthesis(n)), catalan)

    def test_expected_first_element_for_n3(self):
        self.assertIn("((()))", Solution().generateParenthesis(3))


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming, Backtracking, Bracket Sequences
