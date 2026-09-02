# 491. Non-decreasing Subsequences
# https://leetcode.com/problems/non-decreasing-subsequences/
# Medium

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        nums = [4, 6, 7, 7]
        expected = [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
        self.assertEqual(sorted(self.sol.findSubsequences(nums), key=repr), sorted(expected, key=repr))

    def test_example2(self):
        nums = [4, 4, 3, 2, 1]
        expected = [[4, 4]]
        self.assertEqual(self.sol.findSubsequences(nums), expected)

    def test_single_element(self):
        self.assertEqual(self.sol.findSubsequences([5]), [])

    def test_two_identical(self):
        self.assertEqual(self.sol.findSubsequences([1, 1]), [[1, 1]])

    def test_two_increasing(self):
        self.assertEqual(self.sol.findSubsequences([1, 2]), [[1, 2]])

    def test_two_decreasing(self):
        self.assertEqual(self.sol.findSubsequences([2, 1]), [])

    def test_all_equal(self):
        nums = [3, 3, 3]
        expected = [[3, 3], [3, 3, 3]]
        self.assertEqual(sorted(self.sol.findSubsequences(nums), key=repr), sorted(expected, key=repr))

    def test_no_duplicates_expected(self):
        nums = [1, 2, 1]
        out = self.sol.findSubsequences(nums)
        reps = [tuple(s) for s in out]
        self.assertEqual(len(reps), len(set(reps)))
        for s in out:
            self.assertTrue(len(s) >= 2)
            for a, b in zip(s, s[1:]):
                self.assertLessEqual(a, b)

    def test_negative_numbers(self):
        nums = [-1, -2, -1]
        out = self.sol.findSubsequences(nums)
        reps = [tuple(s) for s in out]
        self.assertEqual(len(reps), len(set(reps)))
        self.assertIn((-2, -1), reps)

    def test_mixed_signs(self):
        nums = [-2, 0, 2, 0, 2]
        out = self.sol.findSubsequences(nums)
        reps = [tuple(s) for s in out]
        self.assertEqual(len(reps), len(set(reps)))
        for s in out:
            self.assertTrue(len(s) >= 2)
            for a, b in zip(s, s[1:]):
                self.assertLessEqual(a, b)

    def test_max_length_sorted(self):
        nums = list(range(1, 16))
        out = self.sol.findSubsequences(nums)
        expected_count = 2**15 - 1 - 15
        self.assertEqual(len(out), expected_count)

    def test_min_max_values(self):
        nums = [-100, 100]
        self.assertEqual(self.sol.findSubsequences(nums), [[-100, 100]])

    def test_duplicates_all(self):
        nums = [2, 2, 2]
        out = self.sol.findSubsequences(nums)
        self.assertEqual(out, [[2, 2], [2, 2, 2]])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Backtracking, Bit Manipulation
