# 292. Nim Game
# https://leetcode.com/problems/nim-game/
# Easy

class Solution:
    def canWinNim(self, n: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_single_stone(self):
        self.assertTrue(Solution().canWinNim(1))

    def test_two_stones(self):
        self.assertTrue(Solution().canWinNim(2))

    def test_three_stones(self):
        self.assertTrue(Solution().canWinNim(3))

    def test_four_stones(self):
        self.assertFalse(Solution().canWinNim(4))

    def test_five_stones(self):
        self.assertTrue(Solution().canWinNim(5))

    def test_six_stones(self):
        self.assertTrue(Solution().canWinNim(6))

    def test_seven_stones(self):
        self.assertTrue(Solution().canWinNim(7))

    def test_eight_stones(self):
        self.assertFalse(Solution().canWinNim(8))

    def test_nine_stones(self):
        self.assertTrue(Solution().canWinNim(9))

    def test_twelve_stones(self):
        self.assertFalse(Solution().canWinNim(12))

    def test_thirteen_stones(self):
        self.assertTrue(Solution().canWinNim(13))

    def test_large_multiple_of_four(self):
        self.assertFalse(Solution().canWinNim(10**9))

    def test_large_multiple_of_four_plus_one(self):
        self.assertTrue(Solution().canWinNim(10**9 + 1))

    def test_max_value(self):
        self.assertFalse(Solution().canWinNim((1 << 31) - 1 - ((1 << 31) - 1) % 4))

    def test_max_value_not_multiple_of_four(self):
        n = (1 << 31) - 1
        self.assertTrue(n % 4 != 0)
        self.assertTrue(Solution().canWinNim(n))

    def test_seventy_two_stones(self):
        self.assertFalse(Solution().canWinNim(72))

    def test_seventy_three_stones(self):
        self.assertTrue(Solution().canWinNim(73))

    def test_returns_bool_type(self):
        self.assertIsInstance(Solution().canWinNim(1), bool)
        self.assertIsInstance(Solution().canWinNim(4), bool)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Brainteaser, Minimax, Game Theory, Nim Game, Impartial Game
