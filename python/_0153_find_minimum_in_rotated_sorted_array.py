# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Medium

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_examples(self):
        self.assertEqual(self.sol.findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(self.sol.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(self.sol.findMin([11, 13, 15, 17]), 11)

    def test_single_element(self):
        self.assertEqual(self.sol.findMin([1]), 1)
        self.assertEqual(self.sol.findMin([0]), 0)
        self.assertEqual(self.sol.findMin([-5]), -5)

    def test_two_elements_rotated(self):
        self.assertEqual(self.sol.findMin([2, 1]), 1)
        self.assertEqual(self.sol.findMin([5, 3]), 3)

    def test_two_elements_unrotated(self):
        self.assertEqual(self.sol.findMin([1, 2]), 1)
        self.assertEqual(self.sol.findMin([3, 4]), 3)

    def test_rotation_at_first_position(self):
        self.assertEqual(self.sol.findMin([1, 2, 3, 4]), 1)
        self.assertEqual(self.sol.findMin([5, 6, 7, 8, 9]), 5)

    def test_rotation_at_last_position(self):
        self.assertEqual(self.sol.findMin([2, 3, 4, 1]), 1)
        self.assertEqual(self.sol.findMin([6, 7, 8, 9, 5]), 5)

    def test_rotation_in_middle(self):
        self.assertEqual(self.sol.findMin([5, 1, 2, 3, 4]), 1)
        self.assertEqual(self.sol.findMin([3, 4, 5, 6, 1, 2]), 1)

    def test_negative_numbers(self):
        self.assertEqual(self.sol.findMin([-3, -2, -1, 0, 1]), -3)
        self.assertEqual(self.sol.findMin([0, 1, -3, -2, -1]), -3)

    def test_all_negative_rotated(self):
        self.assertEqual(self.sol.findMin([-1, -5, -4, -3, -2]), -5)

    def test_zero_and_positive(self):
        self.assertEqual(self.sol.findMin([1, 2, 3, 0]), 0)
        self.assertEqual(self.sol.findMin([0, 1, 2, 3]), 0)

    def test_larger_array(self):
        rotated = list(range(10, 100)) + list(range(0, 10))
        self.assertEqual(self.sol.findMin(rotated), 0)

    def test_random_rotations_sorted_copy(self):
        nums = [9, 7, 5, 3, 1, 11, 13, 15, 17]
        base = sorted(nums)
        for k in range(len(base)):
            rotated = base[k:] + base[:k]
            self.assertEqual(self.sol.findMin(rotated), base[0])

    def test_min_at_index_zero(self):
        self.assertEqual(self.sol.findMin([4]), 4)
        self.assertEqual(self.sol.findMin([1, 2, 3]), 1)

    def test_min_at_last_index(self):
        self.assertEqual(self.sol.findMin([2, 1]), 1)
        self.assertEqual(self.sol.findMin([3, 4, 5, 1]), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search
