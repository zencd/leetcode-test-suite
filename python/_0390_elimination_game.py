# 390. Elimination Game
# https://leetcode.com/problems/elimination-game/
# Medium

class Solution:
    def lastRemaining(self, n: int) -> int:
        raise Exception("Not solved yet")


def brute_last_remaining(n: int) -> int:
    arr = list(range(1, n + 1))
    left_to_right = True
    while len(arr) > 1:
        if left_to_right:
            arr = arr[1::2]
        else:
            arr = arr[::-1][1::2][::-1]
        left_to_right = not left_to_right
    return arr[0]


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_element(self):
        self.assertEqual(self.sol.lastRemaining(1), 1)

    def test_small_n_matches_brute_force(self):
        for n in range(1, 201):
            expected = brute_last_remaining(n)
            self.assertEqual(
                self.sol.lastRemaining(n),
                expected,
                f"mismatch at n={n}",
            )

    def test_specific_small_values(self):
        cases = {
            1: 1,
            2: 2,
            3: 2,
            4: 2,
            5: 2,
            6: 4,
            7: 4,
            8: 6,
            9: 6,
            10: 8,
            11: 8,
            16: 6,
            32: 22,
        }
        for n, expected in cases.items():
            self.assertEqual(self.sol.lastRemaining(n), expected, f"n={n}")

    def test_power_of_two(self):
        for exp in range(1, 20):
            n = 1 << exp
            self.assertEqual(
                self.sol.lastRemaining(n),
                brute_last_remaining(n),
            )

    def test_large_n_in_range(self):
        values = [10**9, 10**9 - 1, 987654321, 536870912, 123456789]
        for n in values:
            result = self.sol.lastRemaining(n)
            self.assertIsInstance(result, int)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, n)

    def test_result_is_int_type(self):
        for n in (1, 2, 100, 10**9):
            self.assertIsInstance(self.sol.lastRemaining(n), int)

    def test_many_midsize_values(self):
        for n in (
            10,
            25,
            50,
            100,
            255,
            256,
            257,
            511,
            512,
            1000,
            4095,
            4096,
            4097,
            10000,
        ):
            self.assertEqual(
                self.sol.lastRemaining(n),
                brute_last_remaining(n),
            )

    def test_input_not_mutated_semantics(self):
        first = self.sol.lastRemaining(9)
        second = self.sol.lastRemaining(9)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Recursion
