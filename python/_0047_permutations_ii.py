# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/
# Medium

from typing import List
import unittest


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        raise Exception("Not solved yet")


class TestPermuteUnique(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(Solution().permuteUnique([1]), [[1]])

    def test_two_distinct(self):
        self.assertEqual(Solution().permuteUnique([1, 2]), [[1, 2], [2, 1]])

    def test_two_same(self):
        self.assertEqual(Solution().permuteUnique([1, 1]), [[1, 1]])

    def test_example_1(self):
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertEqual(Solution().permuteUnique([1, 1, 2]), expected)

    def test_example_2(self):
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(Solution().permuteUnique([1, 2, 3]), expected)

    def test_all_same(self):
        self.assertEqual(Solution().permuteUnique([2, 2, 2]), [[2, 2, 2]])

    def test_negative_numbers(self):
        expected = [[-1, 0], [0, -1]]
        self.assertEqual(Solution().permuteUnique([-1, 0]), expected)

    def test_zero_and_duplicates(self):
        expected = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
        self.assertEqual(Solution().permuteUnique([0, 0, 1]), expected)

    def test_unsorted_input(self):
        result = Solution().permuteUnique([3, 1, 2])
        self.assertEqual(len(result), 6)
        self.assertEqual(
            sorted(result),
            sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        )

    def test_no_duplication_in_result(self):
        result = Solution().permuteUnique([1, 1, 1, 2])
        self.assertEqual(len(result), len(set(tuple(p) for p in result)))

    def test_max_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        result = Solution().permuteUnique(nums)
        self.assertEqual(len(result), 40320)
        self.assertTrue(all(sorted(p) == nums for p in result))

    def test_max_length_with_duplicates(self):
        nums = [1, 1, 2, 2, 3, 3, 4, 4]
        result = Solution().permuteUnique(nums)
        self.assertEqual(len(result), 2520)
        self.assertEqual(len(result), len(set(tuple(p) for p in result)))

    def test_boundary_values(self):
        result = Solution().permuteUnique([-10, 10])
        self.assertEqual(sorted(result), [[-10, 10], [10, -10]])

    def test_two_pairs_of_duplicates(self):
        result = Solution().permuteUnique([1, 1, 2, 2])
        self.assertEqual(len(result), 6)
        expected = [
            [1, 1, 2, 2],
            [1, 2, 1, 2],
            [1, 2, 2, 1],
            [2, 1, 1, 2],
            [2, 1, 2, 1],
            [2, 2, 1, 1],
        ]
        self.assertEqual(sorted(result), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Backtracking, Sorting
