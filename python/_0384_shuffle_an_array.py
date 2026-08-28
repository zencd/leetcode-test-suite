# 384. Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/
# Medium

from typing import List
import random
import unittest


class Solution:
    def __init__(self, nums: List[int]):
        raise Exception("Not solved yet")

    def reset(self) -> List[int]:
        raise Exception("Not solved yet")

    def shuffle(self) -> List[int]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def test_init_preserves_input(self):
        nums = [1, 2, 3]
        Solution(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_init_single_element(self):
        s = Solution([42])
        self.assertEqual(s.reset(), [42])
        self.assertEqual(s.shuffle(), [42])

    def test_reset_returns_original(self):
        s = Solution([1, 2, 3])
        self.assertEqual(s.reset(), [1, 2, 3])

    def test_reset_after_shuffle_restores_original(self):
        s = Solution([1, 2, 3, 4])
        s.shuffle()
        self.assertEqual(s.reset(), [1, 2, 3, 4])
        self.assertEqual(s.reset(), [1, 2, 3, 4])

    def test_shuffle_returns_permutation(self):
        s = Solution([5, 6, 7, 8, 9])
        result = s.shuffle()
        self.assertEqual(sorted(result), [5, 6, 7, 8, 9])

    def test_shuffle_length_preserved(self):
        s = Solution([10, -20, 30])
        self.assertEqual(len(s.shuffle()), 3)

    def test_shuffle_handles_negatives(self):
        s = Solution([-1, -1000000, 0, 999999, 1000000])
        result = s.shuffle()
        self.assertEqual(sorted(result), [-1000000, -1, 0, 999999, 1000000])

    def test_shuffle_two_elements(self):
        s = Solution([1, 2])
        results = {tuple(s.shuffle()) for _ in range(100)}
        for r in results:
            self.assertEqual(sorted(r), [1, 2])
        self.assertTrue((1, 2) in results)

    def test_shuffle_all_permutations_reached(self):
        s = Solution([1, 2, 3])
        seen = set()
        for _ in range(2000):
            seen.add(tuple(s.shuffle()))
        self.assertEqual(
            seen, {(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)}
        )

    def test_shuffle_is_random_not_fixed(self):
        s = Solution([1, 2, 3, 4, 5])
        results = [list(s.shuffle()) for _ in range(100)]
        self.assertGreater(len({tuple(r) for r in results}), 1)

    def test_reset_independent_of_modified_returns(self):
        nums = [1, 2, 3]
        s = Solution(nums)
        r1 = s.reset()
        r1[0] = 999
        self.assertEqual(s.reset(), [1, 2, 3])
        r2 = s.shuffle()
        r2[0] = -999
        self.assertEqual(s.reset(), [1, 2, 3])

    def test_input_not_mutated_by_calls(self):
        nums = [1, 2, 3, 4]
        s = Solution(nums)
        for _ in range(20):
            s.shuffle()
            s.reset()
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_sequential_calls_order(self):
        s = Solution([1, 2, 3])
        s.shuffle()
        self.assertEqual(s.reset(), [1, 2, 3])
        s.shuffle()
        self.assertEqual(sorted(s.shuffle()), [1, 2, 3])
        self.assertEqual(s.reset(), [1, 2, 3])

    def test_max_length_boundary(self):
        nums = list(range(50))
        s = Solution(nums)
        result = s.shuffle()
        self.assertEqual(sorted(result), nums)
        self.assertEqual(s.reset(), nums)

    def test_many_calls(self):
        s = Solution([1, 2, 3, 4, 5])
        for _ in range(1000):
            result = s.shuffle()
            self.assertEqual(sorted(result), [1, 2, 3, 4, 5])
        self.assertEqual(s.reset(), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Design, Randomized
