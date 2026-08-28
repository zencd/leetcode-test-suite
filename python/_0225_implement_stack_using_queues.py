# 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/
# Easy

from collections import deque


class MyStack:
    def __init__(self):
        raise Exception("Not solved yet")

    def push(self, x: int) -> None:
        raise Exception("Not solved yet")

    def pop(self) -> int:
        raise Exception("Not solved yet")

    def top(self) -> int:
        raise Exception("Not solved yet")

    def empty(self) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_initial_empty(self):
        stack = MyStack()
        self.assertTrue(stack.empty())

    def test_push_then_pop_single(self):
        stack = MyStack()
        stack.push(5)
        self.assertFalse(stack.empty())
        self.assertEqual(stack.pop(), 5)
        self.assertTrue(stack.empty())

    def test_push_top_pop(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertFalse(stack.empty())

    def test_top_does_not_mutate(self):
        stack = MyStack()
        stack.push(3)
        stack.push(7)
        self.assertEqual(stack.top(), 7)
        self.assertEqual(stack.top(), 7)
        self.assertEqual(stack.top(), 7)
        self.assertEqual(stack.pop(), 7)
        self.assertEqual(stack.pop(), 3)
        self.assertTrue(stack.empty())

    def test_lifo_order_multiple(self):
        stack = MyStack()
        for value in [1, 2, 3, 4, 5]:
            stack.push(value)
        expected = [5, 4, 3, 2, 1]
        actual = [stack.pop() for _ in range(5)]
        self.assertEqual(actual, expected)
        self.assertTrue(stack.empty())

    def test_interleaved_push_pop_top(self):
        stack = MyStack()
        reference = []
        operations = [
            ("push", 1),
            ("push", 2),
            ("top", None),
            ("pop", None),
            ("push", 3),
            ("top", None),
            ("pop", None),
            ("push", 4),
            ("push", 5),
            ("top", None),
            ("pop", None),
            ("pop", None),
            ("pop", None),
        ]
        for name, arg in operations:
            if name == "push":
                stack.push(arg)
                reference.append(arg)
            elif name == "top":
                self.assertEqual(stack.top(), reference[-1])
            elif name == "pop":
                self.assertEqual(stack.pop(), reference.pop())
        self.assertTrue(stack.empty())
        self.assertEqual(reference, [])

    def test_pop_until_empty(self):
        stack = MyStack()
        stack.push(9)
        stack.push(8)
        stack.push(7)
        self.assertFalse(stack.empty())
        for expected in [7, 8, 9]:
            self.assertEqual(stack.pop(), expected)
        self.assertTrue(stack.empty())

    def test_reuse_after_empty(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        stack.pop()
        self.assertTrue(stack.empty())
        stack.push(4)
        stack.push(6)
        self.assertEqual(stack.top(), 6)
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.pop(), 4)
        self.assertTrue(stack.empty())

    def test_constraint_values(self):
        stack = MyStack()
        for value in range(1, 10):
            stack.push(value)
        for value in range(9, 0, -1):
            self.assertEqual(stack.pop(), value)
        self.assertTrue(stack.empty())

    def test_many_operations(self):
        stack = MyStack()
        reference = []
        for i in range(100):
            if i % 5 == 0:
                if reference:
                    self.assertEqual(stack.pop(), reference.pop())
            else:
                value = (i % 9) + 1
                stack.push(value)
                reference.append(value)
        while reference:
            self.assertEqual(stack.pop(), reference.pop())
        self.assertTrue(stack.empty())

    def test_duplicate_values(self):
        stack = MyStack()
        stack.push(3)
        stack.push(3)
        stack.push(3)
        self.assertEqual(stack.top(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertTrue(stack.empty())

    def test_example_from_description(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertFalse(stack.empty())


if __name__ == "__main__":
    unittest.main()

# Tags: Stack, Design, Queue
