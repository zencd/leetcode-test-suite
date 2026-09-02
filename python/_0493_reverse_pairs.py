# 493. Reverse Pairs
# https://leetcode.com/problems/reverse-pairs/
# Hard

from typing import List
import unittest


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


def _brute_force(nums: List[int]) -> int:
    return sum(1 for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] > 2 * nums[j])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assert_pairs(self, nums: List[int], expected: int) -> None:
        self.assertEqual(self.sol.reversePairs(nums), expected)

    def test_examples(self) -> None:
        self.assert_pairs([1, 3, 2, 3, 1], 2)
        self.assert_pairs([2, 4, 3, 5, 1], 3)

    def test_empty(self) -> None:
        self.assert_pairs([], 0)

    def test_single_element(self) -> None:
        self.assert_pairs([1], 0)
        self.assert_pairs([2**31 - 1], 0)
        self.assert_pairs([-(2**31)], 0)

    def test_two_elements(self) -> None:
        self.assert_pairs([3, 1], 1)
        self.assert_pairs([3, 2], 0)
        self.assert_pairs([1, 3], 0)
        self.assert_pairs([0, 1], 0)
        self.assert_pairs([-3, -1], 0)

    def test_all_equal(self) -> None:
        self.assert_pairs([5, 5, 5, 5], 0)
        self.assert_pairs([-7, -7, -7], 3)

    def test_all_zeros(self) -> None:
        self.assert_pairs([0, 0, 0, 0], 0)

    def test_no_reverse_pairs(self) -> None:
        self.assert_pairs([0, 1, 2, 3, 4], 0)
        self.assert_pairs([-5, -4, -3, -2, -1], 4)

    def test_negative_numbers(self) -> None:
        self.assert_pairs([-3, -2, -1], 1)
        self.assert_pairs([-2, -1, 0], 0)
        self.assert_pairs([-10, -1], 0)
        self.assert_pairs([-10, -10, -9], 3)

    def test_mixed_signs(self) -> None:
        self.assert_pairs([-5, -1, 3, 1], 1)
        self.assert_pairs([1, -1, 4, -2, 8], 4)
        self.assert_pairs([-(2**31), -(2**31), -(2**31) + 1], 3)

    def test_extreme_values(self) -> None:
        self.assert_pairs([2**31 - 1, -(2**31)], 1)
        self.assert_pairs([2**31 - 1, 2**31 - 1], 0)
        self.assert_pairs([-(2**31), 2**31 - 1], 0)

    def test_duplicates_with_pairs(self) -> None:
        self.assert_pairs([4, 2, 4, 1], 2)
        self.assert_pairs([2, 2, 2, 1, 1], 0)
        self.assert_pairs([10, 10, 10, 5, 5], 0)

    def test_descending(self) -> None:
        self.assert_pairs([5, 4, 3, 2, 1], 4)

    def test_known_manual_cases(self) -> None:
        self.assert_pairs([5, 3, 4, 3, 1], 4)
        self.assert_pairs([3, 1], 1)
        self.assert_pairs([1, 2], 0)

    def test_random_cases_against_brute_force(self) -> None:
        import random

        random.seed(493)
        for trial in range(200):
            n = random.randint(0, 30)
            hi = random.choice([3, 10, 10**6, 2**31 - 1])
            lo = random.choice([-hi, -(2**31), 0, hi // 2])
            nums = [random.randint(lo, hi) for _ in range(n)]
            self.assertEqual(
                self.sol.reversePairs(nums),
                _brute_force(nums),
                f"mismatch on {nums}",
            )

    def test_large_sorted_input(self) -> None:
        n = 50_000
        self.assertEqual(
            self.sol.reversePairs(
                list(range(1, n + 1)),
            ),
            0,
        )
        self.assertEqual(self.sol.reversePairs([-1] * n), n * (n - 1) // 2)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set, Treap
