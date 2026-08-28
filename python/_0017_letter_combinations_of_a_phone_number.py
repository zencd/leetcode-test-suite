# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Medium

from typing import List
import unittest


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        raise Exception("Not solved yet")


class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        expected = set("ad ae af bd be bf cd ce cf".split())
        self.assertEqual(set(self.sol.letterCombinations("23")), expected)

    def test_example_2(self):
        self.assertEqual(set(self.sol.letterCombinations("2")), {"a", "b", "c"})

    def test_empty_string(self):
        self.assertEqual(self.sol.letterCombinations(""), [])

    def test_single_digit_9(self):
        self.assertEqual(set(self.sol.letterCombinations("9")), {"w", "x", "y", "z"})

    def test_single_digit_7(self):
        self.assertEqual(set(self.sol.letterCombinations("7")), {"p", "q", "r", "s"})

    def test_two_digits_79(self):
        expected = [
            "pw",
            "px",
            "py",
            "pz",
            "qw",
            "qx",
            "qy",
            "qz",
            "rw",
            "rx",
            "ry",
            "rz",
            "sw",
            "sx",
            "sy",
            "sz",
        ]
        self.assertEqual(len(self.sol.letterCombinations("79")), 16)
        self.assertEqual(set(self.sol.letterCombinations("79")), set(expected))

    def test_repeated_digits(self):
        letters = self.sol.letterCombinations("22")
        self.assertEqual(len(letters), 9)
        self.assertEqual(
            set(letters),
            {"aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"},
        )

    def test_max_length_4(self):
        letters = self.sol.letterCombinations("2345")
        self.assertEqual(len(letters), 3 * 3 * 3 * 3)
        for s in letters:
            self.assertEqual(len(s), 4)
        self.assertEqual(
            set(letters),
            {a + b + c + d for a in "abc" for b in "def" for c in "ghi" for d in "jkl"},
        )

    def test_digit_with_four_letters(self):
        letters = self.sol.letterCombinations("78")
        self.assertEqual(len(letters), 4 * 3)
        self.assertEqual(
            set(letters),
            {a + b for a in "pqrs" for b in "tuv"},
        )

    def test_result_size_for_mixed_lengths(self):
        self.assertEqual(len(self.sol.letterCombinations("777")), 4**3)
        self.assertEqual(len(self.sol.letterCombinations("2468")), 3**4)

    def test_all_characters_from_correct_sets(self):
        letters = self.sol.letterCombinations("2468")
        mapping = {0: "abc", 1: "ghi", 2: "mno", 3: "tuv"}
        for s in letters:
            for i, ch in enumerate(s):
                self.assertIn(ch, mapping[i])

    def test_no_duplicates(self):
        for digits in ("23", "2222", "999", "79"):
            letters = self.sol.letterCombinations(digits)
            self.assertEqual(len(letters), len(set(letters)))

    def test_all_digits_9(self):
        letters = self.sol.letterCombinations("99")
        self.assertEqual(len(letters), 16)
        self.assertEqual(set(letters), {a + b for a in "wxyz" for b in "wxyz"})


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Backtracking
