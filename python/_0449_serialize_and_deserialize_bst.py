# 449. Serialize and Deserialize BST
# https://leetcode.com/problems/serialize-and-deserialize-bst/
# Medium

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        raise Exception("Not solved yet")

    def deserialize(self, data: str) -> Optional[TreeNode]:
        raise Exception("Not solved yet")


def tree_from_list(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.ser = Codec()
        self.deser = Codec()

    def roundtrip(self, root):
        data = self.ser.serialize(root)
        restored = self.deser.deserialize(data)
        self.assertEqual(tree_to_list(root), tree_to_list(restored))

    def test_empty_tree(self):
        self.assertEqual(self.ser.serialize(None), "")
        self.assertIsNone(self.deser.deserialize(""))

    def test_single_node(self):
        root = TreeNode(5)
        self.roundtrip(root)

    def test_example_1(self):
        root = tree_from_list([2, 1, 3])
        self.roundtrip(root)

    def test_skewed_left(self):
        root = tree_from_list([5, 4, None, 3, None, 2, None, 1])
        self.roundtrip(root)

    def test_skewed_right(self):
        root = tree_from_list([1, None, 2, None, 3, None, 4])
        self.roundtrip(root)

    def test_two_node_left(self):
        root = tree_from_list([2, 1])
        self.roundtrip(root)

    def test_two_node_right(self):
        root = tree_from_list([1, None, 2])
        self.roundtrip(root)

    def test_complete_tree(self):
        root = tree_from_list([4, 2, 6, 1, 3, 5, 7])
        self.roundtrip(root)

    def test_zero_valued_nodes(self):
        root = TreeNode(0)
        root.right = TreeNode(1)
        root.right.right = TreeNode(2)
        self.roundtrip(root)

    def test_zero_with_children(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        self.roundtrip(root)

    def test_wide_balanced(self):
        root = tree_from_list([10, 5, 15, 2, 7, 12, 20, 1, 3, 6, 8, 11, 13, 18, 25])
        self.roundtrip(root)

    def test_deep_chain(self):
        root = TreeNode(1)
        node = root
        for i in range(2, 51):
            node.right = TreeNode(i)
            node = node.right
        self.roundtrip(root)

    def test_serialize_produces_string(self):
        root = tree_from_list([2, 1, 3])
        data = self.ser.serialize(root)
        self.assertIsInstance(data, str)
        self.assertEqual(data, "2,1,3")

    def test_deserialize_single_value(self):
        root = self.deser.deserialize("42")
        self.assertEqual(tree_to_list(root), [42])

    def test_deserialize_known_string(self):
        root = self.deser.deserialize("2,1,3")
        self.assertEqual(tree_to_list(root), [2, 1, 3])

    def test_structure_preserved(self):
        root = tree_from_list([5, 3, 8, 1, 4, 7, 9])
        data = self.ser.serialize(root)
        restored = self.deser.deserialize(data)
        self.assertEqual(tree_to_list(restored), [5, 3, 8, 1, 4, 7, 9])

    def test_large_balanced_tree(self):
        root = tree_from_list([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93])
        self.roundtrip(root)

    def test_max_values(self):
        root = TreeNode(10000)
        root.left = TreeNode(0)
        self.roundtrip(root)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Search Tree, Binary Tree
