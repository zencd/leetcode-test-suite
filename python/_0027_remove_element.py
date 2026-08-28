# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Easy

from typing import List
import unittest


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        raise Exception("Not solved yet")


class TestRemoveElement(unittest.TestCase):
    def test_example1(self):
        nums = [3, 2, 2, 3]
        k = Solution().removeElement(nums, 3)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2, 2])

    def test_example2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = Solution().removeElement(nums, 2)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0, 0, 1, 3, 4])

    def test_empty_array(self):
        nums = []
        k = Solution().removeElement(nums, 1)
        self.assertEqual(k, 0)
        self.assertEqual(nums, [])

    def test_all_removed(self):
        nums = [5, 5, 5, 5]
        k = Solution().removeElement(nums, 5)
        self.assertEqual(k, 0)

    def test_single_element_kept(self):
        nums = [7]
        k = Solution().removeElement(nums, 3)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:1], [7])

    def test_single_element_removed(self):
        nums = [7]
        k = Solution().removeElement(nums, 7)
        self.assertEqual(k, 0)

    def test_val_not_in_array(self):
        nums = [1, 2, 3]
        k = Solution().removeElement(nums, 4)
        self.assertEqual(k, 3)
        self.assertEqual(nums, [1, 2, 3])

    def test_val_at_beginning(self):
        nums = [2, 1, 2, 3, 4]
        k = Solution().removeElement(nums, 2)
        self.assertEqual(k, 3)
        self.assertEqual(sorted(nums[:k]), [1, 3, 4])

    def test_val_at_end(self):
        nums = [1, 3, 4, 2]
        k = Solution().removeElement(nums, 2)
        self.assertEqual(k, 3)
        self.assertEqual(sorted(nums[:k]), [1, 3, 4])

    def test_val_in_middle(self):
        nums = [1, 2, 3]
        k = Solution().removeElement(nums, 2)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [1, 3])

    def test_duplicates_of_val(self):
        nums = [2, 2, 2]
        k = Solution().removeElement(nums, 2)
        self.assertEqual(k, 0)

    def test_duplicates_of_others(self):
        nums = [1, 1, 1, 2]
        k = Solution().removeElement(nums, 2)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [1, 1, 1])

    def test_all_elements_equal_kept(self):
        nums = [9, 9, 9]
        k = Solution().removeElement(nums, 0)
        self.assertEqual(k, 3)
        self.assertEqual(nums, [9, 9, 9])

    def test_zero_val(self):
        nums = [0, 1, 0, 2, 0]
        k = Solution().removeElement(nums, 0)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [1, 2])

    def test_in_place_preservation(self):
        nums = [3, 2, 2, 3]
        original_id = id(nums)
        Solution().removeElement(nums, 3)
        self.assertEqual(id(nums), original_id)

    def test_max_values(self):
        nums = [50] * 100
        k = Solution().removeElement(nums, 100)
        self.assertEqual(k, 100)
        self.assertEqual(nums, [50] * 100)

    def test_max_range_all_removed(self):
        nums = list(range(51))
        k = Solution().removeElement(nums, 0)
        self.assertEqual(k, 50)
        self.assertEqual(sorted(nums[:k]), list(range(1, 51)))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers
