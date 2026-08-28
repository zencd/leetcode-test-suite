# 274. H-Index
# https://leetcode.com/problems/h-index/
# Medium

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.hIndex([3, 0, 6, 1, 5]), 3)

    def test_example2(self):
        self.assertEqual(self.sol.hIndex([1, 3, 1]), 1)

    def test_single_paper_zero(self):
        self.assertEqual(self.sol.hIndex([0]), 0)

    def test_single_paper_one(self):
        self.assertEqual(self.sol.hIndex([1]), 1)

    def test_single_paper_high(self):
        self.assertEqual(self.sol.hIndex([1000]), 1)

    def test_all_zeros(self):
        self.assertEqual(self.sol.hIndex([0, 0, 0, 0]), 0)

    def test_all_ones(self):
        self.assertEqual(self.sol.hIndex([1, 1, 1, 1]), 1)

    def test_all_high_citations(self):
        self.assertEqual(self.sol.hIndex([10, 10, 10, 10]), 4)

    def test_exceeding_citations(self):
        self.assertEqual(self.sol.hIndex([100, 200, 300]), 3)

    def test_two_papers(self):
        self.assertEqual(self.sol.hIndex([0, 1]), 1)

    def test_two_papers_both_cited(self):
        self.assertEqual(self.sol.hIndex([2, 2]), 2)

    def test_one_cited_twice(self):
        self.assertEqual(self.sol.hIndex([1, 2]), 1)

    def test_mixed_values(self):
        self.assertEqual(self.sol.hIndex([2, 1, 3, 0]), 2)

    def test_boundary_h_equals_n(self):
        self.assertEqual(self.sol.hIndex([3, 3, 3]), 3)

    def test_h_less_than_n(self):
        self.assertEqual(self.sol.hIndex([100, 0, 0, 0, 0]), 1)

    def test_large_citations_small_n(self):
        self.assertEqual(self.sol.hIndex([1000, 1000, 1000, 1000, 1000]), 5)

    def test_sorted_ascending(self):
        self.assertEqual(self.sol.hIndex([1, 2, 3, 4, 5]), 3)

    def test_sorted_descending(self):
        self.assertEqual(self.sol.hIndex([5, 4, 3, 2, 1]), 3)

    def test_only_one_high_rest_zero(self):
        self.assertEqual(self.sol.hIndex([1000, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 1)

    def test_all_at_least_half(self):
        n = 4
        citations = [2] * n
        self.assertEqual(self.sol.hIndex(citations), 2)

    def test_zero_first(self):
        self.assertEqual(self.sol.hIndex([0, 2, 3, 4]), 2)

    def test_large_input(self):
        n = 5000
        citations = [i % 1001 for i in range(n)]
        result = self.sol.hIndex(citations)
        papers_at_least_h = sum(1 for c in citations if c >= result)
        self.assertTrue(papers_at_least_h >= result)
        if result < n:
            papers_at_least_h1 = sum(1 for c in citations if c >= result + 1)
            self.assertTrue(papers_at_least_h1 < result + 1)

    def test_two_hundreds(self):
        self.assertEqual(self.sol.hIndex([1, 1, 1, 1, 1, 1, 1, 2]), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Sorting, Counting Sort
