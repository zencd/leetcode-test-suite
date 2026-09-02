# 324. Wiggle Sort II
# https://leetcode.com/problems/wiggle-sort-ii/
# Medium

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        raise Exception("Not solved yet")


import unittest


def check_wiggle(nums: List[int]) -> bool:
    if any(nums[i] >= nums[i + 1] for i in range(0, len(nums) - 1, 2)):
        return False
    if any(nums[i] <= nums[i + 1] for i in range(1, len(nums) - 1, 2)):
        return False
    return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        nums = [1, 5, 1, 1, 6, 4]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [1, 1, 1, 4, 5, 6])
        self.assertTrue(check_wiggle(nums))

    def test_example2(self):
        nums = [1, 3, 2, 2, 3, 1]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [1, 1, 2, 2, 3, 3])
        self.assertTrue(check_wiggle(nums))

    def test_single_element(self):
        nums = [42]
        self.sol.wiggleSort(nums)
        self.assertEqual(nums, [42])
        self.assertTrue(check_wiggle(nums))

    def test_two_elements(self):
        nums = [2, 1]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [1, 2])
        self.assertTrue(check_wiggle(nums))

    def test_two_elements_equal(self):
        nums = [3, 3]
        self.sol.wiggleSort(nums)
        self.assertEqual(nums, [3, 3])

    def test_third_example(self):
        nums = [3, 5, 2, 1, 6, 4]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [1, 2, 3, 4, 5, 6])
        self.assertTrue(check_wiggle(nums))

    def test_all_equal(self):
        nums = [7, 7, 7, 7, 7]
        self.sol.wiggleSort(nums)
        self.assertEqual(nums, [7, 7, 7, 7, 7])

    def test_sorted_input(self):
        nums = [1, 2, 3, 4, 5]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [1, 2, 3, 4, 5])
        self.assertTrue(check_wiggle(nums))

    def test_reverse_sorted_input(self):
        nums = [9, 7, 5, 3, 1]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [1, 3, 5, 7, 9])
        self.assertTrue(check_wiggle(nums))

    def test_three_elements(self):
        nums = [1, 2, 3]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [1, 2, 3])
        self.assertTrue(check_wiggle(nums))

    def test_heavy_duplicates(self):
        nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [1, 1, 1, 2, 2, 3, 3, 3, 3])
        self.assertTrue(check_wiggle(nums))

    def test_zeros_and_max(self):
        nums = [0, 5000, 0, 5000, 0, 5000]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [0, 0, 0, 5000, 5000, 5000])
        self.assertTrue(check_wiggle(nums))

    def test_even_length_descending_pairs(self):
        nums = [6, 5, 4, 3, 2, 1]
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), [1, 2, 3, 4, 5, 6])
        self.assertTrue(check_wiggle(nums))

    def test_large_random(self):
        import random

        random.seed(0)
        nums = [random.randint(0, 5000) for _ in range(50000)]
        expected = sorted(nums)
        self.sol.wiggleSort(nums)
        self.assertEqual(sorted(nums), expected)
        self.assertTrue(check_wiggle(nums))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Divide and Conquer, Greedy, Sorting, Quickselect
