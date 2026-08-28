# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Medium

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


def combos(result):
    return sorted(map(tuple, result))


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            combos(self.sol.combinationSum([2, 3, 6, 7], 7)),
            [(2, 2, 3), (7,)],
        )

    def test_example2(self):
        self.assertEqual(
            combos(self.sol.combinationSum([2, 3, 5], 8)),
            [(2, 2, 2, 2), (2, 3, 3), (3, 5)],
        )

    def test_example3_no_solution(self):
        self.assertEqual(self.sol.combinationSum([2], 1), [])

    def test_single_candidate_match(self):
        self.assertEqual(self.sol.combinationSum([5], 5), [[5]])

    def test_single_candidate_reuse(self):
        self.assertEqual(self.sol.combinationSum([3], 9), [[3, 3, 3]])

    def test_single_candidate_unreachable(self):
        self.assertEqual(self.sol.combinationSum([3], 7), [])

    def test_target_reached_by_subsets(self):
        self.assertEqual(
            combos(self.sol.combinationSum([1, 2, 4], 4)),
            [(1, 1, 1, 1), (1, 1, 2), (2, 2), (4,)],
        )

    def test_unsorted_input(self):
        self.assertEqual(
            combos(self.sol.combinationSum([7, 6, 3, 2], 7)),
            [(2, 2, 3), (7,)],
        )

    def test_target_smaller_than_all_candidates(self):
        self.assertEqual(self.sol.combinationSum([5, 8, 9], 4), [])

    def test_target_one_min(self):
        self.assertEqual(self.sol.combinationSum([2, 3], 1), [])

    def test_single_composition_pairs(self):
        self.assertEqual(
            combos(self.sol.combinationSum([2, 4, 6], 10)),
            [(2, 2, 2, 2, 2), (2, 2, 2, 4), (2, 2, 6), (2, 4, 4), (4, 6)],
        )

    def test_one_element_equals_target(self):
        res = self.sol.combinationSum([10, 20, 40], 40)
        self.assertIn([40], res)
        self.assertIn([20, 20], res)
        self.assertIn([10, 10, 20], res)
        self.assertIn([10, 10, 10, 10], res)

    def test_repeated_smallest_target(self):
        self.assertEqual(
            self.sol.combinationSum([4], 12),
            [[4, 4, 4]],
        )

    def test_many_repeats(self):
        res = self.sol.combinationSum([1], 10)
        self.assertEqual(res, [[1] * 10])

    def test_all_sums_and_members_valid(self):
        cands = [2, 3, 6, 7]
        target = 15
        res = self.sol.combinationSum(cands, target)
        self.assertGreater(len(res), 0)
        for c in res:
            self.assertEqual(sum(c), target)
            for x in c:
                self.assertIn(x, cands)
            self.assertEqual(c, sorted(c))
        self.assertEqual(len(set(map(tuple, res))), len(res))

    def test_no_duplicate_combinations(self):
        res = self.sol.combinationSum([2, 3], 6)
        combos_set = set(map(tuple, res))
        self.assertEqual(len(combos_set), len(res))
        self.assertEqual(combos(res), [(2, 2, 2), (3, 3)])

    def test_large_target_multiple_options(self):
        res = self.sol.combinationSum([2, 40], 40)
        self.assertEqual(
            combos(res),
            [(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), (40,)],
        )

    def test_two_equal_repeats(self):
        self.assertEqual(self.sol.combinationSum([5], 10), [[5, 5]])

    def test_empty_result_kept_empty(self):
        res = self.sol.combinationSum([6, 7, 8], 5)
        self.assertEqual(res, [])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Backtracking
