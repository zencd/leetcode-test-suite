# 315. Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# Hard

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_element(self):
        self.assertEqual(self.sol.countSmaller([-1]), [0])
        self.assertEqual(self.sol.countSmaller([7]), [0])
        self.assertEqual(self.sol.countSmaller([0]), [0])

    def test_examples(self):
        self.assertEqual(self.sol.countSmaller([5, 2, 6, 1]), [2, 1, 1, 0])
        self.assertEqual(self.sol.countSmaller([-1]), [0])
        self.assertEqual(self.sol.countSmaller([-1, -1]), [0, 0])

    def test_all_equal(self):
        self.assertEqual(self.sol.countSmaller([3, 3, 3]), [0, 0, 0])
        self.assertEqual(self.sol.countSmaller([0, 0]), [0, 0])
        self.assertEqual(self.sol.countSmaller([-5, -5, -5, -5]), [0, 0, 0, 0])

    def test_strictly_increasing(self):
        self.assertEqual(self.sol.countSmaller([1, 2, 3, 4]), [0, 0, 0, 0])

    def test_strictly_decreasing(self):
        self.assertEqual(self.sol.countSmaller([4, 3, 2, 1]), [3, 2, 1, 0])
        self.assertEqual(self.sol.countSmaller([2, 1]), [1, 0])

    def test_two_elements(self):
        self.assertEqual(self.sol.countSmaller([1, 2]), [0, 0])
        self.assertEqual(self.sol.countSmaller([2, 1]), [1, 0])

    def test_duplicates_mixed(self):
        self.assertEqual(self.sol.countSmaller([1, 0, 1]), [1, 0, 0])
        self.assertEqual(self.sol.countSmaller([2, 2, 1, 2]), [1, 1, 0, 0])
        self.assertEqual(self.sol.countSmaller([1, 2, 1, 1]), [0, 2, 0, 0])
        self.assertEqual(self.sol.countSmaller([4, 4, 4, 2, 4]), [1, 1, 1, 0, 0])

    def test_negative_values(self):
        self.assertEqual(self.sol.countSmaller([-5, -2, -10, 0]), [1, 1, 0, 0])
        self.assertEqual(self.sol.countSmaller([-5, -2, -10]), [1, 1, 0])
        self.assertEqual(self.sol.countSmaller([-1, -2, -3]), [2, 1, 0])

    def test_boundary_values(self):
        self.assertEqual(self.sol.countSmaller([-(10**4), 10**4, 0]), [0, 1, 0])
        self.assertEqual(self.sol.countSmaller([10**4, -(10**4), 10**4]), [1, 0, 0])
        self.assertEqual(
            self.sol.countSmaller([-(10**4), -(10**4), 10**4, -(10**4)]),
            [0, 0, 1, 0],
        )

    def test_does_not_mutate_input(self):
        nums = [5, 2, 6, 1]
        copy = list(nums)
        self.sol.countSmaller(nums)
        self.assertEqual(nums, copy)

    def test_returns_new_list(self):
        out1 = self.sol.countSmaller([5, 2, 6, 1])
        out2 = self.sol.countSmaller([5, 2, 6, 1])
        self.assertIsNot(out1, out2)
        self.assertEqual(out1, out2)

    def test_random_against_reference(self):
        import random

        random.seed(42)
        for _ in range(40):
            n = random.randint(1, 50)
            nums = [random.randint(-15, 15) for _ in range(n)]
            expected = [
                sum(1 for j in range(i + 1, len(nums)) if nums[j] < nums[i])
                for i in range(len(nums))
            ]
            self.assertEqual(
                self.sol.countSmaller(nums), expected, msg=f"failed on nums={nums}"
            )

    def test_large_input_against_reference(self):
        import random

        random.seed(1)
        n = 1000
        nums = [random.randint(-(10**4), 10**4) for _ in range(n)]
        expected = [
            sum(1 for j in range(i + 1, n) if nums[j] < nums[i]) for i in range(n)
        ]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_large_input_worst_case_sorted(self):
        import random

        random.seed(7)
        n = 10_000
        pool = [-(10**4), 0, 10**4]
        nums = [random.choice(pool) for _ in range(n)]
        expected = [
            sum(1 for j in range(i + 1, n) if nums[j] < nums[i]) for i in range(n)
        ]
        self.assertEqual(self.sol.countSmaller(nums), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set, Treap
