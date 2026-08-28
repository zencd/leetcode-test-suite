# 299. Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/
# Medium

from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.getHint("1807", "7810"), "1A3B")

    def test_example2(self):
        self.assertEqual(self.sol.getHint("1123", "0111"), "1A1B")

    def test_all_bulls(self):
        self.assertEqual(self.sol.getHint("1234", "1234"), "4A0B")

    def test_no_match(self):
        self.assertEqual(self.sol.getHint("1234", "5678"), "0A0B")

    def test_all_cows(self):
        self.assertEqual(self.sol.getHint("1234", "2341"), "0A4B")

    def test_single_digit_same(self):
        self.assertEqual(self.sol.getHint("5", "5"), "1A0B")

    def test_single_digit_different(self):
        self.assertEqual(self.sol.getHint("5", "6"), "0A0B")

    def test_duplicate_digits_in_secret(self):
        self.assertEqual(self.sol.getHint("1111", "2222"), "0A0B")

    def test_duplicate_digits_all_same(self):
        self.assertEqual(self.sol.getHint("9087", "9087"), "4A0B")

    def test_duplicate_digits_reversed(self):
        self.assertEqual(self.sol.getHint("1122", "2211"), "0A4B")

    def test_duplicate_digits_partial(self):
        self.assertEqual(self.sol.getHint("1123", "1132"), "2A2B")

    def test_guess_has_extra_digit_not_in_secret(self):
        self.assertEqual(self.sol.getHint("12", "11"), "1A0B")

    def test_all_same_digit(self):
        self.assertEqual(self.sol.getHint("999999", "999999"), "6A0B")

    def test_all_same_digit_mismatch(self):
        self.assertEqual(self.sol.getHint("999999", "111111"), "0A0B")

    def test_all_same_digit_partial_bull(self):
        self.assertEqual(self.sol.getHint("999999", "199999"), "5A0B")

    def test_long_strings(self):
        secret = "1234567890" * 50
        guess = "0123456789" * 50
        self.assertEqual(self.sol.getHint(secret, guess), "0A500B")

    def test_long_strings_all_bulls(self):
        s = "9876543210" * 100
        self.assertEqual(self.sol.getHint(s, s), "1000A0B")

    def test_zero_single(self):
        self.assertEqual(self.sol.getHint("0", "0"), "1A0B")

    def test_zero_single_mismatch(self):
        self.assertEqual(self.sol.getHint("0", "1"), "0A0B")

    def test_zero_and_one_reversed(self):
        self.assertEqual(self.sol.getHint("10", "01"), "0A2B")

    def test_partial_bulls_only(self):
        self.assertEqual(self.sol.getHint("1234", "1256"), "2A0B")

    def test_full_reversal(self):
        self.assertEqual(self.sol.getHint("1234", "4321"), "0A4B")

    def test_duplicate_secret_with_other_digit_guess(self):
        self.assertEqual(self.sol.getHint("777777", "777776"), "5A0B")


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Counting
