# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Medium

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(
            sorted(self.solution.threeSum([-1, 0, 1, 2, -1, -4])),
            [[-1, -1, 2], [-1, 0, 1]],
        )

    def test_example2(self):
        self.assertEqual(self.solution.threeSum([0, 1, 1]), [])

    def test_example3(self):
        self.assertEqual(self.solution.threeSum([0, 0, 0]), [[0, 0, 0]])

    def test_minimal_valid(self):
        self.assertEqual(self.solution.threeSum([0, 0, 0]), [[0, 0, 0]])

    def test_minimal_invalid(self):
        self.assertEqual(self.solution.threeSum([1, 2, 3]), [])

    def test_all_zeros(self):
        self.assertEqual(self.solution.threeSum([0, 0, 0, 0, 0]), [[0, 0, 0]])

    def test_multiple_triplets(self):
        self.assertEqual(
            sorted(self.solution.threeSum([3, -1, 1, -2, 2])),
            [[-2, -1, 3]],
        )

    def test_multiple_triplets2(self):
        self.assertEqual(
            self.solution.threeSum(
                [-40, -40, -30, -20, -10, 0, 10, 20, 40, 50, 60, 70]
            ),
            [
                [-40, -30, 70],
                [-40, -20, 60],
                [-40, -10, 50],
                [-40, 0, 40],
                [-30, -20, 50],
                [-30, -10, 40],
                [-30, 10, 20],
                [-20, 0, 20],
                [-10, 0, 10],
            ],
        )

    def test_duplicates_skipped(self):
        self.assertEqual(
            sorted(self.solution.threeSum([-2, 0, 0, 2, 2, 0, 0])),
            [[-2, 0, 2], [0, 0, 0]],
        )

    def test_no_solution(self):
        self.assertEqual(self.solution.threeSum([1, 2, 3, 4, 5]), [])

    def test_all_negative(self):
        self.assertEqual(self.solution.threeSum([-4, -3, -2, -1]), [])

    def test_all_positive(self):
        self.assertEqual(self.solution.threeSum([1, 2, 3, 4]), [])

    def test_mixed_with_triplet(self):
        self.assertEqual(self.solution.threeSum([-1, 2, -3, 4]), [[-3, -1, 4]])

    def test_mixed_with_no_triplet(self):
        self.assertEqual(self.solution.threeSum([-1, 2, -3, 5]), [])

    def test_two_triplets_with_shared_elements(self):
        self.assertEqual(
            sorted(self.solution.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 4])),
            [[-4, 0, 4], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
        )

    def test_triplet_from_negatives_and_positive(self):
        self.assertEqual(self.solution.threeSum([-1, -2, 3]), [[-2, -1, 3]])

    def test_large_values(self):
        self.assertEqual(self.solution.threeSum([-100000, 100000, 1]), [])

    def test_large_values_with_solution(self):
        self.assertEqual(
            sorted(self.solution.threeSum([-100000, 100000, -50000, 50000, 0])),
            [[-100000, 0, 100000], [-50000, 0, 50000]],
        )

    def test_sorted_output_within_triplets(self):
        result = self.solution.threeSum([1, -1, 0])
        for triplet in result:
            self.assertEqual(triplet, sorted(triplet))

    def test_result_triples_sum_to_zero(self):
        nums = [-1, 0, 1, 2, -1, -4, -2, 3]
        for triplet in self.solution.threeSum(nums):
            self.assertEqual(sum(triplet), 0)

    def test_duplicates_in_input(self):
        self.assertEqual(
            self.solution.threeSum([-1, -1, -1, 1, 1, 1, 0, 0, 0]),
            [[-1, 0, 1], [0, 0, 0]],
        )

    def test_exactly_three_elements(self):
        self.assertEqual(self.solution.threeSum([1, -1, 0]), [[-1, 0, 1]])

    def test_exactly_three_no_solution(self):
        self.assertEqual(self.solution.threeSum([1, 1, 2]), [])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Sorting
