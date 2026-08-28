# 385. Mini Parser
# https://leetcode.com/problems/mini-parser/
# Medium

class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self._is_int = False
            self._list = []
        else:
            self._is_int = True
            self._value = value

    def isInteger(self):
        return self._is_int

    def add(self, elem):
        self._is_int = False
        self._list.append(elem)

    def setInteger(self, value):
        self._is_int = True
        self._value = value

    def getInteger(self):
        if self._is_int:
            return self._value
        return None

    def getList(self):
        if not self._is_int:
            return self._list
        return None


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        raise Exception("Not solved yet")


def serialize(ni: NestedInteger) -> str:
    if ni.isInteger():
        return str(ni.getInteger())
    return "[" + ",".join(serialize(x) for x in ni.getList()) + "]"


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def parse_and_check_str(self, s):
        return serialize(self.sol.deserialize(s))

    def test_positive_integer(self):
        ni = self.sol.deserialize("324")
        self.assertTrue(ni.isInteger())
        self.assertEqual(ni.getInteger(), 324)
        self.assertIsNone(ni.getList())

    def test_negative_integer(self):
        ni = self.sol.deserialize("-123")
        self.assertTrue(ni.isInteger())
        self.assertEqual(ni.getInteger(), -123)

    def test_zero(self):
        ni = self.sol.deserialize("0")
        self.assertTrue(ni.isInteger())
        self.assertEqual(ni.getInteger(), 0)

    def test_max_values(self):
        self.assertEqual(self.sol.deserialize("1000000").getInteger(), 1000000)
        self.assertEqual(self.sol.deserialize("-1000000").getInteger(), -1000000)

    def test_single_element_list(self):
        self.assertEqual(self.parse_and_check_str("[1]"), "[1]")

    def test_simple_list(self):
        self.assertEqual(self.parse_and_check_str("[1,2,3]"), "[1,2,3]")

    def test_list_of_negative_numbers(self):
        self.assertEqual(self.parse_and_check_str("[-1,-2,-3]"), "[-1,-2,-3]")

    def test_nested_lists(self):
        self.assertEqual(
            self.parse_and_check_str("[123,[456,[789]]]"), "[123,[456,[789]]]"
        )

    def test_deep_nesting(self):
        self.assertEqual(self.parse_and_check_str("[[[[324]]]]"), "[[[[324]]]]")

    def test_empty_list(self):
        ni = self.sol.deserialize("[]")
        self.assertFalse(ni.isInteger())
        self.assertEqual(ni.getList(), [])
        self.assertIsNone(ni.getInteger())

    def test_list_with_empty_list(self):
        self.assertEqual(self.parse_and_check_str("[1,[]]"), "[1,[]]")

    def test_mixed(self):
        self.assertEqual(self.parse_and_check_str("[-123,[]]"), "[-123,[]]")

    def test_list_structure(self):
        ni = self.sol.deserialize("[1,[2,3]]")
        self.assertFalse(ni.isInteger())
        lst = ni.getList()
        self.assertEqual(len(lst), 2)
        self.assertTrue(lst[0].isInteger())
        self.assertEqual(lst[0].getInteger(), 1)
        self.assertFalse(lst[1].isInteger())
        inner = lst[1].getList()
        self.assertEqual([x.getInteger() for x in inner], [2, 3])

    def test_list_get_integer_returns_none(self):
        self.assertIsNone(self.sol.deserialize("[1]").getInteger())
        self.assertIsNone(self.sol.deserialize("[]").getInteger())

    def test_integer_get_list_returns_none(self):
        self.assertIsNone(self.sol.deserialize("5").getList())

    def test_many_elements(self):
        s = "[" + ",".join(str(i) for i in range(50000)) + "]"
        ni = self.sol.deserialize(s)
        lst = ni.getList()
        self.assertEqual(len(lst), 50000)
        self.assertEqual(lst[0].getInteger(), 0)
        self.assertEqual(lst[49999].getInteger(), 49999)

    def test_many_sublists(self):
        s = "[" + ",".join("[5]" for _ in range(2000)) + "]"
        ni = self.sol.deserialize(s)
        lst = ni.getList()
        self.assertEqual(len(lst), 2000)
        for elem in lst:
            self.assertFalse(elem.isInteger())
            self.assertEqual(elem.getList()[0].getInteger(), 5)

    def test_deep_nesting_performance(self):
        depth = 2000
        s = "[" * depth + "7" + "]" * depth
        ni = self.sol.deserialize(s)
        for _ in range(depth - 1):
            self.assertFalse(ni.isInteger())
            ni = ni.getList()[0]
        self.assertFalse(ni.isInteger())
        inner = ni.getList()
        self.assertEqual(len(inner), 1)
        self.assertTrue(inner[0].isInteger())
        self.assertEqual(inner[0].getInteger(), 7)

    def test_negative_number_in_nested_list(self):
        self.assertEqual(self.parse_and_check_str("[1,[2,-3]]"), "[1,[2,-3]]")

    def test_multi_digit_boundaries(self):
        self.assertEqual(self.parse_and_check_str("[10,200,3000]"), "[10,200,3000]")


if __name__ == "__main__":
    unittest.main()

# Tags: String, Stack, Depth-First Search
