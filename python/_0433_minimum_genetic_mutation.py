# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/
# Medium

from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]), 1)

    def test_example2(self):
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]), 2)

    def test_start_equals_end(self):
        self.assertEqual(self.sol.minMutation("AAAAAAAA", "AAAAAAAA", ["AAAAAAAA"]), 0)

    def test_empty_bank(self):
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AACCGGTA", []), -1)

    def test_end_not_in_bank(self):
        self.assertEqual(self.sol.minMutation("AACCGGTT", "TTTTTTTT", ["AACCGGTA"]), -1)

    def test_no_path(self):
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA"]), -1)

    def test_longer_chain(self):
        bank = ["AACCGGTA", "AAACGGTA", "AAACGATA", "AAACGACA"]
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AAACGACA", bank), 4)

    def test_single_step_alternate_allele(self):
        self.assertEqual(self.sol.minMutation("AAAAAAAT", "AAAAAAAC", ["AAAAAAAC"]), 1)

    def test_multiple_paths_same_cost(self):
        bank = ["AACCGGTA", "AACCGTTA", "AAACGGTA"]
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AAACGGTA", bank), 2)

    def test_duplicated_bank_entries(self):
        bank = ["AACCGGTA", "AACCGGTA", "AAACGGTA", "AACCGGTA"]
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AAACGGTA", bank), 2)

    def test_start_not_in_bank(self):
        bank = ["AACCGGTA", "AAACGGTA"]
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AAACGGTA", bank), 2)

    def test_end_reachable_only_via_middle(self):
        bank = ["AAACGGTT"]
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AAACGGTT", bank), 1)

    def test_all_T_string(self):
        bank = ["TTTTTTTT"]
        self.assertEqual(self.sol.minMutation("TTTTTTTA", "TTTTTTTT", bank), 1)

    def test_unreachable_all_T(self):
        bank = ["TTTTTTTA"]
        self.assertEqual(self.sol.minMutation("AAAAAAAA", "TTTTTTTT", bank), -1)

    def test_long_chain(self):
        bank = [
            "AAAAAAAT",
            "AAAAAACT",
            "AAAAACCT",
            "AAACACCT",
            "AACCACCT",
            "ACCCACCT",
            "CCCCACCT",
            "CCCCCCCT",
        ]
        self.assertEqual(self.sol.minMutation("AAAAAAAA", "CCCCCCCT", bank), 8)

    def test_bank_contains_start_gene(self):
        bank = ["AACCGGTT", "AACCGGTA"]
        self.assertEqual(self.sol.minMutation("AACCGGTT", "AACCGGTA", bank), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Breadth-First Search, Bidirectional Search
