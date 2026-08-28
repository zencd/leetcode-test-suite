# 332. Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
# Hard

from collections import defaultdict
from typing import List
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        self.assertEqual(
            self.sol.findItinerary(tickets), ["JFK", "MUC", "LHR", "SFO", "SJC"]
        )

    def test_example2(self):
        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
        self.assertEqual(
            self.sol.findItinerary(tickets), ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        )

    def test_single_ticket(self):
        tickets = [["JFK", "SFO"]]
        self.assertEqual(self.sol.findItinerary(tickets), ["JFK", "SFO"])

    def test_loop(self):
        tickets = [["JFK", "AAA"], ["AAA", "JFK"]]
        self.assertEqual(self.sol.findItinerary(tickets), ["JFK", "AAA", "JFK"])

    def test_lexicographic_order_of_choices(self):
        tickets = [["JFK", "ZZZ"], ["JFK", "AAA"], ["AAA", "BBB"], ["BBB", "JFK"]]
        self.assertEqual(
            self.sol.findItinerary(tickets), ["JFK", "AAA", "BBB", "JFK", "ZZZ"]
        )

    def test_multi_leg_chain(self):
        tickets = [["JFK", "AAA"], ["AAA", "BBB"], ["BBB", "CCC"], ["CCC", "DDD"]]
        self.assertEqual(
            self.sol.findItinerary(tickets), ["JFK", "AAA", "BBB", "CCC", "DDD"]
        )

    def test_return_to_jfk_branching(self):
        tickets = [["JFK", "AAA"], ["JFK", "BBB"], ["AAA", "JFK"], ["BBB", "JFK"]]
        self.assertEqual(
            self.sol.findItinerary(tickets), ["JFK", "AAA", "JFK", "BBB", "JFK"]
        )

    def test_nested_cycles(self):
        tickets = [
            ["JFK", "AAA"],
            ["JFK", "BBB"],
            ["AAA", "BBB"],
            ["BBB", "JFK"],
            ["BBB", "CCC"],
            ["CCC", "JFK"],
        ]
        result = self.sol.findItinerary(tickets)
        self.assertEqual(result[0], "JFK")
        self.assertEqual(len(result), 7)
        self.assertEqual(result, ["JFK", "AAA", "BBB", "CCC", "JFK", "BBB", "JFK"])

    def test_airport_names_of_different_lengths(self):
        tickets = [["JFK", "A"], ["A", "AA"], ["AA", "JFK"]]
        self.assertEqual(self.sol.findItinerary(tickets), ["JFK", "A", "AA", "JFK"])

    def test_all_tickets_used_exactly_once(self):
        tickets = [
            ["JFK", "ATL"],
            ["ATL", "LAX"],
            ["LAX", "JFK"],
            ["JFK", "SFO"],
            ["SFO", "ATL"],
        ]
        result = self.sol.findItinerary(tickets)
        self.assertEqual(len(result), len(tickets) + 1)
        from collections import Counter

        cnt = Counter((a, b) for a, b in zip(result, result[1:]))
        self.assertEqual(cnt, Counter(tuple(t) for t in tickets))

    def test_large_random_consistency(self):
        import random

        random.seed(42)
        airports = ["AAA", "BBB", "CCC", "DDD", "JFK", "EEE", "FFF"]
        tickets = []
        cur = "JFK"
        for _ in range(50):
            nxt = random.choice(airports)
            while nxt == cur:
                nxt = random.choice(airports)
            tickets.append([cur, nxt])
            cur = nxt
        random.shuffle(tickets)
        result = self.sol.findItinerary(tickets)
        self.assertEqual(len(result), 51)
        self.assertEqual(result[0], "JFK")
        from collections import Counter

        self.assertEqual(
            Counter(zip(result, result[1:])), Counter(tuple(t) for t in tickets)
        )

    def test_input_not_mutated(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        original = [t[:] for t in tickets]
        self.sol.findItinerary(tickets)
        self.assertEqual(tickets, original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Depth-First Search, Graph Theory, Sorting, Heap (Priority Queue), Eulerian Circuit, Eulerian Path, Semi-Eulerian Graph
