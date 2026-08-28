# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/
# Easy

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zero(self):
        self.assertEqual(self.sol.countBits(0), [0])

    def test_one(self):
        self.assertEqual(self.sol.countBits(1), [0, 1])

    def test_example_1(self):
        self.assertEqual(self.sol.countBits(2), [0, 1, 1])

    def test_example_2(self):
        self.assertEqual(self.sol.countBits(5), [0, 1, 1, 2, 1, 2])

    def test_three(self):
        self.assertEqual(self.sol.countBits(3), [0, 1, 1, 2])

    def test_seven(self):
        self.assertEqual(self.sol.countBits(7), [0, 1, 1, 2, 1, 2, 2, 3])

    def test_eight(self):
        self.assertEqual(self.sol.countBits(8), [0, 1, 1, 2, 1, 2, 2, 3, 1])

    def test_ten(self):
        self.assertEqual(self.sol.countBits(10), [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2])

    def test_fifteen(self):
        self.assertEqual(
            self.sol.countBits(15),
            [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4],
        )

    def test_sixteen(self):
        self.assertEqual(self.sol.countBits(16)[:9], [0, 1, 1, 2, 1, 2, 2, 3, 1])
        self.assertEqual(self.sol.countBits(16)[16], 1)
        self.assertEqual(len(self.sol.countBits(16)), 17)

    def test_twenty_five_five(self):
        self.assertEqual(self.sol.countBits(255)[-1], 8)

    def test_result_length(self):
        for n in [0, 1, 42, 999]:
            self.assertEqual(len(self.sol.countBits(n)), n + 1)

    def test_matches_reference_for_range(self):
        n = 1000
        expected = [bin(i).count("1") for i in range(n + 1)]
        self.assertEqual(self.sol.countBits(n), expected)

    def test_max_constraint(self):
        n = 10**5
        result = self.sol.countBits(n)
        self.assertEqual(len(result), n + 1)
        expected = [bin(i).count("1") for i in range(n + 1)]
        self.assertEqual(result, expected)

    def test_powers_of_two_have_single_bit(self):
        n = 1024
        result = self.sol.countBits(n)
        for i in range(n + 1):
            is_power_of_two = i != 0 and (i & (i - 1)) == 0
            if is_power_of_two:
                self.assertEqual(result[i], 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Dynamic Programming, Bit Manipulation
