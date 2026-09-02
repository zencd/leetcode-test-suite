# 458. Poor Pigs
# https://leetcode.com/problems/poor-pigs/
# Hard

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.poorPigs(4, 15, 15), 2)
        self.assertEqual(self.sol.poorPigs(4, 15, 30), 2)

    def test_single_bucket(self):
        self.assertEqual(self.sol.poorPigs(1, 15, 15), 0)
        self.assertEqual(self.sol.poorPigs(1, 1, 1), 0)
        self.assertEqual(self.sol.poorPigs(1, 100, 100), 0)

    def test_single_round(self):
        self.assertEqual(self.sol.poorPigs(2, 15, 15), 1)
        self.assertEqual(self.sol.poorPigs(3, 15, 15), 2)
        self.assertEqual(self.sol.poorPigs(10, 15, 15), 4)
        self.assertEqual(self.sol.poorPigs(8, 15, 15), 3)

    def test_exact_powers(self):
        self.assertEqual(self.sol.poorPigs(9, 15, 15), 4)
        self.assertEqual(self.sol.poorPigs(27, 15, 45), 3)
        self.assertEqual(self.sol.poorPigs(64, 15, 75), 3)

    def test_multiple_rounds(self):
        self.assertEqual(self.sol.poorPigs(8, 15, 30), 2)
        self.assertEqual(self.sol.poorPigs(27, 15, 45), 3)
        self.assertEqual(self.sol.poorPigs(100, 15, 150), 2)

    def test_many_rounds(self):
        self.assertEqual(self.sol.poorPigs(1000, 1, 100), 2)
        self.assertEqual(self.sol.poorPigs(1000, 15, 100), 4)
        self.assertEqual(self.sol.poorPigs(1000, 100, 100), 10)

    def test_edge_constraints(self):
        self.assertEqual(self.sol.poorPigs(1000, 1, 1), 10)
        self.assertEqual(self.sol.poorPigs(1000, 100, 100), 10)
        self.assertEqual(self.sol.poorPigs(1, 1, 100), 0)

    def test_one_round_many_rounds_boundary(self):
        self.assertEqual(self.sol.poorPigs(2, 15, 29), 1)
        self.assertEqual(self.sol.poorPigs(4, 15, 29), 2)
        self.assertEqual(self.sol.poorPigs(4, 15, 30), 2)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming, Combinatorics
