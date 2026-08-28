# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
# Easy

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertCountEqual(self.sol.intersection([1, 2, 2, 1], [2, 2]), [2])

    def test_example_2(self):
        self.assertCountEqual(self.sol.intersection([4, 9, 5], [9, 4, 9, 8, 4]), [9, 4])

    def test_no_common_elements(self):
        self.assertCountEqual(self.sol.intersection([1, 2, 3], [4, 5, 6]), [])

    def test_all_elements_common(self):
        self.assertCountEqual(self.sol.intersection([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_single_elements_both(self):
        self.assertCountEqual(self.sol.intersection([5], [5]), [5])

    def test_single_elements_different(self):
        self.assertCountEqual(self.sol.intersection([1], [2]), [])

    def test_duplicate_elements_in_both_arrays(self):
        self.assertCountEqual(self.sol.intersection([2, 2, 2], [2, 2]), [2])

    def test_zero_values(self):
        self.assertCountEqual(self.sol.intersection([0, 1], [0, 2]), [0])

    def test_zero_only(self):
        self.assertCountEqual(self.sol.intersection([0, 0], [0]), [0])

    def test_max_constraint_values(self):
        self.assertCountEqual(self.sol.intersection([1000], [0, 1000]), [1000])

    def test_result_contained_in_inputs(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [3, 5, 6, 7, 8]
        result = self.sol.intersection(nums1, nums2)
        self.assertCountEqual(result, [3, 5])
        for value in result:
            self.assertIn(value, nums1)
            self.assertIn(value, nums2)

    def test_result_is_unique(self):
        nums1 = [1, 1, 1, 2, 2, 2]
        nums2 = [1, 1, 2, 2, 3, 3]
        result = self.sol.intersection(nums1, nums2)
        self.assertCountEqual(result, [1, 2])
        self.assertEqual(len(result), len(set(result)))

    def test_symmetric(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [3, 4, 5, 6]
        self.assertCountEqual(
            self.sol.intersection(nums1, nums2), self.sol.intersection(nums2, nums1)
        )

    def test_large_arrays(self):
        nums1 = list(range(1000))
        nums2 = list(range(500, 1500))
        self.assertCountEqual(
            self.sol.intersection(nums1, nums2), list(range(500, 1000))
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Two Pointers, Binary Search, Sorting
