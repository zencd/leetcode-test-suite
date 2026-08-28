# 264. Ugly Number II
# https://leetcode.com/problems/ugly-number-ii/
# Medium

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_n1(self):
        self.assertEqual(self.sol.nthUglyNumber(1), 1)

    def test_n2(self):
        self.assertEqual(self.sol.nthUglyNumber(2), 2)

    def test_n3(self):
        self.assertEqual(self.sol.nthUglyNumber(3), 3)

    def test_n4(self):
        self.assertEqual(self.sol.nthUglyNumber(4), 4)

    def test_n5(self):
        self.assertEqual(self.sol.nthUglyNumber(5), 5)

    def test_n6(self):
        self.assertEqual(self.sol.nthUglyNumber(6), 6)

    def test_n7(self):
        self.assertEqual(self.sol.nthUglyNumber(7), 8)

    def test_n8(self):
        self.assertEqual(self.sol.nthUglyNumber(8), 9)

    def test_n9(self):
        self.assertEqual(self.sol.nthUglyNumber(9), 10)

    def test_n10(self):
        self.assertEqual(self.sol.nthUglyNumber(10), 12)

    def test_n11(self):
        self.assertEqual(self.sol.nthUglyNumber(11), 15)

    def test_n15(self):
        self.assertEqual(self.sol.nthUglyNumber(15), 24)

    def test_n20(self):
        self.assertEqual(self.sol.nthUglyNumber(20), 36)

    def test_n30(self):
        self.assertEqual(self.sol.nthUglyNumber(30), 80)

    def test_n50(self):
        self.assertEqual(self.sol.nthUglyNumber(50), 243)

    def test_n169(self):
        self.assertEqual(self.sol.nthUglyNumber(169), 8748)

    def test_n170(self):
        self.assertEqual(self.sol.nthUglyNumber(170), 9000)

    def test_known_sequence_first_15(self):
        expected = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
        for i, expected_val in enumerate(expected, start=1):
            self.assertEqual(self.sol.nthUglyNumber(i), expected_val)

    def test_max_constraint(self):
        self.assertEqual(self.sol.nthUglyNumber(1690), 2123366400)

    def test_result_is_multiple_of_2_3_5(self):
        for n in (1, 7, 10, 100, 1690):
            val = self.sol.nthUglyNumber(n)
            while val % 2 == 0:
                val //= 2
            while val % 3 == 0:
                val //= 3
            while val % 5 == 0:
                val //= 5
            self.assertEqual(val, 1)

    def test_ugly_numbers_are_distinct_and_sorted(self):
        n = 50
        prev = 1
        for i in range(2, n + 1):
            cur = self.sol.nthUglyNumber(i)
            self.assertGreater(cur, prev)
            prev = cur


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Math, Dynamic Programming, Heap (Priority Queue)
