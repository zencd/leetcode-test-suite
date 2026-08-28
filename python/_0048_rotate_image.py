# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/
# Medium

import unittest
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        raise Exception("Not solved yet")


class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def rotate(self, matrix):
        self.sol.rotate(matrix)
        return matrix

    def test_1x1(self):
        self.assertEqual(self.rotate([[5]]), [[5]])

    def test_example_1(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.rotate(m), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_example_2(self):
        m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        self.assertEqual(
            self.rotate(m),
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        )

    def test_2x2(self):
        self.assertEqual(self.rotate([[1, 2], [3, 4]]), [[3, 1], [4, 2]])

    def test_negative_values(self):
        self.assertEqual(self.rotate([[-1, -2], [-3, -4]]), [[-3, -1], [-4, -2]])

    def test_zero_values(self):
        m = [[0, 0], [0, 1]]
        self.assertEqual(self.rotate(m), [[0, 0], [1, 0]])

    def test_extreme_values(self):
        m = [[-1000, 1000], [0, -1]]
        self.assertEqual(self.rotate(m), [[0, -1000], [-1, 1000]])

    def test_in_place_modification(self):
        m = [[1, 2], [3, 4]]
        self.sol.rotate(m)
        self.assertEqual(m, [[3, 1], [4, 2]])

    def test_return_value_is_none(self):
        self.assertIsNone(self.sol.rotate([[1]]))

    def test_rotation_idempotency_four_times(self):
        original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        backup = [row[:] for row in original]
        for _ in range(4):
            self.sol.rotate(original)
        self.assertEqual(original, backup)

    def test_two_rotations_equal_180(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.sol.rotate(m)
        self.sol.rotate(m)
        self.assertEqual(m, [[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    def test_larger_4x4(self):
        m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        self.assertEqual(self.rotate(m), expected)

    def test_duplicates(self):
        self.assertEqual(
            self.rotate([[7, 7, 7], [7, 7, 7], [7, 7, 8]]),
            [[7, 7, 7], [7, 7, 7], [8, 7, 7]],
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Matrix
