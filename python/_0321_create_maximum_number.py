# 321. Create Maximum Number
# https://leetcode.com/problems/create-maximum-number/
# Hard

from typing import List


def select_k(nums: List[int], k: int) -> List[int]:
    stack = []
    drop = len(nums) - k
    for d in nums:
        while drop > 0 and stack and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)
    return stack[:k]


def is_greater(a: List[int], b: List[int]) -> bool:
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return a[i] > b[i]
    return len(a) > len(b)


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        raise Exception("Not solved yet")

    @staticmethod
    def merge(a: List[int], b: List[int]) -> List[int]:
        res = []
        i = j = 0
        while i < len(a) and j < len(b):
            if is_greater(a[i:], b[j:]):
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        res.extend(a[i:])
        res.extend(b[j:])
        return res


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5), [9, 8, 6, 5, 3]
        )

    def test_example2(self):
        self.assertEqual(self.sol.maxNumber([6, 7], [6, 0, 4], 5), [6, 7, 6, 0, 4])

    def test_example3(self):
        self.assertEqual(self.sol.maxNumber([3, 9], [8, 9], 3), [9, 8, 9])

    def test_take_all_from_one(self):
        self.assertEqual(self.sol.maxNumber([1], [2, 3], 3), [2, 3, 1])
        self.assertEqual(self.sol.maxNumber([9, 9, 9], [1, 2], 5), [9, 9, 9, 1, 2])
        self.assertEqual(self.sol.maxNumber([7, 1], [3, 2, 5], 3), [7, 5, 1])

    def test_k_equals_one(self):
        self.assertEqual(self.sol.maxNumber([3], [9], 1), [9])

    def test_k_single_from_empty_side(self):
        self.assertEqual(self.sol.maxNumber([5], [1], 1), [5])
        self.assertEqual(self.sol.maxNumber([1], [5], 1), [5])

    def test_order_preserved(self):
        self.assertEqual(
            self.sol.maxNumber([1, 2, 3], [4, 5, 6], 6), [4, 5, 6, 1, 2, 3]
        )

    def test_all_nines(self):
        self.assertEqual(self.sol.maxNumber([9, 9], [9, 9], 3), [9, 9, 9])

    def test_all_zeros_after_first(self):
        self.assertEqual(self.sol.maxNumber([1, 0, 0], [2, 0, 0], 4), [2, 1, 0, 0])
        self.assertEqual(self.sol.maxNumber([1, 0, 0], [2, 0, 0], 5), [2, 1, 0, 0, 0])

    def test_zeros_result(self):
        self.assertEqual(self.sol.maxNumber([1], [2], 1), [2])

    def test_pick_from_middle(self):
        self.assertEqual(self.sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 1), [9])

    def test_interleave_equal_prefix(self):
        self.assertEqual(self.sol.maxNumber([9, 8, 7], [9, 8, 6], 4), [9, 9, 8, 8])
        self.assertEqual(self.sol.maxNumber([2, 9], [8, 9], 2), [9, 9])
        self.assertEqual(self.sol.maxNumber([2, 9], [8], 2), [9, 8])

    def test_single_elements(self):
        self.assertEqual(self.sol.maxNumber([5], [5], 1), [5])

    def test_take_max_k_from_longer(self):
        self.assertEqual(self.sol.maxNumber([0], [9, 9, 9, 9], 2), [9, 9])

    def test_k_exceeds_one_array(self):
        nums1, nums2, k = [9, 8], [7, 6, 5, 4], 5
        self.assertEqual(self.sol.maxNumber(nums1, nums2, k), [9, 8, 7, 6, 5])

    def test_result_length_correct(self):
        nums1, nums2 = [1, 5, 3], [2, 4, 6]
        for k in range(1, 7):
            self.assertEqual(len(self.sol.maxNumber(nums1, nums2, k)), k)

    def test_optimality_small_random(self):
        import itertools

        def brute(nums1, nums2, k):
            best = None
            for t in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
                for c1 in itertools.combinations(range(len(nums1)), t):
                    for c2 in itertools.combinations(range(len(nums2)), k - t):
                        a = [nums1[i] for i in c1]
                        b = [nums2[i] for i in c2]
                        res = self.sol.merge(a, b)
                        val = int("".join(map(str, res)))
                        if best is None or val > best:
                            best = val
            return [int(ch) for ch in str(best)]

        cases = [
            ([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5),
            ([6, 7], [6, 0, 4], 5),
            ([3, 9], [8, 9], 3),
            ([7, 1], [3, 2, 5], 4),
            ([2, 2, 0], [3, 3, 1], 5),
            ([0, 1], [1, 0], 2),
        ]
        for n1, n2, k in cases:
            self.assertEqual(
                self.sol.maxNumber(n1, n2, k), brute(n1, n2, k), f"case {n1} {n2} {k}"
            )

    def test_helper_select_k(self):
        self.assertEqual(select_k([3, 4, 6, 5], 3), [4, 6, 5])
        self.assertEqual(select_k([9, 1, 2, 5], 2), [9, 5])
        self.assertEqual(select_k([1, 2, 3], 3), [1, 2, 3])
        self.assertEqual(select_k([3, 2, 1], 2), [3, 2])

    def test_helper_is_greater(self):
        self.assertTrue(is_greater([9, 8, 3], [9, 7, 4]))
        self.assertFalse(is_greater([9, 7, 4], [9, 8, 3]))
        self.assertTrue(is_greater([9, 9, 9, 9], [9, 9, 9, 8]))
        self.assertTrue(is_greater([9, 9], [9]))
        self.assertFalse(is_greater([9], [9, 9]))
        self.assertTrue(is_greater([1, 2], [1, 1]))

    def test_larger_input(self):
        nums1 = [1] * 20 + [9, 9, 9]
        nums2 = [9, 9] * 10
        res = self.sol.maxNumber(nums1, nums2, 15)
        self.assertEqual(len(res), 15)
        self.assertEqual(res[:6], [9, 9, 9, 9, 9, 9])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Stack, Greedy, Monotonic Stack
