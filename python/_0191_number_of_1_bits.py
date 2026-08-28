# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
# Easy

class Solution:
    def hammingWeight(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.hammingWeight(11), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.hammingWeight(128), 1)

    def test_example_3(self):
        self.assertEqual(self.sol.hammingWeight(2147483645), 30)

    def test_one(self):
        self.assertEqual(self.sol.hammingWeight(1), 1)

    def test_two(self):
        self.assertEqual(self.sol.hammingWeight(2), 1)

    def test_three(self):
        self.assertEqual(self.sol.hammingWeight(3), 2)

    def test_four(self):
        self.assertEqual(self.sol.hammingWeight(4), 1)

    def test_seven(self):
        self.assertEqual(self.sol.hammingWeight(7), 3)

    def test_eight(self):
        self.assertEqual(self.sol.hammingWeight(8), 1)

    def test_powers_of_two(self):
        for k in range(31):
            self.assertEqual(self.sol.hammingWeight(1 << k), 1)

    def test_all_bits_set_small(self):
        self.assertEqual(self.sol.hammingWeight(2**8 - 1), 8)

    def test_all_bits_set_32bit(self):
        self.assertEqual(self.sol.hammingWeight(2**32 - 1), 32)

    def test_max_32bit(self):
        self.assertEqual(self.sol.hammingWeight(2**31 - 1), 31)

    def test_min_constraint(self):
        self.assertEqual(self.sol.hammingWeight(0), 0)

    def test_alternating_bits(self):
        self.assertEqual(self.sol.hammingWeight(0b1010), 2)
        self.assertEqual(self.sol.hammingWeight(0b1010101), 4)

    def test_even_and_odd(self):
        self.assertEqual(self.sol.hammingWeight(10), 2)
        self.assertEqual(self.sol.hammingWeight(13), 3)

    def test_against_bin_count(self):
        for n in [0, 1, 9, 42, 99, 255, 1023, 4096, 65535, 123456789]:
            self.assertEqual(self.sol.hammingWeight(n), bin(n).count("1"))

    def test_large_random_values(self):
        import random

        random.seed(191)
        for _ in range(50):
            n = random.randrange(1, 2**31)
            self.assertEqual(self.sol.hammingWeight(n), bin(n).count("1"))

    def test_return_type_is_int(self):
        self.assertIsInstance(self.sol.hammingWeight(11), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Divide and Conquer, Bit Manipulation
