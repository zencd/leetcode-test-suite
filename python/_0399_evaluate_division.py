# 399. Evaluate Division
# https://leetcode.com/problems/evaluate-division/
# Medium

from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1.0, 1.0, -1.0]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_example2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        expected = [3.75, 0.4, 5.0, 0.2]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_example3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        expected = [0.5, 2.0, -1.0, -1.0]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_identity_query_defined_variable(self):
        equations = [["a", "b"]]
        values = [4.0]
        queries = [["a", "a"]]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), [1.0]
        )

    def test_direct_equation_query(self):
        equations = [["a", "b"]]
        values = [3.0]
        queries = [["a", "b"]]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), [3.0]
        )

    def test_reverse_direct_query(self):
        equations = [["a", "b"]]
        values = [3.0]
        queries = [["b", "a"]]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), [1.0 / 3.0]
        )

    def test_three_variable_chain(self):
        equations = [["a", "b"], ["b", "c"], ["c", "d"]]
        values = [2.0, 3.0, 4.0]
        queries = [["a", "d"], ["d", "a"], ["a", "c"], ["b", "d"]]
        expected = [24.0, 1.0 / 24.0, 6.0, 12.0]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_cycle_with_consistent_values(self):
        equations = [["a", "b"], ["b", "c"], ["c", "a"]]
        values = [2.0, 3.0, 1.0 / 6.0]
        queries = [["a", "b"], ["b", "c"], ["c", "a"], ["a", "c"]]
        expected = [2.0, 3.0, 1.0 / 6.0, 6.0]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_disconnected_components(self):
        equations = [["a", "b"], ["x", "y"]]
        values = [2.0, 5.0]
        queries = [["a", "x"], ["b", "y"], ["y", "x"], ["a", "b"]]
        expected = [-1.0, -1.0, 0.2, 2.0]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_multiple_queries_mixed(self):
        equations = [["a", "b"], ["c", "d"]]
        values = [1.0, 1.0]
        queries = [
            ["a", "b"],
            ["b", "a"],
            ["c", "d"],
            ["d", "c"],
            ["a", "c"],
            ["b", "d"],
            ["z", "z"],
        ]
        expected = [1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_variable_with_digits(self):
        equations = [["a1", "b2"], ["b2", "c3"]]
        values = [2.0, 0.5]
        queries = [["a1", "c3"], ["c3", "a1"]]
        expected = [1.0, 1.0]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_single_letter_variables(self):
        equations = [["1", "2"]]
        values = [20.0]
        queries = [["1", "2"], ["2", "1"]]
        expected = [20.0, 0.05]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_max_value_boundary(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [20.0, 20.0]
        queries = [["a", "c"], ["c", "a"]]
        expected = [400.0, 0.0025]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_unknown_pair_same_component_different_paths(self):
        equations = [["a", "b"], ["c", "d"], ["b", "c"]]
        values = [2.0, 4.0, 8.0]
        queries = [["a", "d"], ["a", "b"], ["b", "a"], ["d", "a"], ["c", "b"]]
        expected = [64.0, 2.0, 0.5, 1.0 / 64.0, 0.125]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_query_with_only_one_defined_variable(self):
        equations = [["a", "b"]]
        values = [1.5]
        queries = [["a", "c"], ["c", "a"], ["c", "b"]]
        expected = [-1.0, -1.0, -1.0]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_duplicated_equations_consistent(self):
        equations = [["a", "b"], ["b", "a"]]
        values = [2.0, 0.5]
        queries = [["a", "b"], ["b", "a"]]
        expected = [2.0, 0.5]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def test_larger_graph(self):
        equations = [
            ["a", "b"],
            ["b", "c"],
            ["c", "d"],
            ["d", "e"],
            ["e", "f"],
            ["f", "g"],
            ["g", "a"],
        ]
        values = [2.0, 3.0, 0.5, 4.0, 0.5, 2.0, 1.0 / 12.0]
        queries = [
            ["a", "c"],
            ["a", "e"],
            ["a", "g"],
            ["a", "f"],
            ["b", "g"],
            ["b", "g"],
            ["g", "b"],
            ["e", "a"],
        ]
        expected = [6.0, 12.0, 12.0, 6.0, 6.0, 6.0, 1.0 / 6.0, 1.0 / 12.0]
        self.assertResultsNear(
            self.solution.calcEquation(equations, values, queries), expected
        )

    def assertResultsNear(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        for a, e in zip(actual, expected):
            if e == -1.0:
                self.assertEqual(a, -1.0)
            else:
                self.assertAlmostEqual(a, e, places=5)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, String, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Shortest Path, Bellman–Ford Algorithm, Floyd–Warshall Algorithm
