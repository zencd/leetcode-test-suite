# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Medium

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_example2(self):
        self.assertEqual(self.sol.maxArea([1, 1]), 1)

    def test_two_elements(self):
        self.assertEqual(self.sol.maxArea([4, 9]), 4)

    def test_all_equal(self):
        self.assertEqual(self.sol.maxArea([3, 3, 3, 3, 3]), 12)

    def test_increasing(self):
        self.assertEqual(self.sol.maxArea([1, 2, 3, 4]), 4)

    def test_decreasing(self):
        self.assertEqual(self.sol.maxArea([4, 3, 2, 1]), 4)

    def test_zero(self):
        self.assertEqual(self.sol.maxArea([0, 0]), 0)

    def test_zero_inside(self):
        self.assertEqual(self.sol.maxArea([0, 5, 0, 5, 0]), 10)

    def test_max_heights(self):
        self.assertEqual(self.sol.maxArea([10**4, 10**4]), 10**4)

    def test_max_area_at_extremes(self):
        self.assertEqual(self.sol.maxArea([1, 0, 0, 0, 10**4]), 4 * 1)

    def test_max_area_from_tall_edges(self):
        self.assertEqual(self.sol.maxArea([10**4, 1, 1, 10**4]), 3 * 10**4)

    def test_long_array_same_height(self):
        n = 10**5
        self.assertEqual(self.sol.maxArea([5] * n), 5 * (n - 1))

    def test_long_array_ramp(self):
        n = 10**5
        height = list(range(n))
        left = 0
        right = n - 1
        expected = 0
        while left < right:
            expected = max(expected, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        self.assertEqual(self.sol.maxArea(height), expected)

    def test_input_not_mutated(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        snapshot = list(height)
        self.sol.maxArea(height)
        self.assertEqual(height, snapshot)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Greedy
