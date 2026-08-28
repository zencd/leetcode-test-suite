# 67. Add Binary
# https://leetcode.com/problems/add-binary/
# Easy

import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        raise Exception("Not solved yet")


class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.addBinary("11", "1"), "100")
        self.assertEqual(self.sol.addBinary("1010", "1011"), "10101")

    def test_adding_zero(self):
        self.assertEqual(self.sol.addBinary("0", "0"), "0")
        self.assertEqual(self.sol.addBinary("0", "1"), "1")
        self.assertEqual(self.sol.addBinary("101", "0"), "101")

    def test_same_length(self):
        self.assertEqual(self.sol.addBinary("11", "11"), "110")
        self.assertEqual(self.sol.addBinary("1010", "1010"), "10100")

    def test_carry_chain(self):
        self.assertEqual(self.sol.addBinary("111", "1"), "1000")
        self.assertEqual(self.sol.addBinary("1111111", "1"), "10000000")

    def test_different_lengths(self):
        self.assertEqual(self.sol.addBinary("1", "11111"), "100000")
        self.assertEqual(self.sol.addBinary("100", "11"), "111")
        self.assertEqual(self.sol.addBinary("111", "1000"), "1111")

    def test_ones_only(self):
        self.assertEqual(self.sol.addBinary("1", "1"), "10")
        self.assertEqual(self.sol.addBinary("11", "1111"), "10010")

    def test_larger_values(self):
        self.assertEqual(self.sol.addBinary("1101", "1101"), "11010")
        self.assertEqual(self.sol.addBinary("10100", "111"), "11011")

    def test_consistency_with_int(self):
        cases = [
            ("1", "1"),
            ("101", "110"),
            ("1111111111", "1"),
            ("1000000000000000000000000000000", "1111111111111111111111111111111"),
            ("1" * 100, "1" * 100),
        ]
        for a, b in cases:
            expected = bin(int(a, 2) + int(b, 2))[2:]
            self.assertEqual(self.sol.addBinary(a, b), expected)

    def test_symmetry(self):
        self.assertEqual(
            self.sol.addBinary("101", "1101"), self.sol.addBinary("1101", "101")
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Bit Manipulation, Simulation
