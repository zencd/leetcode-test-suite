# 374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/
# Easy

def guess(num: int) -> int:
    raise NotImplementedError


class Solution:
    def guessNumber(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.picked = None
        self.original_guess = guess

    def tearDown(self):
        globals()["guess"] = self.original_guess

    def monkey_patch(self, picked):
        global guess

        def fake(num: int) -> int:
            if num > picked:
                return -1
            elif num < picked:
                return 1
            return 0

        guess = fake

    def check(self, n, picked):
        self.monkey_patch(picked)
        sol = Solution()
        self.assertEqual(sol.guessNumber(n), picked)

    def test_example1(self):
        self.check(10, 6)

    def test_example2(self):
        self.check(1, 1)

    def test_example3(self):
        self.check(2, 1)

    def test_pick_equals_n(self):
        self.check(2, 2)

    def test_pick_first(self):
        self.check(100, 1)

    def test_pick_last(self):
        self.check(100, 100)

    def test_pick_middle_odd(self):
        self.check(9, 5)

    def test_pick_middle_even(self):
        self.check(10, 5)

    def test_two_lower(self):
        self.check(2, 1)

    def test_two_upper(self):
        self.check(2, 2)

    def test_three_lower(self):
        self.check(3, 1)

    def test_three_middle(self):
        self.check(3, 2)

    def test_three_upper(self):
        self.check(3, 3)

    def test_all_small_n(self):
        for n in range(1, 51):
            for p in range(1, n + 1):
                self.monkey_patch(p)
                sol = Solution()
                self.assertEqual(sol.guessNumber(n), p)

    def test_large_n_lower(self):
        max_n = 2**31 - 1
        self.check(max_n, 1)

    def test_large_n_middle(self):
        max_n = 2**31 - 1
        self.check(max_n, 2**30)

    def test_large_n_upper(self):
        max_n = 2**31 - 1
        self.check(max_n, max_n)

    def test_large_n_near_upper(self):
        max_n = 2**31 - 1
        self.check(max_n, max_n - 1)

    def test_large_n_near_lower(self):
        max_n = 2**31 - 1
        self.check(max_n, 2)

    def test_guess_api_contract_lower_pick(self):
        self.monkey_patch(6)
        self.assertEqual(guess(6), 0)
        self.assertEqual(guess(5), 1)
        self.assertEqual(guess(7), -1)

    def test_guess_api_contract_upper_pick(self):
        self.monkey_patch(100)
        self.assertEqual(guess(100), 0)
        self.assertEqual(guess(99), 1)
        self.assertEqual(guess(1), 1)

    def test_returns_int(self):
        self.monkey_patch(7)
        sol = Solution()
        result = sol.guessNumber(10)
        self.assertIsInstance(result, int)

    def test_deterministic_repeated_calls(self):
        for _ in range(5):
            self.check(17, 9)


if __name__ == "__main__":
    unittest.main()

# Tags: Binary Search, Interactive
