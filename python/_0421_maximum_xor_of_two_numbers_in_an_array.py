# 421. Maximum XOR of Two Numbers in an Array
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# Medium

from typing import List
import unittest


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_first_example(self):
        self.assertEqual(self.sol.findMaximumXOR([3, 10, 5, 25, 2, 8]), 28)

    def test_second_example(self):
        nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
        self.assertEqual(self.sol.findMaximumXOR(nums), 127)

    def test_single_element(self):
        self.assertEqual(self.sol.findMaximumXOR([5]), 0)

    def test_two_elements(self):
        self.assertEqual(self.sol.findMaximumXOR([1, 2]), 3)

    def test_two_same_elements(self):
        self.assertEqual(self.sol.findMaximumXOR([7, 7]), 0)

    def test_all_zeros(self):
        self.assertEqual(self.sol.findMaximumXOR([0, 0, 0]), 0)

    def test_zero_and_one(self):
        self.assertEqual(self.sol.findMaximumXOR([0, 1]), 1)

    def test_negative_not_allowed_but_large_values(self):
        self.assertEqual(self.sol.findMaximumXOR([1, 2, 3]), 3)

    def test_max_constraint_value(self):
        nums = [2**31 - 1, 2**31 - 2]
        self.assertEqual(self.sol.findMaximumXOR(nums), 1)

    def test_all_max_value(self):
        self.assertEqual(self.sol.findMaximumXOR([2**31 - 1] * 3), 0)

    def test_zero_with_max_value(self):
        self.assertEqual(self.sol.findMaximumXOR([0, 2**31 - 1]), 2**31 - 1)

    def test_duplicates_do_not_affect(self):
        nums = [3, 3, 3, 10, 10, 5]
        self.assertEqual(self.sol.findMaximumXOR(nums), 15)

    def test_known_pair(self):
        self.assertEqual(self.sol.findMaximumXOR([8, 1, 2, 12, 15, 24, 25, 5]), 29)

    def test_three_elements_known(self):
        self.assertEqual(self.sol.findMaximumXOR([10, 5, 25]), 28)

    def test_large_array(self):
        import random

        random.seed(0)
        n = 2 * 10**5
        nums = [random.randint(0, 2**31 - 1) for _ in range(n)]

        def brute_or_verify(max_x):
            for _ in range(10000):
                a = random.randrange(n)
                b = random.randrange(n)
                self.assertLessEqual(nums[a] ^ nums[b], max_x if max_x is not None else nums[a] ^ nums[b])

        result = self.sol.findMaximumXOR(nums)
        best = 0
        for a in nums[:2000]:
            for b in nums[:2000]:
                best = max(best, a ^ b)
        self.assertGreaterEqual(result, best)
        brute_or_verify(result)

    def test_two_power_of_two(self):
        self.assertEqual(self.sol.findMaximumXOR([8, 16]), 24)

    def test_sequential_numbers(self):
        self.assertEqual(self.sol.findMaximumXOR([1, 2, 3, 4]), 7)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Bit Manipulation, Trie
