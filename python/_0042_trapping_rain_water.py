# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Hard

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_example2(self):
        self.assertEqual(self.solution.trap([4, 2, 0, 3, 2, 5]), 9)

    def test_empty_list(self):
        self.assertEqual(self.solution.trap([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.trap([5]), 0)

    def test_two_elements(self):
        self.assertEqual(self.solution.trap([3, 7]), 0)

    def test_three_elements_flat(self):
        self.assertEqual(self.solution.trap([2, 2, 2]), 0)

    def test_all_zeros(self):
        self.assertEqual(self.solution.trap([0, 0, 0, 0, 0]), 0)

    def test_single_bar(self):
        self.assertEqual(self.solution.trap([5, 0, 0, 0, 5]), 15)

    def test_no_water_trap(self):
        self.assertEqual(self.solution.trap([1, 2, 3, 4, 5]), 0)

    def test_decreasing(self):
        self.assertEqual(self.solution.trap([5, 4, 3, 2, 1]), 0)

    def test_peak_middle(self):
        self.assertEqual(self.solution.trap([3, 2, 4, 2, 3]), 2)
        self.assertEqual(self.solution.trap([1, 2, 3, 2, 1]), 0)

    def test_valley_middle(self):
        self.assertEqual(self.solution.trap([3, 1, 3]), 2)

    def test_water_on_left_only(self):
        self.assertEqual(self.solution.trap([3, 0, 0, 3, 0, 0]), 6)

    def test_water_on_right_only(self):
        self.assertEqual(self.solution.trap([0, 0, 3, 0, 0, 3]), 6)

    def test_symmetric(self):
        self.assertEqual(self.solution.trap([1, 0, 1]), 1)

    def test_equal_walls(self):
        self.assertEqual(self.solution.trap([10, 0, 0, 10]), 20)

    def test_interior_water_multiple_pools(self):
        self.assertEqual(self.solution.trap([5, 2, 3, 2, 5]), 8)

    def test_high_bar_in_middle(self):
        self.assertEqual(self.solution.trap([3, 1, 4, 1, 3]), 4)

    def test_zeros_at_both_ends(self):
        self.assertEqual(self.solution.trap([0, 1, 0, 1, 0]), 1)

    def test_large_values(self):
        self.assertEqual(
            self.solution.trap([100000, 0, 100000]),
            100000,
        )

    def test_many_poles(self):
        self.assertEqual(self.solution.trap([2, 0, 2, 0, 2, 0, 2]), 6)

    def test_one_high_wide_basin(self):
        h = [5] + [0] * 10 + [5]
        self.assertEqual(self.solution.trap(h), 50)

    def test_random_vs_brickforce(self):
        import random

        def brute(height):
            if not height:
                return 0
            total = 0
            n = len(height)
            for i in range(n):
                left = max(height[: i + 1])
                right = max(height[i:])
                total += min(left, right) - height[i]
            return total

        random.seed(42)
        for _ in range(50):
            n = random.randint(0, 20)
            h = [random.randint(0, 8) for _ in range(n)]
            self.assertEqual(self.solution.trap(h), brute(h), "input=%s" % h)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
