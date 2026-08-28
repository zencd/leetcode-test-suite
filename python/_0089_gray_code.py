# 89. Gray Code
# https://leetcode.com/problems/gray-code/
# Medium

from typing import List
import unittest


class Solution:
    def grayCode(self, n: int) -> List[int]:
        raise Exception("Not solved yet")


def is_valid_gray_code(seq: List[int], n: int) -> bool:
    if len(seq) != 1 << n:
        return False
    if seq[0] != 0:
        return False
    if len(set(seq)) != len(seq):
        return False
    for x in seq:
        if x < 0 or x >= 1 << n:
            return False

    def bit_diff(a: int, b: int) -> bool:
        v = a ^ b
        return v != 0 and (v & (v - 1)) == 0

    for i in range(1, len(seq)):
        if not bit_diff(seq[i - 1], seq[i]):
            return False
    if not bit_diff(seq[-1], seq[0]):
        return False
    return True


class TestGrayCode(unittest.TestCase):
    def test_n1(self):
        self.assertEqual(Solution().grayCode(1), [0, 1])

    def test_n2(self):
        seq = Solution().grayCode(2)
        self.assertTrue(is_valid_gray_code(seq, 2))

    def test_n3(self):
        self.assertTrue(is_valid_gray_code(Solution().grayCode(3), 3))

    def test_small_values(self):
        self.assertEqual(Solution().grayCode(1), [0, 1])
        self.assertTrue(is_valid_gray_code(Solution().grayCode(2), 2))
        self.assertTrue(is_valid_gray_code(Solution().grayCode(3), 3))

    def test_large_values(self):
        self.assertTrue(is_valid_gray_code(Solution().grayCode(15), 15))
        self.assertTrue(is_valid_gray_code(Solution().grayCode(16), 16))

    def test_sequence_starts_with_zero(self):
        self.assertEqual(Solution().grayCode(4)[0], 0)

    def test_no_duplicates(self):
        seq = Solution().grayCode(5)
        self.assertEqual(len(seq), len(set(seq)))


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Backtracking, Bit Manipulation
