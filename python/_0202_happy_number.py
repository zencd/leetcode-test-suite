# 202. Happy Number
# https://leetcode.com/problems/happy-number/
# Easy

class Solution:
    def isHappy(self, n: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_19_happy(self):
        self.assertTrue(self.sol.isHappy(19))

    def test_example_2_unhappy(self):
        self.assertFalse(self.sol.isHappy(2))

    def test_one_happy(self):
        self.assertTrue(self.sol.isHappy(1))

    def test_happy_numbers(self):
        for n in [
            7,
            10,
            13,
            19,
            23,
            28,
            31,
            32,
            44,
            49,
            68,
            70,
            79,
            82,
            86,
            91,
            94,
            97,
            100,
            103,
            109,
            203,
            208,
            219,
            236,
            262,
            280,
            293,
            313,
            326,
            329,
            331,
            338,
            356,
            362,
            365,
            383,
            386,
            391,
            397,
            404,
            409,
            440,
            446,
            464,
            469,
            478,
            487,
            490,
            496,
            10000,
            10009,
            10030,
            10033,
        ]:
            self.assertTrue(self.sol.isHappy(n), f"{n} should be happy")

    def test_unhappy_numbers(self):
        for n in [
            2,
            3,
            4,
            5,
            6,
            8,
            9,
            11,
            12,
            14,
            15,
            16,
            17,
            18,
            20,
            21,
            22,
            24,
            25,
            26,
            27,
            29,
            30,
            33,
            34,
            35,
            38,
            41,
            99,
            184,
            128,
            888888,
            2147483647,
        ]:
            self.assertFalse(self.sol.isHappy(n), f"{n} should not be happy")

    def test_single_digit(self):
        expected = {
            1: True,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False,
            7: True,
            8: False,
            9: False,
        }
        for n, res in expected.items():
            self.assertEqual(self.sol.isHappy(n), res, f"n={n}")

    def test_max_constraint(self):
        self.assertFalse(self.sol.isHappy(2**31 - 1))

    def test_returns_bool(self):
        self.assertIsInstance(self.sol.isHappy(19), bool)
        self.assertIsInstance(self.sol.isHappy(2), bool)

    def test_bruteforce_cross_check(self):
        def naive(n):
            seen = set()
            while n != 1 and n not in seen:
                seen.add(n)
                total = 0
                while n:
                    n, d = divmod(n, 10)
                    total += d * d
                n = total
            return n == 1

        for n in range(1, 300):
            self.assertEqual(self.sol.isHappy(n), naive(n), f"n={n}")


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Math, Two Pointers, Floyd's Cycle Finding Algorithm
