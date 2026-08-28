# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/
# Medium

import unittest
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        raise Exception("Not solved yet")


class TestCombinationSum2(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assertCombinationEqual(self, expected, actual) -> None:
        normalized_expected = sorted(tuple(c) for c in expected)
        normalized_actual = sorted(tuple(c) for c in actual)
        self.assertEqual(normalized_expected, normalized_actual)

    def test_example1(self) -> None:
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertCombinationEqual(
            expected, self.solution.combinationSum2(candidates, target)
        )

    def test_example2(self) -> None:
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [[1, 2, 2], [5]]
        self.assertCombinationEqual(
            expected, self.solution.combinationSum2(candidates, target)
        )

    def test_single_element_match(self) -> None:
        candidates = [5]
        target = 5
        self.assertCombinationEqual(
            [[5]], self.solution.combinationSum2(candidates, target)
        )

    def test_single_element_no_match(self) -> None:
        candidates = [5]
        target = 3
        self.assertCombinationEqual(
            [], self.solution.combinationSum2(candidates, target)
        )

    def test_no_combination_possible(self) -> None:
        candidates = [3, 4, 5]
        target = 2
        self.assertCombinationEqual(
            [], self.solution.combinationSum2(candidates, target)
        )

    def test_all_duplicates(self) -> None:
        candidates = [2, 2, 2]
        target = 4
        self.assertCombinationEqual(
            [[2, 2]], self.solution.combinationSum2(candidates, target)
        )

    def test_all_three_duplicates(self) -> None:
        candidates = [2, 2, 2]
        target = 6
        self.assertCombinationEqual(
            [[2, 2, 2]], self.solution.combinationSum2(candidates, target)
        )

    def test_two_ones_make_two(self) -> None:
        candidates = [1, 1]
        target = 2
        self.assertCombinationEqual(
            [[1, 1]], self.solution.combinationSum2(candidates, target)
        )

    def test_two_twos_make_four(self) -> None:
        candidates = [2, 2]
        target = 4
        self.assertCombinationEqual(
            [[2, 2]], self.solution.combinationSum2(candidates, target)
        )

    def test_pair_and_single(self) -> None:
        candidates = [2, 2, 1]
        target = 4
        self.assertCombinationEqual(
            [[2, 2]], self.solution.combinationSum2(candidates, target)
        )

    def test_target_equal_single_duplicate(self) -> None:
        candidates = [3, 3, 3]
        target = 3
        self.assertCombinationEqual(
            [[3]], self.solution.combinationSum2(candidates, target)
        )

    def test_target_exceeds_sum(self) -> None:
        candidates = [1, 2, 3]
        target = 10
        self.assertCombinationEqual(
            [], self.solution.combinationSum2(candidates, target)
        )

    def test_target_one_with_many_ones(self) -> None:
        candidates = [1, 1, 1]
        target = 1
        self.assertCombinationEqual(
            [[1]], self.solution.combinationSum2(candidates, target)
        )

    def test_all_ones_target_three(self) -> None:
        candidates = [1, 1, 1, 1]
        target = 3
        self.assertCombinationEqual(
            [[1, 1, 1]], self.solution.combinationSum2(candidates, target)
        )

    def test_all_ones_insufficient(self) -> None:
        candidates = [1, 1, 1]
        target = 4
        self.assertCombinationEqual(
            [], self.solution.combinationSum2(candidates, target)
        )

    def test_unsorted_input(self) -> None:
        candidates = [7, 3, 5, 1, 9, 2, 4]
        target = 9
        expected = [[2, 7], [4, 5], [9], [1, 3, 5], [2, 3, 4]]
        self.assertCombinationEqual(
            expected, self.solution.combinationSum2(candidates, target)
        )

    def test_large_values(self) -> None:
        candidates = [50] * 5 + [1] * 50
        target = 30
        self.assertCombinationEqual(
            [[1] * 30], self.solution.combinationSum2(candidates, target)
        )

    def test_mixed_sizes(self) -> None:
        candidates = [30, 30, 15]
        target = 30
        self.assertCombinationEqual(
            [[30]], self.solution.combinationSum2(candidates, target)
        )

    def test_target_ten_from_one_to_ten(self) -> None:
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 10
        expected = [
            [1, 9],
            [2, 8],
            [3, 7],
            [4, 6],
            [1, 2, 7],
            [1, 3, 6],
            [1, 4, 5],
            [2, 3, 5],
            [1, 2, 3, 4],
            [10],
        ]
        self.assertCombinationEqual(
            expected, self.solution.combinationSum2(candidates, target)
        )

    def test_input_not_mutated(self) -> None:
        candidates = [10, 1, 2, 7, 6, 1, 5]
        original = list(candidates)
        self.solution.combinationSum2(candidates, 8)
        self.assertEqual(original, candidates)

    def test_no_duplicate_combinations_in_output(self) -> None:
        candidates = [1, 1, 1, 1, 2, 2, 3, 3]
        target = 6
        result = self.solution.combinationSum2(candidates, target)
        serialized = [tuple(c) for c in result]
        self.assertEqual(len(serialized), len(set(serialized)))
        self.assertTrue(all(sum(c) == target for c in result))
        self.assertCombinationEqual(
            [[1, 1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 2, 2], [1, 2, 3], [3, 3]], result
        )

    def test_every_valid_combination_present(self) -> None:
        candidates = [1, 2, 3, 4, 5]
        target = 7
        expected = [[3, 4], [2, 5], [1, 2, 4]]
        self.assertCombinationEqual(
            expected, self.solution.combinationSum2(candidates, target)
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Backtracking
