# 401. Binary Watch
# https://leetcode.com/problems/binary-watch/
# Easy

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_turned_on_0(self):
        self.assertEqual(self.sol.readBinaryWatch(0), ["0:00"])

    def test_turned_on_1(self):
        expected = [
            "0:01",
            "0:02",
            "0:04",
            "0:08",
            "0:16",
            "0:32",
            "1:00",
            "2:00",
            "4:00",
            "8:00",
        ]
        self.assertEqual(sorted(self.sol.readBinaryWatch(1)), sorted(expected))

    def test_turned_on_9_empty(self):
        self.assertEqual(self.sol.readBinaryWatch(9), [])

    def test_turned_on_10_empty(self):
        self.assertEqual(self.sol.readBinaryWatch(10), [])

    def test_order_independent(self):
        for t in range(9):
            self.assertEqual(
                sorted(self.sol.readBinaryWatch(t)),
                sorted(self.sol.readBinaryWatch(t)),
            )

    def test_no_duplicate_times(self):
        for t in range(9):
            res = self.sol.readBinaryWatch(t)
            self.assertEqual(len(res), len(set(res)))

    def test_partition_covers_all_valid_times(self):
        all_times = set()
        for t in range(9):
            for s in self.sol.readBinaryWatch(t):
                h, m = s.split(":")
                self.assertLess(int(h), 12)
                self.assertLess(int(m), 60)
                self.assertNotIn(s, all_times)
                expected_bits = bin(int(h)).count("1") + bin(int(m)).count("1")
                self.assertEqual(expected_bits, t, f"{s} has {expected_bits} bits but listed under t={t}")
                all_times.add(s)
        self.assertEqual(len(all_times), 720)

    def test_minutes_two_digits_format(self):
        for s in self.sol.readBinaryWatch(1):
            h, m = s.split(":")
            self.assertEqual(len(m), 2)
            self.assertTrue(m.isdigit())
            self.assertEqual(h, str(int(h)), "hour must not have leading zero")

    def test_specific_values(self):
        self.assertIn("0:00", self.sol.readBinaryWatch(0))
        self.assertIn("11:59", self.sol.readBinaryWatch(9 + 0) if False else self.sol.readBinaryWatch(bin(11).count("1") + bin(59).count("1")))
        self.assertIn("10:30", self.sol.readBinaryWatch(bin(10).count("1") + bin(30).count("1")))
        self.assertIn("11:00", self.sol.readBinaryWatch(bin(11).count("1")))
        self.assertIn("0:59", self.sol.readBinaryWatch(bin(59).count("1")))

    def test_counts(self):
        self.assertEqual(len(self.sol.readBinaryWatch(0)), 1)
        self.assertEqual(len(self.sol.readBinaryWatch(1)), 10)
        self.assertEqual(len(self.sol.readBinaryWatch(2)), 44)
        self.assertEqual(len(self.sol.readBinaryWatch(3)), 112)
        self.assertEqual(len(self.sol.readBinaryWatch(4)), 181)
        self.assertEqual(len(self.sol.readBinaryWatch(5)), 190)
        self.assertEqual(len(self.sol.readBinaryWatch(6)), 126)
        self.assertEqual(len(self.sol.readBinaryWatch(7)), 48)
        self.assertEqual(len(self.sol.readBinaryWatch(8)), 8)
        self.assertEqual(len(self.sol.readBinaryWatch(9)), 0)
        self.assertEqual(len(self.sol.readBinaryWatch(10)), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Backtracking, Bit Manipulation
