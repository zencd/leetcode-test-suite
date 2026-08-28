# 165. Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/
# Medium

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.compareVersion("1.2", "1.10"), -1)

    def test_example2(self):
        self.assertEqual(self.sol.compareVersion("1.01", "1.001"), 0)

    def test_example3(self):
        self.assertEqual(self.sol.compareVersion("1.0", "1.0.0.0"), 0)

    def test_equal_single_revision(self):
        self.assertEqual(self.sol.compareVersion("1", "1"), 0)

    def test_greater_single_revision(self):
        self.assertEqual(self.sol.compareVersion("2", "1"), 1)

    def test_less_single_revision(self):
        self.assertEqual(self.sol.compareVersion("1", "2"), -1)

    def test_greater_multi(self):
        self.assertEqual(self.sol.compareVersion("2.0", "1.99"), 1)

    def test_less_multi(self):
        self.assertEqual(self.sol.compareVersion("1.99", "2.0"), -1)

    def test_equal_multi(self):
        self.assertEqual(self.sol.compareVersion("1.2.3", "1.2.3"), 0)

    def test_longer_wins(self):
        self.assertEqual(self.sol.compareVersion("1.2.3", "1.2"), 1)

    def test_longer_wins_negative(self):
        self.assertEqual(self.sol.compareVersion("1.2", "1.2.3"), -1)

    def test_trailing_zeros_shorter(self):
        self.assertEqual(self.sol.compareVersion("1.0.0", "1"), 0)

    def test_trailing_zeros_longer(self):
        self.assertEqual(self.sol.compareVersion("1", "1.0.0"), 0)

    def test_leading_zeros_both(self):
        self.assertEqual(self.sol.compareVersion("0001.0002", "1.2"), 0)

    def test_leading_zeros_greater(self):
        self.assertEqual(self.sol.compareVersion("010", "9"), 1)

    def test_leading_zeros_less(self):
        self.assertEqual(self.sol.compareVersion("09", "10"), -1)

    def test_zero(self):
        self.assertEqual(self.sol.compareVersion("0", "0"), 0)

    def test_zero_less(self):
        self.assertEqual(self.sol.compareVersion("0", "0.0.1"), -1)

    def test_zero_less_reversed(self):
        self.assertEqual(self.sol.compareVersion("0.0.1", "0"), 1)

    def test_large_number(self):
        self.assertEqual(self.sol.compareVersion("2147483647", "2147483646"), 1)

    def test_large_number_less(self):
        self.assertEqual(self.sol.compareVersion("2147483646", "2147483647"), -1)

    def test_many_revisions(self):
        v1 = ".".join(["1"] * 100)
        v2 = ".".join(["1"] * 99)
        self.assertEqual(self.sol.compareVersion(v1, v2), 1)

    def test_many_revisions_equal_value(self):
        v1 = ".".join(["0"] * 500)
        v2 = "0"
        self.assertEqual(self.sol.compareVersion(v1, v2), 0)

    def test_mixed_leading_zeros_and_revisions(self):
        self.assertEqual(self.sol.compareVersion("1.02", "1.2.0"), 0)

    def test_decimal_ordering(self):
        self.assertEqual(self.sol.compareVersion("10.1", "9.99"), 1)

    def test_decimal_ordering_negative(self):
        self.assertEqual(self.sol.compareVersion("9.99", "10.1"), -1)


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String
