# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/
# Medium

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_one(self):
        self.assertEqual(self.solution.combinationSum3(3, 7), [[1, 2, 4]])

    def test_example_two(self):
        self.assertEqual(
            self.solution.combinationSum3(3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        )

    def test_example_three(self):
        self.assertEqual(self.solution.combinationSum3(4, 1), [])

    def test_no_solution_small_target(self):
        self.assertEqual(self.solution.combinationSum3(2, 1), [])
        self.assertEqual(self.solution.combinationSum3(3, 5), [])

    def test_k_two_various(self):
        self.assertEqual(self.solution.combinationSum3(2, 3), [[1, 2]])
        self.assertEqual(
            self.solution.combinationSum3(2, 10), [[1, 9], [2, 8], [3, 7], [4, 6]]
        )
        self.assertEqual(
            self.solution.combinationSum3(2, 11), [[2, 9], [3, 8], [4, 7], [5, 6]]
        )
        self.assertEqual(self.solution.combinationSum3(2, 12), [[3, 9], [4, 8], [5, 7]])
        self.assertEqual(self.solution.combinationSum3(2, 13), [[4, 9], [5, 8], [6, 7]])
        self.assertEqual(self.solution.combinationSum3(2, 14), [[5, 9], [6, 8]])
        self.assertEqual(self.solution.combinationSum3(2, 15), [[6, 9], [7, 8]])
        self.assertEqual(self.solution.combinationSum3(2, 3), [[1, 2]])
        self.assertEqual(self.solution.combinationSum3(2, 4), [[1, 3]])
        self.assertEqual(self.solution.combinationSum3(2, 7), [[1, 6], [2, 5], [3, 4]])

    def test_k_three(self):
        self.assertEqual(self.solution.combinationSum3(3, 6), [[1, 2, 3]])
        self.assertEqual(self.solution.combinationSum3(3, 8), [[1, 2, 5], [1, 3, 4]])
        self.assertEqual(
            self.solution.combinationSum3(3, 10),
            [[1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5]],
        )
        self.assertEqual(
            self.solution.combinationSum3(3, 11).__len__(),
            5,
        )
        self.assertEqual(
            self.solution.combinationSum3(3, 11),
            [[1, 2, 8], [1, 3, 7], [1, 4, 6], [2, 3, 6], [2, 4, 5]],
        )
        self.assertEqual(
            self.solution.combinationSum3(3, 15),
            [
                [1, 5, 9],
                [1, 6, 8],
                [2, 4, 9],
                [2, 5, 8],
                [2, 6, 7],
                [3, 4, 8],
                [3, 5, 7],
                [4, 5, 6],
            ],
        )

    def test_k_nine(self):
        self.assertEqual(self.solution.combinationSum3(9, 45), [list(range(1, 10))])
        self.assertEqual(self.solution.combinationSum3(9, 44), [])
        self.assertEqual(self.solution.combinationSum3(9, 46), [])
        self.assertEqual(self.solution.combinationSum3(9, 1), [])
        self.assertEqual(self.solution.combinationSum3(9, 60), [])

    def test_no_reuse_of_numbers(self):
        result = self.solution.combinationSum3(9, 45)
        self.assertEqual(len(result), 1)
        self.assertEqual(sorted(result[0]), list(range(1, 10)))

    def test_combinations_are_unique_and_sorted(self):
        result = self.solution.combinationSum3(3, 11)
        self.assertEqual(len(result), len({tuple(x) for x in result}))
        for combo in result:
            self.assertEqual(len(combo), 3)
            self.assertEqual(combo, sorted(combo))
            self.assertTrue(all(1 <= x <= 9 for x in combo))

    def test_all_combinations_sum_to_target(self):
        for k in range(2, 10):
            for n in range(1, 46):
                for combo in self.solution.combinationSum3(k, n):
                    self.assertEqual(sum(combo), n)
                    self.assertEqual(len(combo), k)

    def test_known_edge_targets(self):
        self.assertEqual(self.solution.combinationSum3(8, 36), [list(range(1, 9))])
        self.assertEqual(self.solution.combinationSum3(8, 44), [list(range(2, 10))])
        self.assertEqual(
            self.solution.combinationSum3(8, 37),
            [
                [1, 2, 3, 4, 5, 6, 7, 9],
            ],
        )
        self.assertEqual(self.solution.combinationSum3(8, 45), [])

    def test_two_number_minimum(self):
        self.assertEqual(self.solution.combinationSum3(2, 3), [[1, 2]])

    def test_large_target_impossible(self):
        self.assertEqual(self.solution.combinationSum3(2, 60), [])
        self.assertEqual(self.solution.combinationSum3(5, 60), [])

    def test_validity_property_across_range(self):
        for k in (2, 4, 6, 9):
            for n in range(1, 46):
                for combo in self.solution.combinationSum3(k, n):
                    self.assertEqual(sum(combo), n)
                    self.assertEqual(len(combo), k)
                    self.assertEqual(len(set(combo)), k)

    def test_expected_count(self):
        self.assertEqual(len(self.solution.combinationSum3(3, 11)), 5)
        self.assertEqual(len(self.solution.combinationSum3(4, 10)), 1)
        self.assertEqual(self.solution.combinationSum3(4, 10), [[1, 2, 3, 4]])
        self.assertEqual(len(self.solution.combinationSum3(5, 15)), 1)
        self.assertEqual(self.solution.combinationSum3(5, 15), [[1, 2, 3, 4, 5]])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Backtracking
