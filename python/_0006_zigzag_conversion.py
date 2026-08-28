# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# Medium

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        raise Exception("Not solved yet")


import unittest


class TestZigzagConversion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_paypal_3_rows(self):
        self.assertEqual(self.solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_paypal_4_rows(self):
        self.assertEqual(self.solution.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_single_char(self):
        self.assertEqual(self.solution.convert("A", 1), "A")

    def test_single_row(self):
        self.assertEqual(self.solution.convert("ABCDEFG", 1), "ABCDEFG")

    def test_rows_greater_than_length(self):
        self.assertEqual(self.solution.convert("ABC", 5), "ABC")

    def test_rows_equal_to_length(self):
        self.assertEqual(self.solution.convert("ABCD", 4), "ABCD")

    def test_two_rows(self):
        self.assertEqual(self.solution.convert("ABCDEF", 2), "ACEBDF")

    def test_lowercase(self):
        self.assertEqual(self.solution.convert("abcd", 3), "abdc")

    def test_with_commas_and_dots(self):
        self.assertEqual(self.solution.convert("a,b,c,d", 3), "ac,,,bd")

    def test_all_same_chars(self):
        self.assertEqual(self.solution.convert("AAAA", 3), "AAAA")

    def test_two_chars_two_rows(self):
        self.assertEqual(self.solution.convert("AB", 2), "AB")

    def test_three_chars_two_rows(self):
        self.assertEqual(self.solution.convert("ABC", 2), "ACB")

    def test_four_chars_three_rows(self):
        self.assertEqual(self.solution.convert("ABCD", 3), "ABDC")

    def test_periodic_cycle(self):
        self.assertEqual(self.solution.convert("ABCDEFGHIJ", 3), "AEIBDFHJCG")

    def test_long_string_3_rows(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.solution.convert(s, 3), "aeimquybdfhjlnprtvxzcgkosw")

    def test_long_string_4_rows(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.solution.convert(s, 4), "agmsybfhlnrtxzceikoquwdjpv")


if __name__ == "__main__":
    unittest.main()

# Tags: String
