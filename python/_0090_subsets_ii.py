# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/
# Medium

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSubsetsWithDup(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def compare(self, obtained: List[List[int]], expected: List[List[int]]) -> None:
        self.assertEqual(
            sorted(map(sorted, obtained)),
            sorted(map(sorted, expected)),
            f"Subsets mismatch.\nObtained: {obtained}\nExpected: {expected}",
        )

    def test_example_1(self) -> None:
        self.compare(
            self.solution.subsetsWithDup([1, 2, 2]),
            [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
        )

    def test_example_2(self) -> None:
        self.compare(self.solution.subsetsWithDup([0]), [[], [0]])

    def test_empty_array(self) -> None:
        self.compare(self.solution.subsetsWithDup([]), [[]])

    def test_single_element(self) -> None:
        self.compare(self.solution.subsetsWithDup([5]), [[], [5]])

    def test_no_duplicates(self) -> None:
        self.compare(
            self.solution.subsetsWithDup([1, 2, 3]),
            [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]],
        )

    def test_all_duplicates(self) -> None:
        self.compare(
            self.solution.subsetsWithDup([4, 4, 4]),
            [[], [4], [4, 4], [4, 4, 4]],
        )

    def test_duplicates_at_ends(self) -> None:
        self.compare(
            self.solution.subsetsWithDup([2, 3, 3, 2]),
            [[], [2], [2, 2], [2, 3], [2, 3, 3], [2, 2, 3], [3], [3, 3], [2, 2, 3, 3]],
        )

    def test_negative_numbers(self) -> None:
        self.compare(
            self.solution.subsetsWithDup([-1, -1, -2]),
            [[], [-1], [-1, -1], [-2], [-1, -2], [-1, -1, -2]],
        )

    def test_mixed_positive_and_negative(self) -> None:
        self.compare(
            self.solution.subsetsWithDup([-1, 0, 1]),
            [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]],
        )

    def test_max_length_array(self) -> None:
        obtained = self.solution.subsetsWithDup([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
        self.assertEqual(len(obtained), 3 * 3 * 3 * 3 * 3)

    def test_no_duplicate_subsets(self) -> None:
        obtained = self.solution.subsetsWithDup([1, 1, 2, 2])
        normalized = [tuple(sorted(subset)) for subset in obtained]
        self.assertEqual(len(normalized), len(set(normalized)))

    def test_result_contains_empty_subset(self) -> None:
        obtained = self.solution.subsetsWithDup([1, 2, 2])
        self.assertIn([], obtained)

    def test_subsets_contain_only_elements_from_input(self) -> None:
        source = [1, 2, 2]
        obtained = self.solution.subsetsWithDup(source)
        for subset in obtained:
            for value in subset:
                self.assertIn(value, source)

    def test_input_order_independence(self) -> None:
        first = self.solution.subsetsWithDup([1, 2, 2])
        second = self.solution.subsetsWithDup([2, 1, 2])
        self.assertEqual(
            sorted(map(sorted, first)),
            sorted(map(sorted, second)),
        )

    def test_input_not_relied_upon_sortedness(self) -> None:
        self.compare(
            self.solution.subsetsWithDup([3, 1, 3]),
            [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

# Tags: Array, Backtracking, Bit Manipulation
