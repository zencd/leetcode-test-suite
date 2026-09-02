# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/
# Medium

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.removeKdigits("1432219", 3), "1219")

    def test_example_2(self):
        self.assertEqual(self.solution.removeKdigits("10200", 1), "200")

    def test_example_3(self):
        self.assertEqual(self.solution.removeKdigits("10", 2), "0")

    def test_remove_all_digits(self):
        self.assertEqual(self.solution.removeKdigits("12345", 5), "0")

    def test_k_equals_length(self):
        self.assertEqual(self.solution.removeKdigits("5", 1), "0")

    def test_single_digit(self):
        self.assertEqual(self.solution.removeKdigits("7", 1), "0")

    def test_all_same_digits(self):
        self.assertEqual(self.solution.removeKdigits("1111", 2), "11")

    def test_decreasing_sequence(self):
        self.assertEqual(self.solution.removeKdigits("54321", 2), "321")

    def test_increasing_sequence(self):
        self.assertEqual(self.solution.removeKdigits("12345", 2), "123")

    def test_single_character_increase(self):
        self.assertEqual(self.solution.removeKdigits("10", 1), "0")

    def test_already_smallest(self):
        self.assertEqual(self.solution.removeKdigits("1234", 0), "1234")

    def test_zeros_everywhere(self):
        self.assertEqual(self.solution.removeKdigits("1000", 1), "0")

    def test_mixed_small(self):
        self.assertEqual(self.solution.removeKdigits("1234567890", 5), "12340")

    def test_remove_from_middle(self):
        self.assertEqual(self.solution.removeKdigits("5321", 2), "21")

    def test_k_larger_than_effective(self):
        self.assertEqual(self.solution.removeKdigits("99999", 3), "99")

    def test_large_decreasing(self):
        self.assertEqual(self.solution.removeKdigits("123456789", 4), "12345")

    def test_alternating(self):
        self.assertEqual(self.solution.removeKdigits("314159", 3), "115")

    def test_zeros_in_output_middle(self):
        self.assertEqual(self.solution.removeKdigits("43210", 1), "3210")

    def test_zero_only_input(self):
        self.assertEqual(self.solution.removeKdigits("0", 1), "0")

    def test_large_input(self):
        num = "9" * 50000 + "1" + "2" * 49999
        self.assertEqual(self.solution.removeKdigits(num, 50000), "1" + "2" * 49999)

    def test_large_same_digits_tail_trim(self):
        num = "1" * 100000
        self.assertEqual(self.solution.removeKdigits(num, 90000), "1" * 10000)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Stack, Greedy, Monotonic Stack
