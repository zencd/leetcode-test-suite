# 470. Implement Rand10() Using Rand7()
# https://leetcode.com/problems/implement-rand10-using-rand7/
# Medium

import random

_rnd = random.Random(12345)


def rand7():
    return _rnd.randrange(1, 8)


class Solution:
    def rand10(self):
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self._old_rand7 = globals().get("rand7")

    def tearDown(self):
        if self._old_rand7 is not None:
            globals()["rand7"] = self._old_rand7
        _rnd.seed(12345)

    def _mock_rand7(self, sequence):
        it = iter(list(sequence))

        def fake():
            return next(it)

        globals()["rand7"] = fake
        return fake

    def test_output_is_within_range_for_many_calls(self):
        self._old_rand7 = None
        for _ in range(1000):
            self.assertIn(self.sol.rand10(), range(1, 11))

    def test_single_call_returns_valid_value(self):
        self.assertIn(self.sol.rand10(), range(1, 11))

    def test_all_ten_values_appear(self):
        seen = set(self.sol.rand10() for _ in range(10000))
        self.assertEqual(seen, set(range(1, 11)))

    def test_distribution_is_roughly_uniform(self):
        counts = [0] * 11
        n = 100000
        for _ in range(n):
            counts[self.sol.rand10()] += 1
        counts = counts[1:]
        mean = n / 10
        for c in counts:
            self.assertAlmostEqual(c, mean, delta=mean * 0.1)

    def test_chi_square_uniformity(self):
        n = 100000
        counts = [0] * 10
        for _ in range(n):
            counts[self.sol.rand10() - 1] += 1
        mean = n / 10
        chi2 = sum((c - mean) ** 2 / mean for c in counts)
        self.assertLess(chi2, 27.9)

    def test_deterministic_sequence_with_fixed_rand7(self):
        self._mock_rand7([1, 1])
        self.assertEqual(self.sol.rand10(), 1)
        self._mock_rand7([7, 7, 1, 1])
        self.assertEqual(self.sol.rand10(), 1)
        self._mock_rand7([1, 5])
        self.assertEqual(self.sol.rand10(), 5)
        self._mock_rand7([2, 3])
        self.assertEqual(self.sol.rand10(), 10)
        self._mock_rand7([4, 7])
        self.assertEqual(self.sol.rand10(), 8)
        seq = [7] * 12 + [1, 1]
        self._mock_rand7(seq)
        self.assertEqual(self.sol.rand10(), 1)

    def test_rejection_of_out_of_range_pairs(self):
        seq = [7, 7, 7, 6, 7, 5, 7, 4, 7, 3, 7, 2, 7, 1, 6, 7] + [1, 5]
        self._mock_rand7(seq)
        self.assertEqual(self.sol.rand10(), 5)

    def test_no_builtin_random_used_in_solution(self):
        import inspect

        src = inspect.getsource(Solution.rand10)
        self.assertNotIn("random", src)
        self.assertNotIn("randint", src)

    def test_does_not_depend_on_solution_state(self):
        a = self.sol.rand10()
        b = self.sol.rand10()
        self.assertIn(a, range(1, 11))
        self.assertIn(b, range(1, 11))

    def test_returns_int_type(self):
        self.assertIsInstance(self.sol.rand10(), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Rejection Sampling, Randomized, Probability and Statistics
