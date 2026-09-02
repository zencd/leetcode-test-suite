# 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/
# Easy

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_n_1(self) -> None:
        self.assertEqual(self.solution.fizzBuzz(1), ["1"])

    def test_n_2(self) -> None:
        self.assertEqual(self.solution.fizzBuzz(2), ["1", "2"])

    def test_n_3(self) -> None:
        self.assertEqual(self.solution.fizzBuzz(3), ["1", "2", "Fizz"])

    def test_n_5(self) -> None:
        self.assertEqual(
            self.solution.fizzBuzz(5),
            ["1", "2", "Fizz", "4", "Buzz"],
        )

    def test_n_15(self) -> None:
        self.assertEqual(
            self.solution.fizzBuzz(15),
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        )

    def test_length_equals_n(self) -> None:
        for n in (1, 2, 3, 4, 5, 15, 16, 100, 999):
            self.assertEqual(len(self.solution.fizzBuzz(n)), n)

    def test_all_elements_are_strings(self) -> None:
        for item in self.solution.fizzBuzz(30):
            self.assertIsInstance(item, str)

    def test_correctness_of_each_slot(self) -> None:
        expected = []
        for i in range(1, 101):
            if i % 15 == 0:
                expected.append("FizzBuzz")
            elif i % 3 == 0:
                expected.append("Fizz")
            elif i % 5 == 0:
                expected.append("Buzz")
            else:
                expected.append(str(i))
        self.assertEqual(self.solution.fizzBuzz(100), expected)

    def test_slot_values(self) -> None:
        result = self.solution.fizzBuzz(30)
        self.assertEqual(result[2], "Fizz")
        self.assertEqual(result[4], "Buzz")
        self.assertEqual(result[14], "FizzBuzz")
        self.assertEqual(result[5], "Fizz")
        self.assertEqual(result[9], "Buzz")
        self.assertEqual(result[19], "Buzz")
        self.assertEqual(result[29], "FizzBuzz")
        self.assertEqual(result[0], "1")
        self.assertEqual(result[28], "29")

    def test_n_4_only_numbers(self) -> None:
        self.assertEqual(self.solution.fizzBuzz(1), ["1"])

    def test_n_10(self) -> None:
        self.assertEqual(
            self.solution.fizzBuzz(10),
            ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"],
        )

    def test_n_6(self) -> None:
        self.assertEqual(
            self.solution.fizzBuzz(6),
            ["1", "2", "Fizz", "4", "Buzz", "Fizz"],
        )

    def test_n_7(self) -> None:
        self.assertEqual(
            self.solution.fizzBuzz(7),
            ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"],
        )

    def test_fizz_buzz_only_at_multiples_of_15(self) -> None:
        result = self.solution.fizzBuzz(60)
        for i, value in enumerate(result, start=1):
            if "FizzBuzz" in value:
                self.assertEqual(value, "FizzBuzz")
                self.assertEqual(i % 15, 0)
            if value == "Fizz":
                self.assertEqual(i % 3, 0)
                self.assertNotEqual(i % 5, 0)
            if value == "Buzz":
                self.assertEqual(i % 5, 0)
                self.assertNotEqual(i % 3, 0)

    def test_n_10000(self) -> None:
        result = self.solution.fizzBuzz(10**4)
        self.assertEqual(len(result), 10**4)
        self.assertEqual(result[-1], "Buzz")
        self.assertEqual(result[14], "FizzBuzz")

    def test_returns_fresh_list(self) -> None:
        first = self.solution.fizzBuzz(10)
        second = self.solution.fizzBuzz(10)
        self.assertEqual(first, second)
        self.assertIsNot(first, second)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Simulation
