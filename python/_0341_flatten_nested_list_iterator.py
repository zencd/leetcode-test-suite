# 341. Flatten Nested List Iterator
# https://leetcode.com/problems/flatten-nested-list-iterator/
# Medium

class NestedInteger:
    def __init__(self, value, nested=False):
        self.value = value
        self.nested = nested

    def isInteger(self) -> bool:
        return not self.nested

    def getInteger(self) -> int:
        if self.nested:
            return None
        return self.value

    def getList(self):
        if not self.nested:
            return None
        return self.value


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        raise Exception("Not solved yet")

    def next(self) -> int:
        raise Exception("Not solved yet")

    def hasNext(self) -> bool:
        raise Exception("Not solved yet")


def make_nested(value):
    if isinstance(value, list):
        return NestedInteger([make_nested(v) for v in value], nested=True)
    return NestedInteger(value)


def flatten(nestedList):
    it = NestedIterator(nestedList)
    res = []
    while it.hasNext():
        res.append(it.next())
    return res


import unittest


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nested = [make_nested(v) for v in [[1, 1], 2, [1, 1]]]
        self.assertEqual(flatten(nested), [1, 1, 2, 1, 1])

    def test_example_2(self):
        nested = [make_nested(v) for v in [1, [4, [6]]]]
        self.assertEqual(flatten(nested), [1, 4, 6])

    def test_single_integer(self):
        nested = [make_nested(42)]
        self.assertEqual(flatten(nested), [42])

    def test_all_integers(self):
        nested = [make_nested(v) for v in [1, 2, 3, 4, 5]]
        self.assertEqual(flatten(nested), [1, 2, 3, 4, 5])

    def test_single_nested_list(self):
        nested = [make_nested([1, 2, 3])]
        self.assertEqual(flatten(nested), [1, 2, 3])

    def test_deeply_nested(self):
        nested = [make_nested(v) for v in [[[[[1]]]]]]
        self.assertEqual(flatten(nested), [1])

    def test_negative_and_zero(self):
        nested = [make_nested(v) for v in [-1, 0, -1000000, 1000000]]
        self.assertEqual(flatten(nested), [-1, 0, -1000000, 1000000])

    def test_nested_with_mixed_ints(self):
        nested = [make_nested(v) for v in [1, [2, [3, 4]], 5]]
        self.assertEqual(flatten(nested), [1, 2, 3, 4, 5])

    def test_lists_of_lists(self):
        nested = [make_nested(v) for v in [[1, 2], [3, 4], [5]]]
        self.assertEqual(flatten(nested), [1, 2, 3, 4, 5])

    def test_empty_inner_list(self):
        nested = [make_nested(v) for v in [[], 1, []]]
        self.assertEqual(flatten(nested), [1])

    def test_only_empty_lists(self):
        nested = [make_nested([[]]), make_nested([])]
        self.assertEqual(flatten(nested), [])

    def test_empty_outer_list(self):
        self.assertEqual(flatten([]), [])

    def test_hasnext_after_exhaustion(self):
        nested = [make_nested(v) for v in [[1, 2], 3]]
        it = NestedIterator(nested)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 1)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 2)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 3)
        self.assertFalse(it.hasNext())

    def test_next_order_with_nested_start(self):
        nested = [make_nested(v) for v in [[[1]], [2], []]]
        it = NestedIterator(nested)
        self.assertEqual(it.next(), 1)
        self.assertEqual(it.next(), 2)
        self.assertFalse(it.hasNext())

    def test_alternating_int_and_list(self):
        nested = [make_nested(v) for v in [1, [2], 3, [4, [5, [6]]], 7]]
        it = NestedIterator(nested)
        expected = [1, 2, 3, 4, 5, 6, 7]
        for value in expected:
            self.assertTrue(it.hasNext())
            self.assertEqual(it.next(), value)
        self.assertFalse(it.hasNext())

    def test_large_list(self):
        data = list(range(100))
        nested = [make_nested(v) for v in data]
        self.assertEqual(flatten(nested), data)

    def test_nested_integers_interface(self):
        ni = NestedInteger(5)
        self.assertTrue(ni.isInteger())
        self.assertEqual(ni.getInteger(), 5)
        self.assertIsNone(ni.getList())
        nl = NestedInteger([NestedInteger(1)], nested=True)
        self.assertFalse(nl.isInteger())
        self.assertIsNone(nl.getInteger())
        self.assertEqual(len(nl.getList()), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Stack, Tree, Depth-First Search, Design, Queue, Iterator
