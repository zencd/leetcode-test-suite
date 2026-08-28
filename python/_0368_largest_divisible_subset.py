# 368. Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/
# Medium

from typing import List
import unittest


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        raise Exception("Not solved yet")


def is_valid_subset(nums: List[int], ans: List[int]) -> bool:
    if not set(ans) <= set(nums):
        return False
    for i in range(len(ans)):
        for j in range(len(ans)):
            if i == j:
                continue
            if ans[i] % ans[j] != 0 and ans[j] % ans[i] != 0:
                return False
    return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def check(self, nums, expected_len=None):
        ans = self.sol.largestDivisibleSubset(nums)
        self.assertTrue(
            is_valid_subset(nums, ans), f"Invalid subset: {ans} from {nums}"
        )
        if expected_len is not None:
            self.assertEqual(len(ans), expected_len)
        return ans

    def test_example1(self):
        self.check([1, 2, 3], 2)

    def test_example2(self):
        self.check([1, 2, 4, 8], 4)

    def test_single_element(self):
        self.assertEqual(self.sol.largestDivisibleSubset([7]), [7])

    def test_empty(self):
        self.assertEqual(self.sol.largestDivisibleSubset([]), [])

    def test_two_elements_divisible(self):
        self.check([2, 4], 2)

    def test_two_elements_not_divisible(self):
        self.check([3, 5], 1)

    def test_all_primes(self):
        self.check([2, 3, 5, 7], 1)

    def test_unsorted_input(self):
        self.check([8, 4, 2, 1], 4)

    def test_complex_case(self):
        self.check([18, 4, 7, 6, 3], 3)

    def test_chain_with_branch(self):
        self.check([1, 2, 3, 4, 9], 3)

    def test_all_ones_not_possible_unique(self):
        self.check([6, 12, 24, 48, 96], 5)

    def test_larger_numbers(self):
        self.check([1000000000, 500000000, 250000000], 3)

    def test_no_common_divisibility(self):
        self.check([17, 23, 29, 31], 1)

    def test_mixed(self):
        self.check([2, 3, 5, 10, 15, 30], 3)

    def test_duplicate_free_random(self):
        self.check([1, 5, 2, 4, 6, 3], 3)

    def test_result_uses_elements_from_input(self):
        nums = [3, 6, 9, 18, 36, 72]
        ans = self.sol.largestDivisibleSubset(nums)
        for x in ans:
            self.assertIn(x, nums)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Dynamic Programming, Sorting
