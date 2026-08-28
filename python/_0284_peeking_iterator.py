# 284. Peeking Iterator
# https://leetcode.com/problems/peeking-iterator/
# Medium

import unittest


class Iterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def hasNext(self):
        return self.index < len(self.nums)

    def next(self):
        if not self.hasNext():
            return None
        value = self.nums[self.index]
        self.index += 1
        return value


class PeekingIterator:
    def __init__(self, iterator):
        raise Exception("Not solved yet")

    def peek(self):
        raise Exception("Not solved yet")

    def next(self):
        raise Exception("Not solved yet")

    def hasNext(self):
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def test_example1(self):
        peeker = PeekingIterator(Iterator([1, 2, 3]))
        self.assertEqual(peeker.next(), 1)
        self.assertEqual(peeker.peek(), 2)
        self.assertEqual(peeker.next(), 2)
        self.assertEqual(peeker.next(), 3)
        self.assertFalse(peeker.hasNext())

    def test_repeated_peek_returns_same_value(self):
        peeker = PeekingIterator(Iterator([1, 2, 3]))
        for _ in range(5):
            self.assertEqual(peeker.peek(), 1)
        self.assertEqual(peeker.peek(), 1)

    def test_peek_does_not_advance_pointer(self):
        peeker = PeekingIterator(Iterator([1, 2, 3]))
        self.assertEqual(peeker.peek(), 1)
        self.assertEqual(peeker.peek(), 1)
        self.assertTrue(peeker.hasNext())
        self.assertEqual(peeker.next(), 1)
        self.assertEqual(peeker.peek(), 2)

    def test_single_element_lifecycle(self):
        peeker = PeekingIterator(Iterator([42]))
        self.assertTrue(peeker.hasNext())
        self.assertEqual(peeker.peek(), 42)
        self.assertTrue(peeker.hasNext())
        self.assertEqual(peeker.next(), 42)
        self.assertFalse(peeker.hasNext())

    def test_empty_iterator_has_next_false(self):
        peeker = PeekingIterator(Iterator([]))
        self.assertFalse(peeker.hasNext())

    def test_has_next_false_after_draining_via_peek(self):
        peeker = PeekingIterator(Iterator([10]))
        peeker.peek()
        peeker.next()
        self.assertFalse(peeker.hasNext())

    def test_interleaved_peek_and_next(self):
        peeker = PeekingIterator(Iterator([1, 2, 3, 4, 5]))
        operations = [
            ("peek", 1),
            ("next", 1),
            ("peek", 2),
            ("peek", 2),
            ("next", 2),
            ("peek", 3),
            ("next", 3),
            ("next", 4),
            ("peek", 5),
            ("peek", 5),
            ("next", 5),
        ]
        for operation, value in operations:
            if operation == "peek":
                self.assertEqual(peeker.peek(), value)
            else:
                self.assertEqual(peeker.next(), value)
        self.assertFalse(peeker.hasNext())

    def test_has_next_toggles_correctly(self):
        peeker = PeekingIterator(Iterator([7, 8]))
        self.assertTrue(peeker.hasNext())
        peeker.next()
        self.assertTrue(peeker.hasNext())
        peeker.next()
        self.assertFalse(peeker.hasNext())

    def test_full_drain_of_large_list(self):
        nums = list(range(1, 1001))
        peeker = PeekingIterator(Iterator(nums))
        seen = []
        while peeker.hasNext():
            self.assertEqual(peeker.peek(), nums[len(seen)])
            seen.append(peeker.next())
        self.assertEqual(seen, nums)
        self.assertFalse(peeker.hasNext())

    def test_peek_before_any_next(self):
        peeker = PeekingIterator(Iterator([9, 3, 7]))
        self.assertEqual(peeker.peek(), 9)
        self.assertEqual(peeker.peek(), 9)
        self.assertEqual(peeker.next(), 9)
        self.assertEqual(peeker.peek(), 3)
        self.assertEqual(peeker.next(), 3)
        self.assertEqual(peeker.peek(), 7)
        self.assertEqual(peeker.peek(), 7)
        self.assertEqual(peeker.next(), 7)
        self.assertFalse(peeker.hasNext())

    def test_peek_then_has_next_then_next_cycle(self):
        peeker = PeekingIterator(Iterator([1, 2, 3]))
        for expected in (1, 2, 3):
            self.assertTrue(peeker.hasNext())
            self.assertEqual(peeker.peek(), expected)
            self.assertTrue(peeker.hasNext())
            self.assertEqual(peeker.next(), expected)
        self.assertFalse(peeker.hasNext())


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Design, Iterator
