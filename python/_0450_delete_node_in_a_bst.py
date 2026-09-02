# 450. Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/
# Medium

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        raise Exception("Not solved yet")


def build_tree(values):
    if not values:
        return None
    nodes = [None] * len(values)
    for i, v in enumerate(values):
        if v is not None:
            nodes[i] = TreeNode(v)
    for i, v in enumerate(values):
        if v is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(values):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(values):
                nodes[i].right = nodes[right_idx]
    return nodes[0]


def to_list(root):
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


def is_bst(root, lo=float("-inf"), hi=float("inf")):
    if root is None:
        return True
    if root.val <= lo or root.val >= hi:
        return False
    return is_bst(root.left, lo, root.val) and is_bst(root.right, root.val, hi)


import unittest


class TestSolution(unittest.TestCase):
    def test_empty_tree(self):
        self.assertIsNone(Solution().deleteNode(None, 0))

    def test_single_node_delete(self):
        self.assertIsNone(Solution().deleteNode(build_tree([5]), 5))

    def test_single_node_not_deleted(self):
        tree = build_tree([5])
        self.assertEqual(5, Solution().deleteNode(tree, 3).val)

    def test_delete_leaf(self):
        tree = build_tree([5, 3, 6, 2, 4, None, 7])
        self.assertEqual([5, 3, 6, 2, None, None, 7], to_list(Solution().deleteNode(tree, 4)))

    def test_delete_node_with_one_left_child(self):
        tree = build_tree([5, 3, 6, 2, None, None, 7])
        self.assertEqual([5, 2, 6, None, None, None, 7], to_list(Solution().deleteNode(tree, 3)))

    def test_delete_node_with_one_right_child(self):
        tree = build_tree([3, None, 4])
        self.assertEqual([4], to_list(Solution().deleteNode(tree, 3)))

    def test_delete_root_with_two_children(self):
        tree = build_tree([5, 3, 6, 2, 4, None, 7])
        result = to_list(Solution().deleteNode(tree, 5))
        self.assertEqual(6, result[0])
        self.assertEqual([6, 3, 7, 2, 4], result)
        self.assertTrue(is_bst(build_tree(result)))

    def test_delete_nonexistent_key(self):
        tree = build_tree([5, 3, 6, 2, 4, None, 7])
        result = to_list(Solution().deleteNode(tree, 0))
        self.assertEqual([5, 3, 6, 2, 4, None, 7], result)

    def test_delete_key_smaller_than_all(self):
        tree = build_tree([5, 3, 6, 2, 4, None, 7])
        result = to_list(Solution().deleteNode(tree, 1))
        self.assertEqual([5, 3, 6, 2, 4, None, 7], result)

    def test_delete_key_between_values(self):
        tree = build_tree([5, 3, 6, 2, 4, None, 7])
        result = to_list(Solution().deleteNode(tree, 3))
        self.assertTrue(3 not in result)
        self.assertTrue(is_bst(build_tree(result)))

    def test_negative_values(self):
        tree = build_tree([-1, -5, 0, -7, -2, None, 1])
        result = to_list(Solution().deleteNode(tree, -5))
        self.assertTrue(-5 not in result)
        self.assertTrue(is_bst(build_tree(result)))

    def test_inorder_preserved_after_delete(self):
        tree = build_tree([5, 3, 6, 2, 4, None, 7])

        def inorder(node):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        original = inorder(tree)
        result_root = Solution().deleteNode(tree, 4)
        new_order = inorder(result_root)
        self.assertEqual([v for v in original if v != 4], new_order)

    def test_deeper_tree(self):
        tree = build_tree([9, 5, 12, 2, 7, 11, 15, 1, 3, 6, 8])
        for key in [9, 5, 12, 2, 15]:
            tree = build_tree([9, 5, 12, 2, 7, 11, 15, 1, 3, 6, 8])
            result_root = Solution().deleteNode(tree, key)
            self.assertTrue(is_bst(result_root))
            self.assertNotIn(
                key,
                to_list(result_root),
                "key %s still present after deletion" % key,
            )

    def test_large_values(self):
        tree = build_tree([50000, -100000, 100000])
        result_root = Solution().deleteNode(tree, -100000)
        self.assertEqual([50000, None, 100000], to_list(result_root))


if __name__ == "__main__":
    unittest.main()

# Tags: Tree, Binary Search Tree, Binary Tree
