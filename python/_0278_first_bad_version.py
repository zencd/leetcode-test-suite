# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/
# Easy

class Solution:
    def firstBadVersion(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self._bad = 1

        def isBadVersion(version):
            return version >= self._bad

        globals()["isBadVersion"] = isBadVersion
        self.sol = Solution()

    def test_bad_at_start(self):
        self._bad = 1
        self.assertEqual(self.sol.firstBadVersion(1), 1)

    def test_bad_at_start_larger(self):
        self._bad = 1
        self.assertEqual(self.sol.firstBadVersion(10), 1)

    def test_bad_at_end(self):
        self._bad = 5
        self.assertEqual(self.sol.firstBadVersion(5), 5)

    def test_bad_at_end_large(self):
        self._bad = 2**31 - 1
        self.assertEqual(self.sol.firstBadVersion(2**31 - 1), 2**31 - 1)

    def test_bad_in_middle(self):
        self._bad = 3
        self.assertEqual(self.sol.firstBadVersion(7), 3)

    def test_example_one(self):
        self._bad = 4
        self.assertEqual(self.sol.firstBadVersion(5), 4)

    def test_example_two(self):
        self._bad = 1
        self.assertEqual(self.sol.firstBadVersion(1), 1)

    def test_bad_second(self):
        self._bad = 2
        self.assertEqual(self.sol.firstBadVersion(3), 2)

    def test_bad_at_middle_even(self):
        self._bad = 4
        self.assertEqual(self.sol.firstBadVersion(8), 4)

    def test_two_versions(self):
        self._bad = 2
        self.assertEqual(self.sol.firstBadVersion(2), 2)

    def test_two_versions_bad_first(self):
        self._bad = 1
        self.assertEqual(self.sol.firstBadVersion(2), 1)

    def test_bad_near_upper_bound(self):
        self._bad = 2**31 - 2
        self.assertEqual(self.sol.firstBadVersion(2**31 - 1), 2**31 - 2)

    def test_bad_just_after_half(self):
        n = 100
        self._bad = 51
        self.assertEqual(self.sol.firstBadVersion(n), 51)

    def test_bad_just_before_half(self):
        n = 100
        self._bad = 50
        self.assertEqual(self.sol.firstBadVersion(n), 50)

    def test_minimal_n(self):
        self._bad = 1
        self.assertEqual(self.sol.firstBadVersion(1), 1)

    def test_minimal_api_calls(self):
        n = 2**31 - 1
        self._bad = n // 2
        calls = []

        def spy(version):
            calls.append(version)
            return version >= self._bad

        globals()["isBadVersion"] = spy
        self.assertEqual(self.sol.firstBadVersion(n), n // 2)
        self.assertLessEqual(len(calls), 31)

    def test_all_results_correct_for_all_bad_positions(self):
        for bad in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            self._bad = bad
            self.assertEqual(self.sol.firstBadVersion(10), bad)


if __name__ == "__main__":
    unittest.main()

# Tags: Binary Search, Interactive
