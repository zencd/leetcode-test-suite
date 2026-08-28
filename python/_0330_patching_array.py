# 330. Patching Array
# https://leetcode.com/problems/patching-array/
# Hard

from typing import List
import unittest


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.minPatches([1, 3], 6), 1)
        self.assertEqual(self.sol.minPatches([1, 5, 10], 20), 2)
        self.assertEqual(self.sol.minPatches([1, 2, 2], 5), 0)

    def test_single_one_covers(self):
        self.assertEqual(self.sol.minPatches([1], 1), 0)
        self.assertEqual(self.sol.minPatches([1], 2), 1)
        self.assertEqual(self.sol.minPatches([1], 8), 3)

    def test_missing_one(self):
        self.assertEqual(self.sol.minPatches([2, 3], 6), 1)
        self.assertEqual(self.sol.minPatches([2], 1), 1)

    def test_no_patches_needed(self):
        self.assertEqual(self.sol.minPatches([1, 2, 3, 4], 10), 0)
        self.assertEqual(self.sol.minPatches([1, 2, 3, 4, 5], 15), 0)
        self.assertEqual(self.sol.minPatches([1, 2, 4, 8], 15), 0)

    def test_doubles(self):
        self.assertEqual(self.sol.minPatches([1, 1], 1), 0)
        self.assertEqual(self.sol.minPatches([1, 1], 2), 0)
        self.assertEqual(self.sol.minPatches([1, 1], 3), 1)

    def test_large_gaps(self):
        self.assertEqual(self.sol.minPatches([1, 100], 100), 6)
        self.assertEqual(self.sol.minPatches([1, 10000], 10000), 13)

    def test_large_n(self):
        self.assertEqual(self.sol.minPatches([1], 2**31 - 1), 30)
        self.assertEqual(
            self.sol.minPatches(
                [
                    1,
                    2,
                    4,
                    8,
                    16,
                    32,
                    64,
                    128,
                    256,
                    512,
                    1024,
                    2048,
                    4096,
                    8192,
                    16384,
                    32768,
                    65536,
                    131072,
                    262144,
                    524288,
                    1048576,
                    2097152,
                    4194304,
                    8388608,
                    16777216,
                    33554432,
                    67108864,
                    134217728,
                    268435456,
                    536870912,
                    1073741824,
                    2147483647,
                ],
                2**31 - 1,
            ),
            0,
        )

    def test_sorted_various(self):
        self.assertEqual(self.sol.minPatches([7, 8, 10, 11, 12, 13, 14], 2), 2)
        self.assertEqual(self.sol.minPatches([1, 2, 5], 4), 1)
        self.assertEqual(self.sol.minPatches([1, 3], 9), 2)

    def test_duplicates_large(self):
        self.assertEqual(self.sol.minPatches([2, 2, 2, 2, 2], 5), 1)
        self.assertEqual(self.sol.minPatches([1, 2, 2, 5], 15), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Greedy
