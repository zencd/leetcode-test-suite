# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/
# Medium

class Solution:
    def numTrees(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_n1(self):
        self.assertEqual(self.sol.numTrees(1), 1)

    def test_n2(self):
        self.assertEqual(self.sol.numTrees(2), 2)

    def test_n3(self):
        self.assertEqual(self.sol.numTrees(3), 5)

    def test_n4(self):
        self.assertEqual(self.sol.numTrees(4), 14)

    def test_n5(self):
        self.assertEqual(self.sol.numTrees(5), 42)

    def test_n6(self):
        self.assertEqual(self.sol.numTrees(6), 132)

    def test_n7(self):
        self.assertEqual(self.sol.numTrees(7), 429)

    def test_n8(self):
        self.assertEqual(self.sol.numTrees(8), 1430)

    def test_n9(self):
        self.assertEqual(self.sol.numTrees(9), 4862)

    def test_n10(self):
        self.assertEqual(self.sol.numTrees(10), 16796)

    def test_n11(self):
        self.assertEqual(self.sol.numTrees(11), 58786)

    def test_n12(self):
        self.assertEqual(self.sol.numTrees(12), 208012)

    def test_n13(self):
        self.assertEqual(self.sol.numTrees(13), 742900)

    def test_n14(self):
        self.assertEqual(self.sol.numTrees(14), 2674440)

    def test_n15(self):
        self.assertEqual(self.sol.numTrees(15), 9694845)

    def test_n16(self):
        self.assertEqual(self.sol.numTrees(16), 35357670)

    def test_n17(self):
        self.assertEqual(self.sol.numTrees(17), 129644790)

    def test_n18(self):
        self.assertEqual(self.sol.numTrees(18), 477638700)

    def test_n19(self):
        self.assertEqual(self.sol.numTrees(19), 1767263190)

    def test_returns_int(self):
        self.assertIsInstance(self.sol.numTrees(3), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming, Tree, Binary Search Tree, Binary Tree
