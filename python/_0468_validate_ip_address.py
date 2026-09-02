# 468. Validate IP Address
# https://leetcode.com/problems/validate-ip-address/
# Medium

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_ipv4(self):
        self.assertEqual(self.sol.validIPAddress("172.16.254.1"), "IPv4")

    def test_example_ipv6(self):
        self.assertEqual(self.sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"), "IPv6")

    def test_example_neither(self):
        self.assertEqual(self.sol.validIPAddress("256.256.256.256"), "Neither")

    def test_ipv4_valid_basic(self):
        self.assertEqual(self.sol.validIPAddress("192.168.1.1"), "IPv4")

    def test_ipv4_zero(self):
        self.assertEqual(self.sol.validIPAddress("0.0.0.0"), "IPv4")

    def test_ipv4_max(self):
        self.assertEqual(self.sol.validIPAddress("255.255.255.255"), "IPv4")

    def test_ipv4_trailing_zero(self):
        self.assertEqual(self.sol.validIPAddress("192.168.1.0"), "IPv4")

    def test_ipv4_leading_zero(self):
        self.assertEqual(self.sol.validIPAddress("192.168.01.1"), "Neither")

    def test_ipv4_double_zero(self):
        self.assertEqual(self.sol.validIPAddress("192.168.1.00"), "Neither")

    def test_ipv4_over_255(self):
        self.assertEqual(self.sol.validIPAddress("256.256.256.256"), "Neither")

    def test_ipv4_wrong_count_dots(self):
        self.assertEqual(self.sol.validIPAddress("1.1.1"), "Neither")
        self.assertEqual(self.sol.validIPAddress("1.1.1.1.1"), "Neither")

    def test_ipv4_empty_part(self):
        self.assertEqual(self.sol.validIPAddress("1..1.1"), "Neither")
        self.assertEqual(self.sol.validIPAddress(".1.1.1"), "Neither")
        self.assertEqual(self.sol.validIPAddress("1.1.1."), "Neither")

    def test_ipv4_with_letters(self):
        self.assertEqual(self.sol.validIPAddress("1a.1.1.1"), "Neither")
        self.assertEqual(self.sol.validIPAddress("192.168@1.1"), "Neither")

    def test_ipv6_valid_lowercase(self):
        self.assertEqual(self.sol.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"), "IPv6")

    def test_ipv6_short_groups(self):
        self.assertEqual(self.sol.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334"), "IPv6")

    def test_ipv6_all_zeros(self):
        self.assertEqual(self.sol.validIPAddress("0:0:0:0:0:0:0:0"), "IPv6")

    def test_ipv6_max_hex(self):
        self.assertEqual(self.sol.validIPAddress("ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"), "IPv6")

    def test_ipv6_leading_zeros_allowed(self):
        self.assertEqual(self.sol.validIPAddress("0001:0001:0001:0001:0001:0001:0001:0001"), "IPv6")

    def test_ipv6_too_long_group(self):
        self.assertEqual(self.sol.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334"), "Neither")

    def test_ipv6_invalid_char(self):
        self.assertEqual(self.sol.validIPAddress("2001:0db8:85a3::8A2E:037j:7334"), "Neither")
        self.assertEqual(self.sol.validIPAddress("2001:0db8:85a3:0:0:8g2e:0370:7334"), "Neither")

    def test_ipv6_empty_group(self):
        self.assertEqual(self.sol.validIPAddress("2001:0db8:85a3::8A2E:0370:7334"), "Neither")
        self.assertEqual(self.sol.validIPAddress("2001:0db8::85a3:0:0:8A2E:0370:7334"), "Neither")

    def test_ipv6_wrong_count(self):
        self.assertEqual(self.sol.validIPAddress("2001:db8:85a3:8A2E:0370:7334"), "Neither")
        self.assertEqual(self.sol.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334:ffff"), "Neither")

    def test_empty_string(self):
        self.assertEqual(self.sol.validIPAddress(""), "Neither")

    def test_only_dots(self):
        self.assertEqual(self.sol.validIPAddress("...."), "Neither")

    def test_only_colons(self):
        self.assertEqual(self.sol.validIPAddress(":::::::"), "Neither")

    def test_mixed_separators(self):
        self.assertEqual(self.sol.validIPAddress("1.1.1:1"), "Neither")
        self.assertEqual(self.sol.validIPAddress("1:1:1.1"), "Neither")

    def test_single_dot(self):
        self.assertEqual(self.sol.validIPAddress("1.1.1.2:2"), "Neither")

    def test_ipv6_with_dots(self):
        self.assertEqual(self.sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:1.2.3.4"), "Neither")

    def test_letters_only(self):
        self.assertEqual(self.sol.validIPAddress("abcdef"), "Neither")


if __name__ == "__main__":
    unittest.main()

# Tags: String
