# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/
# Easy

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.findContentChildren([1, 2, 3], [1, 1]), 1)

    def test_example2(self):
        self.assertEqual(self.sol.findContentChildren([1, 2], [1, 2, 3]), 2)

    def test_no_cookies(self):
        self.assertEqual(self.sol.findContentChildren([1, 2, 3], []), 0)

    def test_children_larger_than_any_cookie(self):
        self.assertEqual(self.sol.findContentChildren([5, 6], [1, 2, 3]), 0)

    def test_single_child_single_cookie_fit(self):
        self.assertEqual(self.sol.findContentChildren([3], [3]), 1)

    def test_single_child_single_cookie_too_small(self):
        self.assertEqual(self.sol.findContentChildren([3], [2]), 0)

    def test_all_children_satisfied(self):
        self.assertEqual(self.sol.findContentChildren([1, 1, 1], [2, 2, 2]), 3)

    def test_fewer_cookies_than_children(self):
        self.assertEqual(self.sol.findContentChildren([1, 1, 1, 1], [1, 1]), 2)

    def test_unsorted_inputs(self):
        self.assertEqual(self.sol.findContentChildren([3, 1, 2], [2, 1, 3]), 3)

    def test_equal_sizes_and_counts(self):
        self.assertEqual(self.sol.findContentChildren([1, 2, 3], [1, 2, 3]), 3)

    def test_large_values(self):
        v = 2**31 - 1
        self.assertEqual(self.sol.findContentChildren([v], [v]), 1)
        self.assertEqual(self.sol.findContentChildren([v], [v - 1]), 0)

    def test_identical_cookies_insufficient(self):
        self.assertEqual(self.sol.findContentChildren([2, 2, 2], [1, 1, 1]), 0)

    def test_mixed_match(self):
        self.assertEqual(self.sol.findContentChildren([5, 1, 2], [1, 1, 1]), 1)

    def test_one_huge_cookie(self):
        self.assertEqual(self.sol.findContentChildren([1, 2, 3], [100]), 1)

    def test_duplicates_both_sides(self):
        self.assertEqual(self.sol.findContentChildren([1, 1, 2, 2], [1, 1, 2, 2]), 4)

    def test_large_lists_match(self):
        g = [1] * 10000
        s = [1] * 10000
        self.assertEqual(self.sol.findContentChildren(g, s), 10000)

    def test_large_lists_mismatch(self):
        g = [2] * 10000
        s = [1] * 10000
        self.assertEqual(self.sol.findContentChildren(g, s), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Greedy, Sorting, Quicksort
