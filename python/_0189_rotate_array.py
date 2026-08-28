# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Medium

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.sol.rotate(nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_example2(self):
        nums = [-1, -100, 3, 99]
        self.sol.rotate(nums, 2)
        self.assertEqual(nums, [3, 99, -1, -100])

    def test_single_element(self):
        nums = [42]
        self.sol.rotate(nums, 0)
        self.assertEqual(nums, [42])

    def test_single_element_k_positive(self):
        nums = [7]
        self.sol.rotate(nums, 5)
        self.assertEqual(nums, [7])

    def test_k_zero(self):
        nums = [1, 2, 3, 4]
        self.sol.rotate(nums, 0)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_k_greater_than_length(self):
        nums = [1, 2, 3, 4, 5]
        self.sol.rotate(nums, 8)
        self.assertEqual(nums, [3, 4, 5, 1, 2])

    def test_k_equals_length(self):
        nums = [1, 2, 3]
        self.sol.rotate(nums, 3)
        self.assertEqual(nums, [1, 2, 3])

    def test_k_much_larger_than_length(self):
        nums = [1, 2, 3, 4, 5, 6]
        self.sol.rotate(nums, 100000)
        self.assertEqual(nums, [3, 4, 5, 6, 1, 2])

    def test_two_elements_k_odd(self):
        nums = [1, 2]
        self.sol.rotate(nums, 3)
        self.assertEqual(nums, [2, 1])

    def test_two_elements_k_even(self):
        nums = [9, 5]
        self.sol.rotate(nums, 2)
        self.assertEqual(nums, [9, 5])

    def test_negative_values(self):
        nums = [-1, -2, -3, -4, -5]
        self.sol.rotate(nums, 2)
        self.assertEqual(nums, [-4, -5, -1, -2, -3])

    def test_mixed_signs(self):
        nums = [0, -5, 10, -1]
        self.sol.rotate(nums, 1)
        self.assertEqual(nums, [-1, 0, -5, 10])

    def test_large_values(self):
        nums = [-2147483648, 2147483647, 0]
        self.sol.rotate(nums, 1)
        self.assertEqual(nums, [0, -2147483648, 2147483647])

    def test_full_rotation_k1(self):
        nums = list(range(10))
        self.sol.rotate(nums, 1)
        self.assertEqual(nums, [9] + list(range(9)))

    def test_duplicates(self):
        nums = [3, 3, 3, 1, 3]
        self.sol.rotate(nums, 2)
        self.assertEqual(nums, [1, 3, 3, 3, 3])

    def test_all_same(self):
        nums = [8, 8, 8]
        self.sol.rotate(nums, 2)
        self.assertEqual(nums, [8, 8, 8])

    def test_returns_none(self):
        nums = [1, 2, 3]
        result = self.sol.rotate(nums, 1)
        self.assertIsNone(result)
        self.assertEqual(nums, [3, 1, 2])

    def test_modifies_in_place(self):
        nums = [1, 2, 3, 4, 5]
        original_id = id(nums)
        self.sol.rotate(nums, 2)
        self.assertEqual(id(nums), original_id)
        self.assertEqual(nums, [4, 5, 1, 2, 3])

    def test_large_array_consistency(self):
        nums = list(range(100001))
        k = 12345
        expected = nums[-k:] + nums[:-k]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, expected)

    def test_many_rotations_accumulate(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        for i in range(1, 4):
            self.sol.rotate(nums, i)
        self.assertEqual(nums, [2, 3, 4, 5, 6, 7, 1])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Two Pointers
