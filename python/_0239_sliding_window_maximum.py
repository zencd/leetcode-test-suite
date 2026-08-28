# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/
# Hard

from collections import deque
from typing import List
import unittest


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        raise Exception("Not solved yet")


def reference_max_sliding_window(nums: List[int], k: int) -> List[int]:
    return [max(nums[i : i + k]) for i in range(len(nums) - k + 1)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7],
        )

    def test_example2_single_element(self):
        self.assertEqual(self.sol.maxSlidingWindow([1], 1), [1])

    def test_k_equals_n(self):
        self.assertEqual(self.sol.maxSlidingWindow([4, 2, 9, 1], 4), [9])
        self.assertEqual(self.sol.maxSlidingWindow([-5, 2, -1, 0], 4), [2])

    def test_k_one(self):
        self.assertEqual(
            self.sol.maxSlidingWindow([7, -2, 0, 5, 3], 1),
            [7, -2, 0, 5, 3],
        )

    def test_all_equal(self):
        self.assertEqual(self.sol.maxSlidingWindow([5, 5, 5, 5], 2), [5, 5, 5])

    def test_all_negative(self):
        self.assertEqual(
            self.sol.maxSlidingWindow([-4, -2, -9, -1, -3], 3),
            [-2, -1, -1],
        )

    def test_mixed_signs(self):
        self.assertEqual(
            self.sol.maxSlidingWindow([-2, 3, 1, -5, 4, 0], 2),
            [3, 3, 1, 4, 4],
        )

    def test_ascending(self):
        self.assertEqual(self.sol.maxSlidingWindow([1, 2, 3, 4, 5], 3), [3, 4, 5])

    def test_descending(self):
        self.assertEqual(self.sol.maxSlidingWindow([5, 4, 3, 2, 1], 3), [5, 4, 3])

    def test_window_leaves_max_only_end(self):
        self.assertEqual(
            self.sol.maxSlidingWindow([9, 1, 2, 3, 4], 3),
            [9, 3, 4],
        )

    def test_max_entering_only_end(self):
        self.assertEqual(
            self.sol.maxSlidingWindow([3, 1, 2, 0, 11], 3),
            [3, 2, 11],
        )

    def test_single_negative(self):
        self.assertEqual(self.sol.maxSlidingWindow([-7], 1), [-7])

    def test_two_elements(self):
        self.assertEqual(self.sol.maxSlidingWindow([2, 8], 2), [8])
        self.assertEqual(self.sol.maxSlidingWindow([8, 2], 1), [8, 2])

    def test_matches_reference_random_cases(self):
        import random

        random.seed(239)
        for _ in range(50):
            n = random.randint(1, 30)
            nums = [random.randint(-100, 100) for _ in range(n)]
            k = random.randint(1, n)
            self.assertEqual(
                self.sol.maxSlidingWindow(nums, k),
                reference_max_sliding_window(nums, k),
            )

    def test_large_random_against_reference(self):
        import random

        random.seed(7)
        for _ in range(5):
            n = random.randint(1000, 2000)
            nums = [random.randint(-(10**4), 10**4) for _ in range(n)]
            for k in (1, 2, n // 2, n - 1, n):
                self.assertEqual(
                    self.sol.maxSlidingWindow(nums, k),
                    reference_max_sliding_window(nums, k),
                )

    def test_large_ascending(self):
        nums = list(range(10000))
        self.assertEqual(
            self.sol.maxSlidingWindow(nums, 9999),
            [9998, 9999],
        )

    def test_large_descending(self):
        nums = list(range(10000, 0, -1))
        self.assertEqual(
            self.sol.maxSlidingWindow(nums, 9999),
            [10000, 9999],
        )

    def test_returns_new_list(self):
        nums = [1, 3, -1]
        out = self.sol.maxSlidingWindow(nums, 2)
        self.assertIsNot(out, nums)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue, Range Minimum/Maximum Query
