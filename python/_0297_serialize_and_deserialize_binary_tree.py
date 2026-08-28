# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Hard

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        raise Exception("Not solved yet")

    def deserialize(self, data):
        raise Exception("Not solved yet")


import unittest


def build_tree(values):
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)
    return root


def tree_values(root):
    out = []
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            out.append(node.val)
            continue
        stack.append((node, True))
        stack.append((node.right, False))
        stack.append((node.left, False))
    return out


def same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.val != b.val:
        return False
    return same_tree(a.left, b.left) and same_tree(a.right, b.right)


def roundtrip(root):
    ser = Codec()
    deser = Codec()
    return deser.deserialize(ser.serialize(root))


class TestSolution(unittest.TestCase):
    def test_empty_tree(self):
        self.assertIsNone(roundtrip(None))
        self.assertEqual(Codec().serialize(None), "#")

    def test_serialize_empty(self):
        self.assertEqual(Codec().serialize(None), "#")

    def test_deserialize_empty(self):
        self.assertIsNone(Codec().deserialize("#"))

    def test_serialize_single_node(self):
        self.assertEqual(Codec().serialize(TreeNode(1)), "1,#,#")

    def test_example1(self):
        root = build_tree([1, 2, 3, None, None, 4, 5])
        restored = roundtrip(root)
        self.assertTrue(same_tree(root, restored))

    def test_example2(self):
        self.assertIsNone(roundtrip(None))

    def test_all_left(self):
        root = build_tree([1, 2, None, 3, None, 4])
        self.assertTrue(same_tree(root, roundtrip(root)))

    def test_all_right(self):
        root = build_tree([1, None, 2, None, 3, None, 4])
        self.assertTrue(same_tree(root, roundtrip(root)))

    def test_negative_values(self):
        root = build_tree([-5, -2, -3, 10, None, -1000, 1000])
        self.assertTrue(same_tree(root, roundtrip(root)))

    def test_boundary_values(self):
        root = build_tree([0, -1000, 1000, 0, 0, None, None])
        self.assertTrue(same_tree(root, roundtrip(root)))

    def test_full_small_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(same_tree(root, roundtrip(root)))

    def test_serialize_known_format(self):
        root = build_tree([1, 2, 3, None, None, 4, 5])
        self.assertEqual(Codec().serialize(root), "1,2,#,#,3,4,#,#,5,#,#")

    def test_deserialize_known_format(self):
        root = Codec().deserialize("1,2,#,#,3,4,#,#,5,#,#")
        self.assertEqual([n.val for n in list(BFS(root))], [1, 2, 3, 4, 5])

    def test_deeper_tree(self):
        root = build_tree([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertTrue(same_tree(root, roundtrip(root)))

    def test_large_chain(self):
        root = None
        cur = root
        for i in range(100):
            node = TreeNode(i)
            if cur is None:
                root = node
            else:
                cur.left = node
            cur = node
        restored = roundtrip(root)
        self.assertTrue(same_tree(root, restored))

    def test_idempotence_of_serialize(self):
        root = build_tree([1, 2, 3, None, 4, None, 5])
        ser = Codec()
        self.assertEqual(ser.serialize(root), ser.serialize(roundtrip(root)))


class BFS:
    def __init__(self, root):
        self.root = root

    def __iter__(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            yield node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
