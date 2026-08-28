# 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/
# Hard

import unittest
from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        raise Exception("Not solved yet")


class TestGetPermutation(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(Solution().getPermutation(3, 3), "213")

    def test_example_2(self):
        self.assertEqual(Solution().getPermutation(4, 9), "2314")

    def test_example_3(self):
        self.assertEqual(Solution().getPermutation(3, 1), "123")

    def test_n_1(self):
        self.assertEqual(Solution().getPermutation(1, 1), "1")

    def test_n_2_first(self):
        self.assertEqual(Solution().getPermutation(2, 1), "12")

    def test_n_2_last(self):
        self.assertEqual(Solution().getPermutation(2, 2), "21")

    def test_n_3_all(self):
        expected = ["123", "132", "213", "231", "312", "321"]
        for k, exp in enumerate(expected, start=1):
            self.assertEqual(Solution().getPermutation(3, k), exp, f"k={k}")

    def test_n_4_first(self):
        self.assertEqual(Solution().getPermutation(4, 1), "1234")

    def test_n_4_last(self):
        self.assertEqual(Solution().getPermutation(4, 24), "4321")

    def test_n_4_boundary(self):
        self.assertEqual(Solution().getPermutation(4, 12), "2431")
        self.assertEqual(Solution().getPermutation(4, 13), "3124")

    def test_n_4_all(self):
        expected = [
            "1234",
            "1243",
            "1324",
            "1342",
            "1423",
            "1432",
            "2134",
            "2143",
            "2314",
            "2341",
            "2413",
            "2431",
            "3124",
            "3142",
            "3214",
            "3241",
            "3412",
            "3421",
            "4123",
            "4132",
            "4213",
            "4231",
            "4312",
            "4321",
        ]
        solution = Solution()
        for k, exp in enumerate(expected, start=1):
            self.assertEqual(solution.getPermutation(4, k), exp, f"k={k}")

    def test_n_9_first(self):
        self.assertEqual(Solution().getPermutation(9, 1), "123456789")

    def test_n_9_last(self):
        self.assertEqual(Solution().getPermutation(9, 362880), "987654321")

    def test_n_9_mid(self):
        result = Solution().getPermutation(9, 181440)
        self.assertEqual(sorted(result), [str(i) for i in range(1, 10)])

    def test_result_is_permutation(self):
        for n in range(1, 9):
            for k in (1, n // 2 + 1, factorial(n) // 2, factorial(n)):
                result = Solution().getPermutation(n, k)
                self.assertEqual(len(result), n)
                self.assertEqual(sorted(result), [str(i) for i in range(1, n + 1)])


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Recursion
