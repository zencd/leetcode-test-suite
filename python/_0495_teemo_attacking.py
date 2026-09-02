# 495. Teemo Attacking
# https://leetcode.com/problems/teemo-attacking/
# Easy

from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1_separated_attacks(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 4], 2), 4)

    def test_example2_overlapping_attacks(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 2], 2), 3)

    def test_single_attack(self):
        self.assertEqual(self.s.findPoisonedDuration([0], 5), 5)

    def test_duration_zero(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 2, 3], 0), 0)

    def test_duration_zero_single_attack(self):
        self.assertEqual(self.s.findPoisonedDuration([100], 0), 0)

    def test_adjacent_attacks_full_overlap(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 2, 3], 10), 12)

    def test_duplicate_attack_times(self):
        self.assertEqual(self.s.findPoisonedDuration([5, 5, 5], 3), 3)

    def test_attack_exactly_at_poison_end(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 3], 2), 4)

    def test_attack_one_before_poison_end(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 3], 3), 5)

    def test_zero_start_time(self):
        self.assertEqual(self.s.findPoisonedDuration([0, 1], 2), 3)

    def test_many_separated_attacks(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 10, 20, 30], 3), 12)

    def test_many_overlapping_attacks(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 2, 3, 4, 5], 10), 14)

    def test_mixed_overlap_and_gap(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 2, 10], 3), 7)

    def test_large_duration_fully_covers(self):
        self.assertEqual(self.s.findPoisonedDuration([1, 2, 3], 10**7), 10**7 + 2)

    def test_single_zero_attack_zero_duration(self):
        self.assertEqual(self.s.findPoisonedDuration([0], 0), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Simulation
