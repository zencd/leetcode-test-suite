# 464. Can I Win
# https://leetcode.com/problems/can-i-win/
# Medium

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertFalse(self.sol.canIWin(10, 11))

    def test_example2_zero_total(self):
        self.assertTrue(self.sol.canIWin(10, 0))

    def test_example3_one(self):
        self.assertTrue(self.sol.canIWin(10, 1))

    def test_single_number(self):
        self.assertTrue(self.sol.canIWin(1, 1))
        self.assertFalse(self.sol.canIWin(1, 2))

    def test_two_numbers(self):
        self.assertTrue(self.sol.canIWin(2, 1))
        self.assertTrue(self.sol.canIWin(2, 2))
        self.assertFalse(self.sol.canIWin(2, 3))

    def test_three_numbers(self):
        self.assertTrue(self.sol.canIWin(3, 1))
        self.assertTrue(self.sol.canIWin(3, 2))
        self.assertTrue(self.sol.canIWin(3, 3))
        self.assertFalse(self.sol.canIWin(3, 4))
        self.assertTrue(self.sol.canIWin(3, 5))
        self.assertTrue(self.sol.canIWin(3, 6))
        self.assertFalse(self.sol.canIWin(3, 7))

    def test_impossible_total(self):
        self.assertFalse(self.sol.canIWin(3, 7))
        self.assertFalse(self.sol.canIWin(10, 56))
        self.assertFalse(self.sol.canIWin(20, 211))

    def test_desired_less_or_equal_max(self):
        for m in range(1, 8):
            self.assertTrue(self.sol.canIWin(m, m), f"maxChoosable={m}")
            self.assertTrue(self.sol.canIWin(m, m - 1), f"maxChoosable={m}")

    def test_max_20_reachable(self):
        self.assertFalse(self.sol.canIWin(10, 11))
        self.assertTrue(self.sol.canIWin(10, 10))

    def test_symmetry_two_player_hand_computed(self):
        self.assertFalse(self.sol.canIWin(4, 5))
        self.assertTrue(self.sol.canIWin(4, 6))

    def test_return_type(self):
        self.assertIsInstance(self.sol.canIWin(10, 11), bool)
        self.assertIsInstance(self.sol.canIWin(10, 0), bool)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming, Bit Manipulation, Memoization, Game Theory, Bitmask
