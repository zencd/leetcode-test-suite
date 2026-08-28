# 134. Gas Station
# https://leetcode.com/problems/gas-station/
# Medium

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3
        )

    def test_example_2(self):
        self.assertEqual(self.sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)

    def test_single_station_sufficient(self):
        self.assertEqual(self.sol.canCompleteCircuit([5], [1]), 0)

    def test_single_station_not_enough(self):
        self.assertEqual(self.sol.canCompleteCircuit([1], [2]), -1)

    def test_single_station_zero_cost(self):
        self.assertEqual(self.sol.canCompleteCircuit([0], [0]), 0)

    def test_single_station_zero_gas(self):
        self.assertEqual(self.sol.canCompleteCircuit([0], [1]), -1)

    def test_single_station_equal(self):
        self.assertEqual(self.sol.canCompleteCircuit([3], [3]), 0)

    def test_two_station_start_at_one(self):
        self.assertEqual(self.sol.canCompleteCircuit([1, 1], [2, 0]), 1)

    def test_two_station_start_at_zero(self):
        self.assertEqual(self.sol.canCompleteCircuit([2, 1], [1, 1]), 0)

    def test_two_station_impossible(self):
        self.assertEqual(self.sol.canCompleteCircuit([1, 1], [2, 2]), -1)

    def test_all_zero(self):
        self.assertEqual(self.sol.canCompleteCircuit([0, 0, 0], [0, 0, 0]), 0)

    def test_start_at_last_station(self):
        self.assertEqual(self.sol.canCompleteCircuit([0, 0, 5], [1, 1, 2]), 2)

    def test_equal_gas_and_cost(self):
        self.assertEqual(self.sol.canCompleteCircuit([2, 2, 2], [2, 2, 2]), 0)

    def test_large_values(self):
        self.assertEqual(self.sol.canCompleteCircuit([10000, 10000], [10000, 1]), 0)

    def test_unique_solution_middle(self):
        self.assertEqual(self.sol.canCompleteCircuit([3, 1, 1], [1, 2, 2]), 0)

    def test_brute_force_random(self):
        import random

        random.seed(42)
        for _ in range(200):
            n = random.randint(1, 8)
            gas = [random.randint(0, 5) for _ in range(n)]
            cost = [random.randint(0, 5) for _ in range(n)]
            expected = -1
            if sum(gas) >= sum(cost):
                for i in range(n):
                    tank = 0
                    ok = True
                    for j in range(n):
                        tank += gas[(i + j) % n] - cost[(i + j) % n]
                        if tank < 0:
                            ok = False
                            break
                    if ok:
                        expected = i
                        break
            self.assertEqual(self.sol.canCompleteCircuit(gas, cost), expected)

    def test_large_linear(self):
        n = 100000
        gas = [1] * n
        cost = list(range(1, n + 1))
        self.assertEqual(self.sol.canCompleteCircuit(gas, cost), -1)

    def test_large_solvable(self):
        n = 100000
        gas = [2] * n
        cost = [1] * n
        self.assertEqual(self.sol.canCompleteCircuit(gas, cost), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Greedy
