# 155. Min Stack
# https://leetcode.com/problems/min-stack/
# Medium

class MinStack:
    def __init__(self):
        raise Exception("Not solved yet")

    def push(self, value: int) -> None:
        raise Exception("Not solved yet")

    def pop(self) -> None:
        raise Exception("Not solved yet")

    def top(self) -> int:
        raise Exception("Not solved yet")

    def getMin(self) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_leetcode_example(self):
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)
        self.assertEqual(s.getMin(), -3)
        s.pop()
        self.assertEqual(s.top(), 0)
        self.assertEqual(s.getMin(), -2)

    def test_single_element(self):
        s = MinStack()
        s.push(5)
        self.assertEqual(s.top(), 5)
        self.assertEqual(s.getMin(), 5)
        s.pop()

    def test_multiple_same_min(self):
        s = MinStack()
        s.push(2)
        s.push(2)
        s.push(2)
        self.assertEqual(s.getMin(), 2)
        s.pop()
        self.assertEqual(s.getMin(), 2)
        s.pop()
        self.assertEqual(s.getMin(), 2)
        s.pop()

    def test_min_restored_after_pop(self):
        s = MinStack()
        s.push(10)
        s.push(5)
        s.push(3)
        self.assertEqual(s.getMin(), 3)
        s.pop()
        self.assertEqual(s.getMin(), 5)
        s.pop()
        self.assertEqual(s.getMin(), 10)

    def test_duplicated_minimum_values(self):
        s = MinStack()
        s.push(-7)
        s.push(-7)
        self.assertEqual(s.getMin(), -7)
        s.pop()
        self.assertEqual(s.getMin(), -7)
        s.pop()

    def test_negative_and_positive(self):
        s = MinStack()
        s.push(-5)
        s.push(3)
        s.push(0)
        self.assertEqual(s.getMin(), -5)
        s.pop()
        s.pop()
        self.assertEqual(s.getMin(), -5)

    def test_alternating_pushe_pop(self):
        s = MinStack()
        self.assertEqual(s.push(1), None)
        self.assertEqual(s.pop(), None)
        self.assertEqual(s.push(-100), None)
        self.assertEqual(s.getMin(), -100)
        self.assertEqual(s.pop(), None)

    def test_push_returns_none(self):
        s = MinStack()
        self.assertIsNone(s.push(0))

    def test_pop_returns_none(self):
        s = MinStack()
        s.push(1)
        self.assertIsNone(s.pop())

    def test_top_after_multiple_pops(self):
        s = MinStack()
        for i in range(10, 0, -1):
            s.push(i)
        self.assertEqual(s.getMin(), 1)
        self.assertEqual(s.top(), 1)
        s.pop()
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.getMin(), 2)
        s.pop()
        self.assertEqual(s.top(), 3)
        self.assertEqual(s.getMin(), 3)

    def test_extreme_values(self):
        s = MinStack()
        low = -(2**31)
        high = 2**31 - 1
        s.push(high)
        self.assertEqual(s.getMin(), high)
        s.push(low)
        self.assertEqual(s.getMin(), low)
        s.push(high)
        self.assertEqual(s.getMin(), low)
        s.pop()
        self.assertEqual(s.getMin(), low)
        s.pop()
        self.assertEqual(s.getMin(), high)
        s.pop()

    def test_large_sequence(self):
        s = MinStack()
        vals = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
        for v in vals:
            s.push(v)
        self.assertEqual(s.getMin(), 1)
        for v in reversed(vals[1:]):
            s.pop()
        self.assertEqual(s.top(), 3)
        self.assertEqual(s.getMin(), 3)
        s.pop()

    def test_interleaved_operations(self):
        s = MinStack()
        s.push(4)
        s.top()
        s.getMin()
        s.push(1)
        s.push(6)
        self.assertEqual(s.getMin(), 1)
        s.pop()
        self.assertEqual(s.getMin(), 1)
        s.pop()
        self.assertEqual(s.getMin(), 4)
        s.pop()

    def test_zero_values(self):
        s = MinStack()
        s.push(0)
        self.assertEqual(s.getMin(), 0)
        self.assertEqual(s.top(), 0)
        s.push(-1)
        self.assertEqual(s.getMin(), -1)
        s.pop()
        self.assertEqual(s.getMin(), 0)
        s.pop()


if __name__ == "__main__":
    unittest.main()

# Tags: Stack, Design
