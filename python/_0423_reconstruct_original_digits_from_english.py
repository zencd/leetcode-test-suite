# 423. Reconstruct Original Digits from English
# https://leetcode.com/problems/reconstruct-original-digits-from-english/
# Medium

class Solution:
    def originalDigits(self, s: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.originalDigits("owoztneoer"), "012")

    def test_example2(self):
        self.assertEqual(self.sol.originalDigits("fviefuro"), "45")

    def test_single_digit_zero(self):
        self.assertEqual(self.sol.originalDigits("zerO".lower()), "0")

    def test_single_digit_one(self):
        self.assertEqual(self.sol.originalDigits("one"), "1")

    def test_single_digit_two(self):
        self.assertEqual(self.sol.originalDigits("two"), "2")

    def test_single_digit_three(self):
        self.assertEqual(self.sol.originalDigits("three"), "3")

    def test_single_digit_four(self):
        self.assertEqual(self.sol.originalDigits("four"), "4")

    def test_single_digit_five(self):
        self.assertEqual(self.sol.originalDigits("five"), "5")

    def test_single_digit_six(self):
        self.assertEqual(self.sol.originalDigits("six"), "6")

    def test_single_digit_seven(self):
        self.assertEqual(self.sol.originalDigits("seven"), "7")

    def test_single_digit_eight(self):
        self.assertEqual(self.sol.originalDigits("eight"), "8")

    def test_single_digit_nine(self):
        self.assertEqual(self.sol.originalDigits("nine"), "9")

    def test_all_digits_once(self):
        s = "zeroonetwothreefourfivesixseveneightnine"
        self.assertEqual(self.sol.originalDigits(s), "0123456789")

    def test_duplicates(self):
        s = "zerozerozero"
        self.assertEqual(self.sol.originalDigits(s), "000")

    def test_mixed_duplicates(self):
        s = "oneonetwo"
        self.assertEqual(self.sol.originalDigits(s), "112")

    def test_multiple_of_each(self):
        s = "zerotwozerotwo"
        self.assertEqual(self.sol.originalDigits(s), "0022")

    def test_seven_and_three_distinguishing(self):
        s = "seven" * 2 + "three" * 3
        self.assertEqual(self.sol.originalDigits(s), "33377")

    def test_eight_and_three_distinguishing(self):
        s = "eight" * 3 + "three" * 2
        self.assertEqual(self.sol.originalDigits(s), "33888")

    def test_five_four_six_nine(self):
        s = "fourfivesixnine"
        self.assertEqual(self.sol.originalDigits(s), "4569")

    def test_nine_with_overlapping_chars(self):
        s = "nine" * 4 + "five" * 2 + "six" + "eight"
        self.assertEqual(self.sol.originalDigits(s), "55689999")

    def test_large_counts(self):
        import random

        words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        letters = []
        expected = []
        for d, w in enumerate(words):
            for _ in range(500):
                letters.extend(list(w))
                expected.append(str(d))
        random.seed(42)
        random.shuffle(letters)
        self.assertEqual(self.sol.originalDigits("".join(letters)), "".join(sorted(expected)))

    def test_only_zero_and_nine(self):
        s = "zero" * 10 + "nine" * 5
        self.assertEqual(self.sol.originalDigits(s), "0" * 10 + "9" * 5)

    def test_two_seven(self):
        s = "two" * 3 + "seven" * 2
        self.assertEqual(self.sol.originalDigits(s), "22277")

    def test_one_two_four(self):
        s = "one" + "two" + "four"
        self.assertEqual(self.sol.originalDigits(s), "124")


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Math, String
