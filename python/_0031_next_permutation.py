# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/
# Medium

import unittest
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        raise Exception("Not solved yet")


class NextPermutationTest(unittest.TestCase):
    def make(self, nums):
        sol = Solution()
        sol.nextPermutation(nums)
        return nums

    def test_example_1(self):
        self.assertEqual(self.make([1, 2, 3]), [1, 3, 2])

    def test_example_2(self):
        self.assertEqual(self.make([3, 2, 1]), [1, 2, 3])

    def test_example_3(self):
        self.assertEqual(self.make([1, 1, 5]), [1, 5, 1])

    def test_single_element(self):
        self.assertEqual(self.make([7]), [7])

    def test_two_elements_ascending(self):
        self.assertEqual(self.make([1, 2]), [2, 1])

    def test_two_elements_descending(self):
        self.assertEqual(self.make([2, 1]), [1, 2])

    def test_two_elements_equal(self):
        self.assertEqual(self.make([5, 5]), [5, 5])

    def test_already_sorted(self):
        self.assertEqual(self.make([1, 2, 3, 4, 5]), [1, 2, 3, 5, 4])

    def test_reverse_sorted(self):
        self.assertEqual(self.make([9, 8, 7, 6, 5]), [5, 6, 7, 8, 9])

    def test_all_equal(self):
        self.assertEqual(self.make([3, 3, 3, 3]), [3, 3, 3, 3])

    def test_duplicates(self):
        self.assertEqual(self.make([1, 5, 1]), [5, 1, 1])

    def test_duplicate_descending_tail(self):
        self.assertEqual(self.make([1, 3, 2, 2, 1]), [2, 1, 1, 2, 3])

    def test_zeros(self):
        self.assertEqual(self.make([0, 0]), [0, 0])

    def test_zero_mixed(self):
        self.assertEqual(self.make([1, 0, 1]), [1, 1, 0])

    def test_max_values(self):
        self.assertEqual(self.make([100, 100, 100]), [100, 100, 100])

    def test_in_place_mutation(self):
        nums = [1, 2, 3]
        sol = Solution()
        result = sol.nextPermutation(nums)
        self.assertIsNone(result)
        self.assertEqual(nums, [1, 3, 2])

    def test_full_cycle_permutations_of_three(self):
        order = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        for i in range(len(order)):
            with self.subTest(current=order[i]):
                expected_next = order[(i + 1) % len(order)]
                self.assertEqual(self.make(list(order[i])), expected_next)

    def test_bruteforce_random(self):
        import random
        from itertools import permutations as perms

        random.seed(42)
        for _ in range(200):
            size = random.randint(1, 6)
            nums = [random.randint(0, 3) for _ in range(size)]
            original = list(nums)
            all_perms = [list(p) for p in set(perms(original))]
            all_perms.sort()
            idx = all_perms.index(original)
            expected_next = all_perms[(idx + 1) % len(all_perms)]
            self.assertEqual(
                self.make(nums), expected_next, msg=f"input was {original}"
            )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers
