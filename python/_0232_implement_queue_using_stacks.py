# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
# Easy

class MyQueue:
    def __init__(self):
        raise Exception("Not solved yet")

    def push(self, x: int) -> None:
        raise Exception("Not solved yet")

    def pop(self) -> int:
        raise Exception("Not solved yet")

    def peek(self) -> int:
        raise Exception("Not solved yet")

    def empty(self) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example1(self):
        q = MyQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.empty(), False)

    def test_initial_state_is_empty(self):
        q = MyQueue()
        self.assertEqual(q.empty(), True)

    def test_push_then_pop_single_element(self):
        q = MyQueue()
        q.push(5)
        self.assertEqual(q.pop(), 5)
        self.assertEqual(q.empty(), True)

    def test_fifo_order(self):
        q = MyQueue()
        for x in [1, 2, 3, 4, 5]:
            q.push(x)
        expected = [1, 2, 3, 4, 5]
        for exp in expected:
            self.assertEqual(q.pop(), exp)
        self.assertEqual(q.empty(), True)

    def test_peek_does_not_remove(self):
        q = MyQueue()
        q.push(7)
        q.push(8)
        self.assertEqual(q.peek(), 7)
        self.assertEqual(q.peek(), 7)
        self.assertEqual(q.peek(), 7)

    def test_peek_before_any_pop(self):
        q = MyQueue()
        q.push(3)
        q.push(4)
        self.assertEqual(q.peek(), 3)
        self.assertEqual(q.pop(), 3)
        self.assertEqual(q.empty(), False)
        self.assertEqual(q.peek(), 4)

    def test_alternating_push_and_pop(self):
        q = MyQueue()
        for x in [1, 9]:
            q.push(x)
            self.assertEqual(q.pop(), x)
        self.assertEqual(q.empty(), True)

    def test_refill_out_stack_after_drain(self):
        q = MyQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)
        q.push(3)
        q.push(4)
        self.assertEqual(q.pop(), 3)
        self.assertEqual(q.pop(), 4)
        self.assertEqual(q.empty(), True)

    def test_interleaved_operations(self):
        q = MyQueue()
        q.push(1)
        q.pop()
        q.push(2)
        q.push(3)
        q.push(4)
        self.assertEqual(q.peek(), 2)
        self.assertEqual(q.pop(), 2)
        q.push(5)
        self.assertEqual(q.pop(), 3)
        self.assertEqual(q.pop(), 4)
        self.assertEqual(q.pop(), 5)
        self.assertEqual(q.empty(), True)

    def test_many_elements(self):
        q = MyQueue()
        values = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        for x in values:
            q.push(x)
        got = [q.pop() for _ in range(len(values))]
        self.assertEqual(got, values)

    def test_empty_after_all_popped(self):
        q = MyQueue()
        q.push(1)
        q.pop()
        self.assertEqual(q.empty(), True)
        q.push(2)
        self.assertEqual(q.empty(), False)
        q.pop()
        self.assertEqual(q.empty(), True)

    def test_push_after_empty(self):
        q = MyQueue()
        q.push(1)
        q.pop()
        q.push(2)
        self.assertEqual(q.peek(), 2)
        self.assertEqual(q.pop(), 2)

    def test_mixed_peek_and_pop_sequence(self):
        q = MyQueue()
        q.push(10)
        q.push(20)
        q.push(30)
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.pop(), 10)
        self.assertEqual(q.peek(), 20)
        self.assertEqual(q.pop(), 20)
        self.assertEqual(q.peek(), 30)
        self.assertEqual(q.pop(), 30)


if __name__ == "__main__":
    unittest.main()

# Tags: Stack, Design, Queue
