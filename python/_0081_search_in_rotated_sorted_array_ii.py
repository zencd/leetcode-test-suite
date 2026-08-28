# 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Medium

import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        raise Exception("Not solved yet")


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assert_search(self, nums, target, expected):
        self.assertEqual(self.solution.search(nums, target), expected)

    def test_example_1(self):
        self.assert_search([2, 5, 6, 0, 0, 1, 2], 0, True)

    def test_example_2(self):
        self.assert_search([2, 5, 6, 0, 0, 1, 2], 3, False)

    def test_single_element_present(self):
        self.assert_search([1], 1, True)

    def test_single_element_absent(self):
        self.assert_search([1], 2, False)

    def test_two_elements_present(self):
        self.assert_search([1, 3], 1, True)
        self.assert_search([1, 3], 3, True)

    def test_two_elements_absent(self):
        self.assert_search([1, 3], 2, False)

    def test_no_rotation_first_element(self):
        self.assert_search([1, 2, 3, 4, 5], 1, True)

    def test_no_rotation_last_element(self):
        self.assert_search([1, 2, 3, 4, 5], 5, True)

    def test_no_rotation_middle_element(self):
        self.assert_search([1, 2, 3, 4, 5], 3, True)

    def test_no_rotation_absent(self):
        self.assert_search([1, 2, 3, 4, 5], 6, False)

    def test_rotate_full_left(self):
        self.assert_search([5, 1, 2, 3, 4], 1, True)
        self.assert_search([5, 1, 2, 3, 4], 5, True)
        self.assert_search([5, 1, 2, 3, 4], 3, True)
        self.assert_search([5, 1, 2, 3, 4], 4, True)
        self.assert_search([5, 1, 2, 3, 4], 0, False)

    def test_rotate_mid(self):
        self.assert_search([3, 4, 5, 1, 2], 1, True)
        self.assert_search([3, 4, 5, 1, 2], 2, True)
        self.assert_search([3, 4, 5, 1, 2], 3, True)
        self.assert_search([3, 4, 5, 1, 2], 5, True)
        self.assert_search([3, 4, 5, 1, 2], 0, False)
        self.assert_search([3, 4, 5, 1, 2], 6, False)

    def test_target_at_pivot_boundary(self):
        self.assert_search([6, 7, 0, 1, 2, 4, 5], 6, True)
        self.assert_search([6, 7, 0, 1, 2, 4, 5], 0, True)
        self.assert_search([11, 13, 15, 17, 5, 7, 9], 9, True)
        self.assert_search([11, 13, 15, 17, 5, 7, 9], 11, True)

    def test_all_duplicates_found(self):
        self.assert_search([2, 2, 2, 2, 2], 2, True)

    def test_all_duplicates_absent(self):
        self.assert_search([2, 2, 2, 2, 2], 1, False)

    def test_duplicates_around_target(self):
        self.assert_search([1, 0, 1, 1, 1], 0, True)

    def test_duplicates_target_absent(self):
        self.assert_search([1, 0, 1, 1, 1], 2, False)

    def test_duplicates_heavy(self):
        self.assert_search([1, 1, 1, 0, 1], 0, True)
        self.assert_search([1, 1, 1, 0, 1], 2, False)
        self.assert_search([1, 3, 1, 1, 1, 2, 1], 3, True)
        self.assert_search([1, 3, 1, 1, 1, 2, 1], 2, True)
        self.assert_search([1, 3, 1, 1, 1, 2, 1], 4, False)

    def test_leetcode_example_large(self):
        nums = [4, 5, 6, 6, 7, 0, 1, 2, 4, 4]
        self.assert_search(nums, 0, True)
        self.assert_search(nums, 7, True)
        self.assert_search(nums, 3, False)

    def test_negative_numbers(self):
        self.assert_search([-1, -3, -5, -7, -9], -5, True)
        self.assert_search([-10, -3, -2, -1, 0, 5], -2, True)
        self.assert_search([-10, -3, -2, -1, 0, 5], -4, False)

    def test_mixed_sign_rotated(self):
        self.assert_search([-3, -1, 2, 5, 6, -5], -3, True)
        self.assert_search([-3, -1, 2, 5, 6, -5], -5, True)
        self.assert_search([-3, -1, 2, 5, 6, -5], 0, False)

    def test_boundary_values(self):
        self.assert_search([-10000, 10000], -10000, True)
        self.assert_search([10000, -10000], 10000, True)
        self.assert_search([10000, -10000], 0, False)

    def test_randomized_bruteforce(self):
        import random

        random.seed(42)
        for _ in range(200):
            base = sorted(random.randint(-5, 5) for _ in range(random.randint(1, 12)))
            k = random.randint(0, len(base) - 1)
            nums = base[k:] + base[:k]
            if random.random() < 0.7:
                target = random.choice(base)
            else:
                target = random.randint(-7, 7)
            expected = target in nums
            self.assertEqual(
                self.solution.search(nums, target),
                expected,
                f"failed on nums={nums}, target={target}",
            )

# Tags: Array, Binary Search
