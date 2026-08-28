# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/
# Easy

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        raise Exception("Not solved yet")


import unittest


def reference_convert(n: int) -> str:
    letters = []
    while n > 0:
        n, r = divmod(n - 1, 26)
        letters.append(chr(ord("A") + r))
    return "".join(reversed(letters))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_letters(self):
        self.assertEqual(self.sol.convertToTitle(1), "A")
        self.assertEqual(self.sol.convertToTitle(2), "B")
        self.assertEqual(self.sol.convertToTitle(3), "C")
        self.assertEqual(self.sol.convertToTitle(13), "M")
        self.assertEqual(self.sol.convertToTitle(14), "N")
        self.assertEqual(self.sol.convertToTitle(25), "Y")
        self.assertEqual(self.sol.convertToTitle(26), "Z")

    def test_two_letter_boundaries(self):
        self.assertEqual(self.sol.convertToTitle(27), "AA")
        self.assertEqual(self.sol.convertToTitle(28), "AB")
        self.assertEqual(self.sol.convertToTitle(29), "AC")
        self.assertEqual(self.sol.convertToTitle(51), "AY")
        self.assertEqual(self.sol.convertToTitle(52), "AZ")
        self.assertEqual(self.sol.convertToTitle(53), "BA")
        self.assertEqual(self.sol.convertToTitle(54), "BB")
        self.assertEqual(self.sol.convertToTitle(676), "YZ")
        self.assertEqual(self.sol.convertToTitle(677), "ZA")
        self.assertEqual(self.sol.convertToTitle(700), "ZX")
        self.assertEqual(self.sol.convertToTitle(701), "ZY")
        self.assertEqual(self.sol.convertToTitle(702), "ZZ")
        self.assertEqual(self.sol.convertToTitle(703), "AAA")

    def test_three_letter_boundaries(self):
        self.assertEqual(self.sol.convertToTitle(18278), "ZZZ")
        self.assertEqual(self.sol.convertToTitle(18279), "AAAA")
        self.assertEqual(self.sol.convertToTitle(18280), "AAAB")
        self.assertEqual(self.sol.convertToTitle(999), "ALK")
        self.assertEqual(self.sol.convertToTitle(2147), "CDO")
        self.assertEqual(self.sol.convertToTitle(3000), "DKJ")
        self.assertEqual(self.sol.convertToTitle(2028), "BYZ")
        self.assertEqual(self.sol.convertToTitle(2029), "BZA")
        self.assertEqual(self.sol.convertToTitle(1352), "AYZ")

    def test_large_numbers(self):
        self.assertEqual(self.sol.convertToTitle(16384), "XFD")
        self.assertEqual(self.sol.convertToTitle(46960), "BQLD")
        self.assertEqual(self.sol.convertToTitle(2**31 - 1), "FXSHRXW")
        self.assertEqual(self.sol.convertToTitle(2**31 - 2), "FXSHRXV")
        self.assertEqual(self.sol.convertToTitle(100000), "EQXD")

    def test_known_examples(self):
        self.assertEqual(self.sol.convertToTitle(1), "A")
        self.assertEqual(self.sol.convertToTitle(28), "AB")
        self.assertEqual(self.sol.convertToTitle(701), "ZY")

    def test_matches_reference_up_to_2000(self):
        for n in range(1, 2001):
            with self.subTest(n=n):
                self.assertEqual(self.sol.convertToTitle(n), reference_convert(n))

    def test_matches_reference_large_samples(self):
        samples = [
            1,
            999,
            702,
            703,
            20000,
            18278,
            18279,
            100000,
            1000000,
            999999,
            123456789,
            2**31 - 1,
        ]
        for n in samples:
            with self.subTest(n=n):
                self.assertEqual(self.sol.convertToTitle(n), reference_convert(n))


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String
