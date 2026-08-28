# 393. UTF-8 Validation
# https://leetcode.com/problems/utf-8-validation/
# Medium

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.validUtf8([197, 130, 1]))

    def test_example2(self):
        self.assertFalse(self.sol.validUtf8([235, 140, 4]))

    def test_single_1byte(self):
        self.assertTrue(self.sol.validUtf8([0]))
        self.assertTrue(self.sol.validUtf8([127]))
        self.assertTrue(self.sol.validUtf8([65]))

    def test_1byte_sequence(self):
        self.assertTrue(self.sol.validUtf8([72, 101, 108, 108, 111]))

    def test_single_2byte(self):
        self.assertTrue(self.sol.validUtf8([194, 161]))
        self.assertTrue(self.sol.validUtf8([223, 160]))

    def test_2byte_missing_continuation(self):
        self.assertFalse(self.sol.validUtf8([194]))

    def test_2byte_bad_continuation(self):
        self.assertFalse(self.sol.validUtf8([194, 65]))
        self.assertTrue(self.sol.validUtf8([194, 128]))
        self.assertFalse(self.sol.validUtf8([194, 255]))

    def test_single_3byte(self):
        self.assertTrue(self.sol.validUtf8([225, 160, 128]))
        self.assertTrue(self.sol.validUtf8([225, 160, 128]))

    def test_3byte_truncated(self):
        self.assertFalse(self.sol.validUtf8([225]))
        self.assertFalse(self.sol.validUtf8([225, 160]))

    def test_3byte_bad_second_continuation(self):
        self.assertFalse(self.sol.validUtf8([225, 160, 65]))

    def test_3byte_bad_first_continuation(self):
        self.assertFalse(self.sol.validUtf8([225, 65, 160]))

    def test_single_4byte(self):
        self.assertTrue(self.sol.validUtf8([240, 144, 144, 146]))
        self.assertTrue(self.sol.validUtf8([244, 143, 155, 165]))

    def test_4byte_truncated(self):
        self.assertFalse(self.sol.validUtf8([240]))
        self.assertFalse(self.sol.validUtf8([240, 144]))
        self.assertFalse(self.sol.validUtf8([240, 144, 144]))

    def test_4byte_bad_continuation(self):
        self.assertFalse(self.sol.validUtf8([240, 144, 65, 144]))
        self.assertFalse(self.sol.validUtf8([240, 65, 144, 144]))

    def test_invalid_leading_5bytes(self):
        self.assertFalse(self.sol.validUtf8([248, 192, 160, 144, 128]))

    def test_invalid_leading_0xff(self):
        self.assertFalse(self.sol.validUtf8([255]))

    def test_invalid_leading_0xfe(self):
        self.assertFalse(self.sol.validUtf8([254, 163]))

    def test_continuation_byte_alone(self):
        self.assertFalse(self.sol.validUtf8([128]))
        self.assertFalse(self.sol.validUtf8([191]))

    def test_mixed_valid(self):
        self.assertTrue(
            self.sol.validUtf8([197, 130, 225, 147, 152, 242, 175, 151, 151, 72, 105])
        )

    def test_extra_trailing_continuation(self):
        self.assertFalse(self.sol.validUtf8([194, 160, 194]))

    def test_continuation_after_new_start(self):
        self.assertFalse(self.sol.validUtf8([240, 242, 175, 151]))

    def test_empty_not_allowed_but_single_ok(self):
        self.assertTrue(self.sol.validUtf8([0]))

    def test_only_127_boundary(self):
        self.assertTrue(self.sol.validUtf8([126, 127]))
        self.assertFalse(self.sol.validUtf8([128]))

    def test_all_255(self):
        self.assertFalse(self.sol.validUtf8([255, 255, 255]))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Bit Manipulation
