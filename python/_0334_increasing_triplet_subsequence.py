# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/
# Medium

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertTrue(self.sol.increasingTriplet([1, 2, 3, 4, 5]))

    def test_example_2(self):
        self.assertFalse(self.sol.increasingTriplet([5, 4, 3, 2, 1]))

    def test_example_3(self):
        self.assertTrue(self.sol.increasingTriplet([2, 1, 5, 0, 4, 6]))

    def test_length_less_than_three(self):
        self.assertFalse(self.sol.increasingTriplet([]))
        self.assertFalse(self.sol.increasingTriplet([1]))
        self.assertFalse(self.sol.increasingTriplet([1, 2]))
        self.assertFalse(self.sol.increasingTriplet([2, 1]))

    def test_exactly_three(self):
        self.assertTrue(self.sol.increasingTriplet([1, 2, 3]))
        self.assertFalse(self.sol.increasingTriplet([3, 2, 1]))
        self.assertFalse(self.sol.increasingTriplet([1, 3, 2]))
        self.assertFalse(self.sol.increasingTriplet([1, 1, 1]))

    def test_duplicates_no_strict_increase(self):
        self.assertFalse(self.sol.increasingTriplet([1, 1, 1, 1]))
        self.assertFalse(self.sol.increasingTriplet([1, 2, 2, 2]))
        self.assertTrue(self.sol.increasingTriplet([1, 2, 2, 3]))

    def test_triplet_not_at_start(self):
        self.assertTrue(self.sol.increasingTriplet([9, 8, 1, 2, 3]))

    def test_triplet_with_interleaving(self):
        self.assertTrue(self.sol.increasingTriplet([2, 1, 5, 0, 4, 6]))
        self.assertTrue(self.sol.increasingTriplet([10, 20, 30, 1, 2, 3, 1]))

    def test_triplet_ends_with_larger_negative(self):
        self.assertTrue(self.sol.increasingTriplet([-1, -5, -2, -4, -3, 0]))

    def test_all_negative(self):
        self.assertTrue(self.sol.increasingTriplet([-5, -4, -3]))
        self.assertFalse(self.sol.increasingTriplet([-3, -4, -5]))

    def test_extreme_values(self):
        self.assertTrue(self.sol.increasingTriplet([-(2**31), 0, 2**31 - 1]))
        self.assertFalse(self.sol.increasingTriplet([2**31 - 1, 0, -(2**31)]))
        self.assertTrue(self.sol.increasingTriplet([0, 1, -(2**31), 2**31 - 1]))

    def test_oscillating(self):
        self.assertTrue(self.sol.increasingTriplet([1, 3, 2, 4, 3, 5, 4, 6, 5]))
        self.assertTrue(self.sol.increasingTriplet([2, 1, 3, 2, 4]))
        self.assertFalse(self.sol.increasingTriplet([2, 1, 2, 1, 2, 1]))
        self.assertFalse(self.sol.increasingTriplet([1, 2, 1, 2, 1, 2]))

    def test_two_equal_extremes(self):
        self.assertFalse(self.sol.increasingTriplet([1, 3, 2, 2]))
        self.assertTrue(self.sol.increasingTriplet([1, 3, 2, 2, 3]))

    def test_larger_array(self):
        nums = list(range(1000, 0, -1)) + [1, 2, 3]
        self.assertTrue(self.sol.increasingTriplet(nums))

    def test_random_smoke(self):
        import random

        random.seed(42)
        for _ in range(50):
            n = random.randint(1, 30)
            arr = [random.randint(-10, 10) for _ in range(n)]
            expected = False
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        if arr[i] < arr[j] < arr[k]:
                            expected = True
            self.assertEqual(
                self.sol.increasingTriplet(arr), expected, f"mismatch for {arr}"
            )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Greedy, Longest Increasing Subsequence
