# 275. H-Index II
# https://leetcode.com/problems/h-index-ii/
# Medium

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.hIndex([0, 1, 3, 5, 6]), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.hIndex([1, 2, 100]), 2)

    def test_single_zero(self):
        self.assertEqual(self.sol.hIndex([0]), 0)

    def test_single_positive(self):
        self.assertEqual(self.sol.hIndex([1]), 1)

    def test_all_zeros(self):
        self.assertEqual(self.sol.hIndex([0, 0, 0, 0]), 0)

    def test_all_ones(self):
        self.assertEqual(self.sol.hIndex([1, 1, 1, 1]), 1)

    def test_all_same_citations(self):
        self.assertEqual(self.sol.hIndex([3, 3, 3, 3]), 3)

    def test_all_huge_citations(self):
        self.assertEqual(self.sol.hIndex([1000, 1000, 1000]), 3)

    def test_two_papers(self):
        self.assertEqual(self.sol.hIndex([0, 1]), 1)

    def test_two_papers_positive(self):
        self.assertEqual(self.sol.hIndex([1, 2]), 1)

    def test_sorted_ascending(self):
        self.assertEqual(self.sol.hIndex([1, 2, 3, 4, 5]), 3)

    def test_duplicates(self):
        self.assertEqual(self.sol.hIndex([0, 0, 1, 1, 1, 2, 3, 4]), 2)

    def test_large_value_at_end(self):
        self.assertEqual(self.sol.hIndex([0, 0, 0, 200]), 1)

    def test_max_citations_all(self):
        self.assertEqual(self.sol.hIndex([200, 200, 200, 200]), 4)

    def test_no_papers_qualify(self):
        self.assertEqual(self.sol.hIndex([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 1)

    def test_half_papers(self):
        self.assertEqual(self.sol.hIndex([0, 0, 0, 5]), 1)

    def test_threshold_at_index_0(self):
        self.assertEqual(self.sol.hIndex([5, 5, 5, 5]), 4)

    def test_threshold_at_last_index(self):
        self.assertEqual(self.sol.hIndex([0, 0, 0, 1]), 1)

    def test_random_case_a(self):
        self.assertEqual(self.sol.hIndex([0, 1, 3, 4, 4, 4]), 3)

    def test_random_case_b(self):
        self.assertEqual(self.sol.hIndex([0, 1, 1, 2, 4, 5]), 2)

    def test_random_case_c(self):
        self.assertEqual(self.sol.hIndex([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search
