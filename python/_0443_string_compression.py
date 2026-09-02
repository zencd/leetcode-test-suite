# 443. String Compression
# https://leetcode.com/problems/string-compression/
# Medium

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        self.assertEqual(self.sol.compress(chars), 6)
        self.assertEqual(chars[:6], ["a", "2", "b", "2", "c", "3"])

    def test_example2(self):
        chars = ["a"]
        self.assertEqual(self.sol.compress(chars), 1)
        self.assertEqual(chars[:1], ["a"])

    def test_example3(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.assertEqual(self.sol.compress(chars), 4)
        self.assertEqual(chars[:4], ["a", "b", "1", "2"])

    def test_all_same_single(self):
        chars = ["x"]
        self.assertEqual(self.sol.compress(chars), 1)
        self.assertEqual(chars[:1], ["x"])

    def test_all_same_9(self):
        chars = ["a"] * 9
        self.assertEqual(self.sol.compress(chars), 2)
        self.assertEqual(chars[:2], ["a", "9"])

    def test_all_same_10_digits_split(self):
        chars = ["a"] * 10
        self.assertEqual(self.sol.compress(chars), 3)
        self.assertEqual(chars[:3], ["a", "1", "0"])

    def test_all_same_100_digits_split(self):
        chars = ["z"] * 100
        self.assertEqual(self.sol.compress(chars), 4)
        self.assertEqual(chars[:4], ["z", "1", "0", "0"])

    def test_no_repeats(self):
        chars = ["a", "b", "c", "d"]
        self.assertEqual(self.sol.compress(chars), 4)
        self.assertEqual(chars[:4], ["a", "b", "c", "d"])

    def test_alternating_groups(self):
        chars = ["a", "b", "a", "b", "a"]
        self.assertEqual(self.sol.compress(chars), 5)
        self.assertEqual(chars[:5], ["a", "b", "a", "b", "a"])

    def test_uppercase_and_symbols(self):
        chars = ["A", "A", "B", "!", "!", "!"]
        self.assertEqual(self.sol.compress(chars), 5)
        self.assertEqual(chars[:5], ["A", "2", "B", "!", "3"])

    def test_digits_in_input(self):
        chars = ["1", "1", "1", "2"]
        self.assertEqual(self.sol.compress(chars), 3)
        self.assertEqual(chars[:3], ["1", "3", "2"])

    def test_mixed_groups_multi_digit(self):
        chars = ["a"] * 12 + ["b"] * 3 + ["c"]
        self.assertEqual(self.sol.compress(chars), 6)
        self.assertEqual(chars[:6], ["a", "1", "2", "b", "3", "c"])

    def test_trailing_long_group(self):
        chars = ["c", "c"] + ["b"] * 21
        self.assertEqual(self.sol.compress(chars), 5)
        self.assertEqual(chars[:5], ["c", "2", "b", "2", "1"])

    def test_length_2000_boundary(self):
        chars = ["a"] * 2000
        length = self.sol.compress(chars)
        self.assertEqual(length, 5)
        self.assertEqual(chars[:5], ["a", "2", "0", "0", "0"])

    def test_input_longer_than_needed_preserved_tail(self):
        chars = ["a", "a", "b", "b"]
        self.assertEqual(self.sol.compress(chars), 4)
        self.assertEqual(chars[:4], ["a", "2", "b", "2"])


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String
