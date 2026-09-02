# 482. License Key Formatting
# https://leetcode.com/problems/license-key-formatting/
# Easy

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.licenseKeyFormatting("5F3Z-2e-9-w", 4), "5F3Z-2E9W")

    def test_example2(self):
        self.assertEqual(self.sol.licenseKeyFormatting("2-5g-3-J", 2), "2-5G-3J")

    def test_single_char(self):
        self.assertEqual(self.sol.licenseKeyFormatting("a", 1), "A")

    def test_single_char_large_k(self):
        self.assertEqual(self.sol.licenseKeyFormatting("a", 5), "A")

    def test_k_equals_1(self):
        self.assertEqual(self.sol.licenseKeyFormatting("abcd", 1), "A-B-C-D")

    def test_k_equals_length(self):
        self.assertEqual(self.sol.licenseKeyFormatting("abcd", 4), "ABCD")

    def test_k_greater_than_length(self):
        self.assertEqual(self.sol.licenseKeyFormatting("z-9-a", 5), "Z9A")

    def test_lower_to_upper(self):
        self.assertEqual(self.sol.licenseKeyFormatting("a-cc", 1), "A-C-C")

    def test_all_dashes(self):
        self.assertEqual(self.sol.licenseKeyFormatting("-", 2), "")

    def test_all_dashes_multiple(self):
        self.assertEqual(self.sol.licenseKeyFormatting("--", 1), "")

    def test_consecutive_dashes(self):
        self.assertEqual(self.sol.licenseKeyFormatting("ab--cd", 2), "AB-CD")

    def test_leading_dash(self):
        self.assertEqual(self.sol.licenseKeyFormatting("-a-b-c", 2), "A-BC")

    def test_trailing_dash(self):
        self.assertEqual(self.sol.licenseKeyFormatting("a-b-c-", 2), "A-BC")

    def test_digits_only(self):
        self.assertEqual(self.sol.licenseKeyFormatting("1-2-3", 2), "1-23")

    def test_first_group_shorter1(self):
        self.assertEqual(self.sol.licenseKeyFormatting("abcd-efgh", 5), "ABC-DEFGH")

    def test_first_group_shorter2(self):
        self.assertEqual(self.sol.licenseKeyFormatting("abcd-efgh", 2), "AB-CD-EF-GH")

    def test_seven_chars(self):
        self.assertEqual(self.sol.licenseKeyFormatting("abcdefg", 5), "AB-CDEFG")

    def test_all_groups_even(self):
        self.assertEqual(self.sol.licenseKeyFormatting("a-b-c-d", 2), "AB-CD")

    def test_single_group(self):
        self.assertEqual(self.sol.licenseKeyFormatting("a-bc", 2), "A-BC")

    def test_abc_k3(self):
        self.assertEqual(self.sol.licenseKeyFormatting("abc", 3), "ABC")


if __name__ == "__main__":
    unittest.main()

# Tags: String
