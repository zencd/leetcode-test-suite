# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/
# Medium

import unittest


class Solution:
    def numDecodings(self, s: str) -> int:
        raise Exception("Not solved yet")


class TestNumDecodings(unittest.TestCase):
    def test_single_digit_one(self):
        self.assertEqual(Solution().numDecodings("1"), 1)

    def test_single_digit_zero(self):
        self.assertEqual(Solution().numDecodings("0"), 0)

    def test_single_digit_nine(self):
        self.assertEqual(Solution().numDecodings("9"), 1)

    def test_example_1(self):
        self.assertEqual(Solution().numDecodings("12"), 2)

    def test_example_2(self):
        self.assertEqual(Solution().numDecodings("226"), 3)

    def test_example_3(self):
        self.assertEqual(Solution().numDecodings("06"), 0)

    def test_leading_zero(self):
        self.assertEqual(Solution().numDecodings("01"), 0)

    def test_double_zero(self):
        self.assertEqual(Solution().numDecodings("00"), 0)

    def test_zero_in_middle(self):
        self.assertEqual(Solution().numDecodings("106"), 1)

    def test_example_11106(self):
        self.assertEqual(Solution().numDecodings("11106"), 2)

    def test_10(self):
        self.assertEqual(Solution().numDecodings("10"), 1)

    def test_11(self):
        self.assertEqual(Solution().numDecodings("11"), 2)

    def test_19(self):
        self.assertEqual(Solution().numDecodings("19"), 2)

    def test_20(self):
        self.assertEqual(Solution().numDecodings("20"), 1)

    def test_21(self):
        self.assertEqual(Solution().numDecodings("21"), 2)

    def test_25(self):
        self.assertEqual(Solution().numDecodings("25"), 2)

    def test_26(self):
        self.assertEqual(Solution().numDecodings("26"), 2)

    def test_27_invalid_pair(self):
        self.assertEqual(Solution().numDecodings("27"), 1)

    def test_28_invalid_pair(self):
        self.assertEqual(Solution().numDecodings("28"), 1)

    def test_29_invalid_pair(self):
        self.assertEqual(Solution().numDecodings("29"), 1)

    def test_30_invalid(self):
        self.assertEqual(Solution().numDecodings("30"), 0)

    def test_40_invalid(self):
        self.assertEqual(Solution().numDecodings("40"), 0)

    def test_90_invalid(self):
        self.assertEqual(Solution().numDecodings("90"), 0)

    def test_100(self):
        self.assertEqual(Solution().numDecodings("100"), 0)

    def test_101(self):
        self.assertEqual(Solution().numDecodings("101"), 1)

    def test_110(self):
        self.assertEqual(Solution().numDecodings("110"), 1)

    def test_111(self):
        self.assertEqual(Solution().numDecodings("111"), 3)

    def test_0010(self):
        self.assertEqual(Solution().numDecodings("0010"), 0)

    def test_1001(self):
        self.assertEqual(Solution().numDecodings("1001"), 0)

    def test_222(self):
        self.assertEqual(Solution().numDecodings("222"), 3)

    def test_22(self):
        self.assertEqual(Solution().numDecodings("22"), 2)

    def test_121(self):
        self.assertEqual(Solution().numDecodings("121"), 3)

    def test_1111(self):
        self.assertEqual(Solution().numDecodings("1111"), 5)

    def test_all_ones_length_5(self):
        self.assertEqual(Solution().numDecodings("1" * 5), 8)

    def test_all_twos_length_5(self):
        self.assertEqual(Solution().numDecodings("2" * 5), 8)

    def test_all_ones_length_10(self):
        self.assertEqual(Solution().numDecodings("1" * 10), 89)

    def test_all_twos_length_10(self):
        self.assertEqual(Solution().numDecodings("2" * 10), 89)

    def test_long_zero_streak(self):
        self.assertEqual(Solution().numDecodings("1000000"), 0)

    def test_alternating_10(self):
        self.assertEqual(Solution().numDecodings("1010101"), 1)

    def test_123(self):
        self.assertEqual(Solution().numDecodings("123"), 3)

    def test_1234(self):
        self.assertEqual(Solution().numDecodings("1234"), 3)

    def test_276(self):
        self.assertEqual(Solution().numDecodings("276"), 1)

    def test_227(self):
        self.assertEqual(Solution().numDecodings("227"), 2)

    def test_122(self):
        self.assertEqual(Solution().numDecodings("122"), 3)

    def test_125(self):
        self.assertEqual(Solution().numDecodings("125"), 3)

    def test_251(self):
        self.assertEqual(Solution().numDecodings("251"), 2)

    def test_250_invalid(self):
        self.assertEqual(Solution().numDecodings("250"), 0)

    def test_260_invalid(self):
        self.assertEqual(Solution().numDecodings("260"), 0)

    def test_105(self):
        self.assertEqual(Solution().numDecodings("105"), 1)

    def test_all_ones_length_20(self):
        self.assertEqual(Solution().numDecodings("1" * 20), 10946)

    def test_all_ones_length_30(self):
        self.assertEqual(Solution().numDecodings("1" * 30), 1346269)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming
