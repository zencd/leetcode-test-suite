# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/
# Hard

import heapq


class MedianFinder:
    def __init__(self):
        raise Exception("Not solved yet")

    def addNum(self, num: int) -> None:
        raise Exception("Not solved yet")

    def findMedian(self) -> float:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertAlmostEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertAlmostEqual(mf.findMedian(), 2.0)

    def test_leetcode_example_order(self):
        mf = MedianFinder()
        for n in [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 7, 0, 2, 2, 7, 4, 5, 6, 3]:
            mf.addNum(n)
        self.assertAlmostEqual(mf.findMedian(), 4)

    def test_single_element(self):
        mf = MedianFinder()
        mf.addNum(5)
        self.assertAlmostEqual(mf.findMedian(), 5.0)

    def test_two_elements(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertAlmostEqual(mf.findMedian(), 1.5)
        mf2 = MedianFinder()
        mf2.addNum(2)
        mf2.addNum(1)
        self.assertAlmostEqual(mf2.findMedian(), 1.5)

    def test_negative_numbers(self):
        mf = MedianFinder()
        for n in [-5, 3, 0, -1, 10]:
            mf.addNum(n)
        self.assertAlmostEqual(mf.findMedian(), 0)

    def test_all_negatives(self):
        mf = MedianFinder()
        for n in [-3, -1, -7]:
            mf.addNum(n)
        self.assertAlmostEqual(mf.findMedian(), -3)

    def test_zero(self):
        mf = MedianFinder()
        mf.addNum(0)
        self.assertAlmostEqual(mf.findMedian(), 0.0)

    def test_duplicates(self):
        mf = MedianFinder()
        for n in [2, 2, 2, 2]:
            mf.addNum(n)
        self.assertAlmostEqual(mf.findMedian(), 2.0)

    def test_many_duplicates_mixed(self):
        mf = MedianFinder()
        for n in [1, 1, 1, 2, 2, 3]:
            mf.addNum(n)
        self.assertAlmostEqual(mf.findMedian(), 1.5)

    def test_alternating_median_queries(self):
        mf = MedianFinder()
        expected = [1.0, 1.5, 2.0, 2.5, 3.0]
        for i, exp in enumerate(expected, start=1):
            mf.addNum(i)
            self.assertAlmostEqual(mf.findMedian(), exp)

    def test_descending_input(self):
        mf = MedianFinder()
        for n in [10, 8, 6, 4, 2]:
            mf.addNum(n)
        self.assertAlmostEqual(mf.findMedian(), 6.0)

    def test_extreme_values(self):
        mf = MedianFinder()
        mf.addNum(-100000)
        mf.addNum(100000)
        self.assertAlmostEqual(mf.findMedian(), 0.0)

    def test_large_stream_vs_sorted(self):
        import random

        random.seed(42)
        vals = [random.randint(-100000, 100000) for _ in range(1000)]
        mf = MedianFinder()
        for n in vals:
            mf.addNum(n)
        s = sorted(vals)
        mid = len(s) // 2
        expected = float(s[mid]) if len(s) % 2 else (s[mid - 1] + s[mid]) / 2
        self.assertAlmostEqual(mf.findMedian(), expected)

    def test_large_stream_vs_sorted_odd(self):
        import random

        random.seed(7)
        vals = [random.randint(-50, 50) for _ in range(999)]
        mf = MedianFinder()
        for n in vals:
            mf.addNum(n)
        s = sorted(vals)
        expected = float(s[len(s) // 2])
        self.assertAlmostEqual(mf.findMedian(), expected)

    def test_interleaved_adds_and_queries(self):
        mf = MedianFinder()
        ops = [
            ("add", 5),
            ("median",),
            ("add", 3),
            ("median",),
            ("add", 8),
            ("median",),
            ("add", 1),
            ("median",),
        ]
        expected = {1: 5.0, 2: 4.0, 3: 5.0, 4: 4.0}
        count = 0
        for op in ops:
            if op[0] == "add":
                mf.addNum(op[1])
            else:
                count += 1
                self.assertAlmostEqual(mf.findMedian(), expected[count])

    def test_return_type_is_float(self):
        mf = MedianFinder()
        mf.addNum(3)
        self.assertIsInstance(mf.findMedian(), float)

    def test_even_with_fractional_median(self):
        mf = MedianFinder()
        for n in [1, 2, 3, 4]:
            mf.addNum(n)
        self.assertAlmostEqual(mf.findMedian(), 2.5)


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
