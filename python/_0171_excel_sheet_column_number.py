# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/
# Easy

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_letter_basic(self):
        self.assertEqual(self.solution.titleToNumber("A"), 1)
        self.assertEqual(self.solution.titleToNumber("B"), 2)
        self.assertEqual(self.solution.titleToNumber("C"), 3)
        self.assertEqual(self.solution.titleToNumber("Z"), 26)

    def test_examples(self):
        self.assertEqual(self.solution.titleToNumber("AB"), 28)
        self.assertEqual(self.solution.titleToNumber("ZY"), 701)

    def test_boundary_transitions(self):
        self.assertEqual(self.solution.titleToNumber("AA"), 27)
        self.assertEqual(self.solution.titleToNumber("AZ"), 52)
        self.assertEqual(self.solution.titleToNumber("BA"), 53)
        self.assertEqual(self.solution.titleToNumber("ZZ"), 702)
        self.assertEqual(self.solution.titleToNumber("AAA"), 703)

    def test_three_letters(self):
        self.assertEqual(self.solution.titleToNumber("ABC"), 731)
        self.assertEqual(self.solution.titleToNumber("ZZZ"), 18278)

    def test_max_constraint(self):
        self.assertEqual(self.solution.titleToNumber("FXSHRXW"), 2147483647)

    def test_max_len_max_chars(self):
        expected = sum(26**i for i in range(1, 8))
        self.assertEqual(self.solution.titleToNumber("ZZZZZZZ"), expected)

    def test_mixed_letters(self):
        self.assertEqual(self.solution.titleToNumber("AD"), 30)
        self.assertEqual(self.solution.titleToNumber("CZ"), 104)
        self.assertEqual(self.solution.titleToNumber("XKCD"), 429342)

    def test_all_singles(self):
        for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            self.assertEqual(self.solution.titleToNumber(ch), i + 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String
