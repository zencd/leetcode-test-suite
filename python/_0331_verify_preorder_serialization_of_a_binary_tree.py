# 331. Verify Preorder Serialization of a Binary Tree
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# Medium

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_valid_full_example(self):
        self.assertTrue(self.sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

    def test_valid_single_null(self):
        self.assertTrue(self.sol.isValidSerialization("#"))

    def test_valid_single_node(self):
        self.assertTrue(self.sol.isValidSerialization("1,#,#"))

    def test_valid_left_child_only(self):
        self.assertTrue(self.sol.isValidSerialization("1,2,#,#,#"))

    def test_valid_right_child_only(self):
        self.assertTrue(self.sol.isValidSerialization("1,#,2,#,#"))

    def test_valid_deep_left_spine(self):
        self.assertTrue(self.sol.isValidSerialization("1,2,3,#,#,#,#"))

    def test_valid_deep_right_spine(self):
        self.assertTrue(self.sol.isValidSerialization("1,#,2,#,3,#,#"))

    def test_invalid_trailing_node(self):
        self.assertFalse(self.sol.isValidSerialization("9,#,#,1"))

    def test_invalid_two_nodes(self):
        self.assertFalse(self.sol.isValidSerialization("1,2"))

    def test_example_2(self):
        self.assertFalse(self.sol.isValidSerialization("1,#"))

    def test_example_3(self):
        self.assertFalse(self.sol.isValidSerialization("9,#,#,1"))

    def test_invalid_empty_after_null(self):
        self.assertFalse(self.sol.isValidSerialization("#,1,#,#"))

    def test_invalid_extra_at_end(self):
        self.assertFalse(self.sol.isValidSerialization("1,#,#,#"))

    def test_invalid_missing_nulls(self):
        self.assertFalse(self.sol.isValidSerialization("1,2,3"))

    def test_valid_zero_value(self):
        self.assertTrue(self.sol.isValidSerialization("0,#,#"))

    def test_valid_max_value(self):
        self.assertTrue(self.sol.isValidSerialization("100,#,#"))

    def test_invalid_single_non_null(self):
        self.assertFalse(self.sol.isValidSerialization("1"))

    def test_valid_perfect_tree_depth_2(self):
        self.assertTrue(self.sol.isValidSerialization("1,2,#,#,3,#,#"))

    def test_invalid_interior_overflow(self):
        self.assertFalse(self.sol.isValidSerialization("1,2,#,#,3,#,#,#"))

    def test_valid_large_valid(self):
        seq = []

        def gen(v, depth):
            seq.append(str(v))
            if depth == 0:
                seq.append("#")
                seq.append("#")
                return
            gen(v * 2 + 1, depth - 1)
            gen(v * 2 + 2, depth - 1)

        gen(1, 4)
        self.assertTrue(self.sol.isValidSerialization(",".join(seq)))

    def test_invalid_large_with_extra(self):
        seq = []

        def gen(v, depth):
            seq.append(str(v))
            if depth == 0:
                seq.append("#")
                seq.append("#")
                return
            gen(v * 2 + 1, depth - 1)
            gen(v * 2 + 2, depth - 1)

        gen(1, 4)
        seq.append("5")
        self.assertFalse(self.sol.isValidSerialization(",".join(seq)))


if __name__ == "__main__":
    unittest.main()

# Tags: String, Stack, Tree, Binary Tree
