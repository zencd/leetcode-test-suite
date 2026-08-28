# 306. Additive Number
# https://leetcode.com/problems/additive-number/
# Medium

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        raise Exception("Not solved yet")

    @staticmethod
    def _str_add(a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        out = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(a[i]) - 48
                i -= 1
            if j >= 0:
                total += ord(b[j]) - 48
                j -= 1
            out.append(chr(48 + total % 10))
            carry = total // 10
        return "".join(reversed(out))


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def check(self, num: str, expected: bool):
        self.assertEqual(self.sol.isAdditiveNumber(num), expected, f"num={num!r}")

    def test_example1_positive(self):
        self.check("112358", True)

    def test_example2_positive(self):
        self.check("199100199", True)

    def test_basic_positive(self):
        self.check("123", True)
        self.check("1235", True)
        self.check("112", True)
        self.check("1123", True)
        self.check("1011", True)
        self.check("101", True)
        self.check("12132538", True)
        self.check("11235813", True)
        self.check("199100", True)
        self.check("19899", True)

    def test_basic_negative(self):
        self.check("1234", False)
        self.check("124", False)
        self.check("1111", False)
        self.check("1122", False)
        self.check("112345", False)
        self.check("1124", False)
        self.check("112235", False)
        self.check("121324", False)
        self.check("19898", False)
        self.check("123456789", False)

    def test_too_short(self):
        self.check("", False)
        self.check("1", False)
        self.check("12", False)

    def test_leading_zeros_invalid(self):
        self.check("1000", False)
        self.check("0110", False)
        self.check("0111", False)
        self.check("1022", False)
        self.check("0101", False)
        self.check("100100", False)
        self.check("0001", False)

    def test_leading_zero_single_digit_allowed(self):
        self.check("000", True)
        self.check("0000", True)
        self.check("000000", True)

    def test_large_numbers_positive(self):
        a = "12345678901234567890"
        s = "12345678901234567899"
        self.assertEqual(str(int(a) + 9), s)
        self.check(a + "9" + s, True)

    def test_large_numbers_invalid(self):
        a = "1" * 20
        b = "2" * 20
        self.check(a + b + "4" * 21, False)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Backtracking
