# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Medium

from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(set(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)), {1, 2})

    def test_example2(self):
        self.assertEqual(Solution().topKFrequent([1], 1), [1])

    def test_example3(self):
        self.assertEqual(
            set(Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)), {1, 2}
        )

    def test_k_equals_all_unique(self):
        self.assertEqual(set(Solution().topKFrequent([1, 2, 3], 3)), {1, 2, 3})

    def test_single_element_k1(self):
        self.assertEqual(Solution().topKFrequent([7], 1), [7])

    def test_negative_numbers(self):
        self.assertEqual(
            set(Solution().topKFrequent([-1, -1, -1, 2, 2, 3], 2)), {-1, 2}
        )

    def test_all_same(self):
        self.assertEqual(Solution().topKFrequent([5, 5, 5, 5], 1), [5])

    def test_all_unique_k1(self):
        self.assertEqual(Solution().topKFrequent([1, 2, 3, 4], 1), [1])

    def test_tie_lower_frequency_excluded(self):
        self.assertEqual(set(Solution().topKFrequent([1, 1, 2, 2, 3, 4], 2)), {1, 2})

    def test_zero_in_array(self):
        self.assertEqual(set(Solution().topKFrequent([0, 0, 1, 1, 1, 2], 2)), {1, 0})

    def test_large_k(self):
        self.assertEqual(
            set(
                Solution().topKFrequent(
                    [1] * 10 + [2] * 5 + [3] * 3 + [4] * 2 + [5] * 1, 4
                )
            ),
            {1, 2, 3, 4},
        )

    def test_result_length(self):
        self.assertEqual(len(Solution().topKFrequent([1, 2, 3, 4, 5], 3)), 3)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
