# 93. Restore IP Addresses
# https://leetcode.com/problems/restore-ip-addresses/
# Medium

import unittest
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        raise Exception("Not solved yet")


def _valid(ip: str) -> bool:
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p or not p.isdigit():
            return False
        if len(p) > 1 and p[0] == "0":
            return False
        if int(p) > 255:
            return False
    return True


def _digits_only(s: str) -> bool:
    return s.isdigit()


class TestRestoreIpAddresses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(
            sorted(self.sol.restoreIpAddresses("25525511135")),
            sorted(["255.255.11.135", "255.255.111.35"]),
        )

    def test_example_2(self):
        self.assertEqual(self.sol.restoreIpAddresses("0000"), ["0.0.0.0"])

    def test_example_3(self):
        self.assertEqual(
            sorted(self.sol.restoreIpAddresses("101023")),
            sorted(["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
        )

    def test_too_short(self):
        self.assertEqual(self.sol.restoreIpAddresses("1"), [])
        self.assertEqual(self.sol.restoreIpAddresses("12"), [])
        self.assertEqual(self.sol.restoreIpAddresses("123"), [])

    def test_four_digits(self):
        self.assertEqual(self.sol.restoreIpAddresses("1234"), ["1.2.3.4"])
        self.assertEqual(self.sol.restoreIpAddresses("1111"), ["1.1.1.1"])
        self.assertEqual(self.sol.restoreIpAddresses("1010"), ["1.0.1.0"])
        self.assertEqual(self.sol.restoreIpAddresses("0010"), ["0.0.1.0"])

    def test_max_range(self):
        self.assertEqual(
            self.sol.restoreIpAddresses("255255255255"), ["255.255.255.255"]
        )

    def test_multi_solutions(self):
        self.assertEqual(
            sorted(self.sol.restoreIpAddresses("16925")),
            sorted(["1.6.9.25", "1.6.92.5", "1.69.2.5", "16.9.2.5"]),
        )
        self.assertEqual(
            sorted(self.sol.restoreIpAddresses("2332516178")),
            sorted(
                ["233.25.16.178", "233.25.161.78", "233.251.6.178", "233.251.61.78"]
            ),
        )
        self.assertEqual(
            sorted(self.sol.restoreIpAddresses("1692501124")),
            sorted(["169.250.1.124", "169.250.11.24", "169.250.112.4"]),
        )

    def test_leading_zero_handling(self):
        self.assertEqual(
            sorted(self.sol.restoreIpAddresses("010010")),
            sorted(["0.10.0.10", "0.100.1.0"]),
        )
        self.assertEqual(
            sorted(self.sol.restoreIpAddresses("10010")),
            sorted(["1.0.0.10", "10.0.1.0"]),
        )
        self.assertEqual(
            sorted(self.sol.restoreIpAddresses("100100")),
            sorted(["1.0.0.100", "10.0.10.0", "100.1.0.0"]),
        )

    def test_too_long_input(self):
        self.assertEqual(self.sol.restoreIpAddresses("12345678901234567890"), [])
        self.assertEqual(self.sol.restoreIpAddresses("9" * 13), [])

    def test_no_valid_over_255(self):
        self.assertEqual(self.sol.restoreIpAddresses("256"), [])
        self.assertEqual(self.sol.restoreIpAddresses("3003000"), [])
        self.assertEqual(self.sol.restoreIpAddresses("0000100"), [])

    def test_returns_list_of_strings(self):
        result = self.sol.restoreIpAddresses("25525511135")
        self.assertIsInstance(result, list)
        for ip in result:
            self.assertIsInstance(ip, str)

    def test_all_results_valid(self):
        for s in [
            "1",
            "12",
            "123",
            "1234",
            "12345",
            "123456",
            "1234567",
            "12345678",
            "123456789",
            "2332516178",
            "255255255255",
            "010010",
            "10010",
            "100100",
            "1692501124",
            "0000",
            "1010",
            "1111",
            "25525511135",
        ]:
            for ip in self.sol.restoreIpAddresses(s):
                self.assertTrue(_valid(ip), "invalid IP %r for %r" % (ip, s))

    def test_three_dots_exactly(self):
        for ip in self.sol.restoreIpAddresses("2332516178"):
            self.assertEqual(ip.count("."), 3)
            self.assertEqual(len(ip.split(".")), 4)

    def test_no_duplicates(self):
        for s in ["25525511135", "101023", "0000", "1692501124", "2332516178"]:
            result = self.sol.restoreIpAddresses(s)
            self.assertEqual(
                len(result),
                len(set(result)),
                "duplicates in %r for %r" % (result, s),
            )

    def test_order_independent_membership(self):
        result = self.sol.restoreIpAddresses("25525511135")
        self.assertIn("255.255.11.135", result)
        self.assertIn("255.255.111.35", result)

    def test_digits_only_input(self):
        for s in ["12345678", "00000001"]:
            for ip in self.sol.restoreIpAddresses(s):
                for p in ip.split("."):
                    self.assertTrue(_digits_only(p))


if __name__ == "__main__":
    unittest.main()

# Tags: String, Backtracking
