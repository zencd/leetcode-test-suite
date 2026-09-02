# 481. Magical String
# https://leetcode.com/problems/magical-string/
# Medium

class Solution:
    def magicalString(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.magicalString(6), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.magicalString(1), 1)

    def test_small_values(self):
        self.assertEqual(self.sol.magicalString(2), 1)
        self.assertEqual(self.sol.magicalString(3), 1)
        self.assertEqual(self.sol.magicalString(4), 2)
        self.assertEqual(self.sol.magicalString(5), 3)
        self.assertEqual(self.sol.magicalString(7), 4)
        self.assertEqual(self.sol.magicalString(8), 4)
        self.assertEqual(self.sol.magicalString(9), 4)
        self.assertEqual(self.sol.magicalString(10), 5)
        self.assertEqual(self.sol.magicalString(11), 5)
        self.assertEqual(self.sol.magicalString(12), 5)
        self.assertEqual(self.sol.magicalString(13), 6)
        self.assertEqual(self.sol.magicalString(14), 7)
        self.assertEqual(self.sol.magicalString(15), 7)
        self.assertEqual(self.sol.magicalString(16), 8)
        self.assertEqual(self.sol.magicalString(17), 9)
        self.assertEqual(self.sol.magicalString(18), 9)

    def test_against_reference_prefix(self):
        reference = "122112122122112112212112122112112122122112122121121122122112122122112112122121122122112122122112112"
        for n in [10, 37, len(reference)]:
            expected = reference[:n].count("1")
            self.assertEqual(self.sol.magicalString(n), expected)

    def test_property_group_runs_match_prefix(self):
        s = [1, 2, 2]
        k = 2
        while len(s) < 300:
            nxt = 3 - s[-1]
            s.extend([nxt] * s[k])
            k += 1
        groups = []
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                groups.append(cnt)
                cnt = 1
        groups.append(cnt)
        self.assertEqual(groups[:100], s[:100])

    def test_large_value(self):
        self.assertEqual(self.sol.magicalString(100000), 49972)

    def test_zero_returns_zero(self):
        self.assertEqual(self.sol.magicalString(0), 0)

    def test_count_never_exceeds_n(self):
        for n in [1, 2, 3, 5, 10, 100, 1000]:
            c = self.sol.magicalString(n)
            self.assertLessEqual(c, n)
            self.assertGreaterEqual(c, 0)

    def test_monotonic_non_decreasing(self):
        prev = 0
        for n in range(1, 60):
            c = self.sol.magicalString(n)
            self.assertGreaterEqual(c, prev)
            prev = c


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String
