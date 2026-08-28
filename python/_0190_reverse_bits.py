# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/
# Easy

class Solution:
    def reverseBits(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.reverseBits(43261596), 964176192)

    def test_example2(self):
        self.assertEqual(self.solution.reverseBits(2147483644), 1073741822)

    def test_zero(self):
        self.assertEqual(self.solution.reverseBits(0), 0)

    def test_one(self):
        self.assertEqual(self.solution.reverseBits(1), 1 << 31)

    def test_two(self):
        self.assertEqual(self.solution.reverseBits(2), 1073741824)

    def test_three(self):
        self.assertEqual(self.solution.reverseBits(3), 3221225472)

    def test_all_ones(self):
        self.assertEqual(self.solution.reverseBits(4294967295), 4294967295)

    def test_max_even(self):
        self.assertEqual(self.solution.reverseBits(2147483646), 2147483646)

    def test_single_high_bit(self):
        self.assertEqual(self.solution.reverseBits(1 << 31), 1)

    def test_single_mid_bit(self):
        self.assertEqual(self.solution.reverseBits(1 << 16), 1 << 15)

    def test_repeated_pattern(self):
        self.assertEqual(self.solution.reverseBits(0x0F0F0F0F), 0xF0F0F0F0)

    def test_palindrome_bits(self):
        self.assertEqual(self.solution.reverseBits(0x00005555), 0xAAAA0000)

    def test_alternating_bits(self):
        self.assertEqual(self.solution.reverseBits(0xAAAAAAAA), 0x55555555)

    def test_little_endian(self):
        self.assertEqual(self.solution.reverseBits(0x000000FF), 0xFF000000)

    def test_big_endian(self):
        self.assertEqual(self.solution.reverseBits(0x01000000), 0x80)

    def test_result_within_32_bits(self):
        for n in (0, 1, 2, 3, 0xFFFFFFFF, 0x7FFFFFFE):
            self.assertTrue(0 <= self.solution.reverseBits(n) < 1 << 32)

    def test_round_trip(self):
        values = [0, 1, 2, 3, 42, 0xFFFFFFFF, 0x12345678, 0x7FFFFFFE]
        for n in values:
            self.assertEqual(self.solution.reverseBits(self.solution.reverseBits(n)), n)


if __name__ == "__main__":
    unittest.main()

# Tags: Divide and Conquer, Bit Manipulation
