# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/
# Easy

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.hammingDistance(1, 4), 2)

    def test_example_2(self):
        self.assertEqual(self.sol.hammingDistance(3, 1), 1)

    def test_same_numbers(self):
        self.assertEqual(self.sol.hammingDistance(0, 0), 0)
        self.assertEqual(self.sol.hammingDistance(5, 5), 0)
        self.assertEqual(self.sol.hammingDistance(2**31 - 1, 2**31 - 1), 0)

    def test_zero_vs_nonzero(self):
        self.assertEqual(self.sol.hammingDistance(0, 1), 1)
        self.assertEqual(self.sol.hammingDistance(0, 7), 3)
        self.assertEqual(self.sol.hammingDistance(7, 0), 3)

    def test_powers_of_two(self):
        self.assertEqual(self.sol.hammingDistance(0, 8), 1)
        self.assertEqual(self.sol.hammingDistance(8, 16), 2)
        self.assertEqual(self.sol.hammingDistance(4, 8), 2)

    def test_all_bits_different(self):
        self.assertEqual(self.sol.hammingDistance(0, 2**31 - 1), 31)

    def test_max_constraint(self):
        self.assertEqual(self.sol.hammingDistance(2**31 - 1, 0), 31)
        self.assertEqual(self.sol.hammingDistance(2**31 - 1, 2**30), 30)

    def test_single_bit_difference(self):
        self.assertEqual(self.sol.hammingDistance(2**30, 0), 1)
        self.assertEqual(self.sol.hammingDistance(1073741824, 1073741825), 1)

    def test_symmetry(self):
        self.assertEqual(self.sol.hammingDistance(12, 34), self.sol.hammingDistance(34, 12))
        self.assertEqual(self.sol.hammingDistance(100, 255), self.sol.hammingDistance(255, 100))

    def test_known_values(self):
        self.assertEqual(self.sol.hammingDistance(9, 3), 2)
        self.assertEqual(self.sol.hammingDistance(10, 9), 2)
        self.assertEqual(self.sol.hammingDistance(255, 254), 1)
        self.assertEqual(self.sol.hammingDistance(15, 3), 2)

    def test_against_reference(self):
        for x, y in [(0, 0), (0, 1), (1, 4), (3, 1), (42, 37), (2**31 - 1, 1)]:
            expected = sum(1 for b in range(31) if ((x >> b) & 1) != ((y >> b) & 1))
            self.assertEqual(self.sol.hammingDistance(x, y), expected, f"Failed for x={x}, y={y}")


if __name__ == "__main__":
    unittest.main()

# Tags: Bit Manipulation
