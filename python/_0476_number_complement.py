# 476. Number Complement
# https://leetcode.com/problems/number-complement/
# Easy

class Solution:
    def findComplement(self, num: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.findComplement(5), 2)
        self.assertEqual(self.solution.findComplement(1), 0)

    def test_small_numbers(self):
        self.assertEqual(self.solution.findComplement(2), 1)
        self.assertEqual(self.solution.findComplement(3), 0)
        self.assertEqual(self.solution.findComplement(4), 3)
        self.assertEqual(self.solution.findComplement(7), 0)
        self.assertEqual(self.solution.findComplement(8), 7)
        self.assertEqual(self.solution.findComplement(10), 5)

    def test_powers_of_two(self):
        for i in range(1, 20):
            n = 1 << i
            self.assertEqual(self.solution.findComplement(n), n - 1)

    def test_all_ones(self):
        for i in range(1, 16):
            n = (1 << i) - 1
            self.assertEqual(self.solution.findComplement(n), 0)

    def test_formula_property(self):
        for n in range(1, 1000):
            k = n.bit_length()
            self.assertEqual(self.solution.findComplement(n), (1 << k) - 1 - n)

    def test_max_constraint(self):
        self.assertEqual(self.solution.findComplement((1 << 31) - 1), 0)
        self.assertIsNotNone(self.solution.findComplement((1 << 31) - 2))

    def test_result_range(self):
        for n in range(1, 100):
            comp = self.solution.findComplement(n)
            self.assertGreaterEqual(comp, 0)
            self.assertLess(comp, (1 << n.bit_length()))


if __name__ == "__main__":
    unittest.main()

# Tags: Bit Manipulation
