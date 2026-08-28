# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Easy

class Solution:
    def reverseVowels(self, s: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_char_vowel(self):
        self.assertEqual(self.sol.reverseVowels("a"), "a")

    def test_single_char_consonant(self):
        self.assertEqual(self.sol.reverseVowels("b"), "b")

    def test_no_vowels(self):
        self.assertEqual(self.sol.reverseVowels("xyz"), "xyz")

    def test_all_consonants(self):
        self.assertEqual(self.sol.reverseVowels("bcdfg"), "bcdfg")

    def test_single_vowel_with_consonants(self):
        self.assertEqual(self.sol.reverseVowels("hellO"), "hOlle")
        self.assertEqual(self.sol.reverseVowels("bcd"), "bcd")

    def test_all_vowels(self):
        self.assertEqual(self.sol.reverseVowels("aeiou"), "uoiea")
        self.assertEqual(self.sol.reverseVowels("AEIOU"), "UOIEA")
        self.assertEqual(self.sol.reverseVowels("aaaa"), "aaaa")

    def test_aeb_pair(self):
        self.assertEqual(self.sol.reverseVowels("aeb"), "eab")

    def test_mixed_case_vowels(self):
        self.assertEqual(self.sol.reverseVowels("aBcDe"), "eBcDa")

    def test_leetcode_example_1(self):
        self.assertEqual(self.sol.reverseVowels("IceCreAm"), "AceCreIm")

    def test_leetcode_example_2(self):
        self.assertEqual(self.sol.reverseVowels("leetcode"), "leotcede")

    def test_hello_example(self):
        self.assertEqual(self.sol.reverseVowels("hello"), "holle")

    def test_palindrome_vowels(self):
        self.assertEqual(self.sol.reverseVowels("aba"), "aba")
        self.assertEqual(self.sol.reverseVowels("racecar"), "racecar")
        self.assertEqual(self.sol.reverseVowels("yay"), "yay")

    def test_y_is_not_vowel(self):
        self.assertEqual(self.sol.reverseVowels("xyay"), "xyay")

    def test_spaces(self):
        self.assertEqual(self.sol.reverseVowels("a e i o u"), "u o i e a")
        self.assertEqual(self.sol.reverseVowels("a b c"), "a b c")

    def test_digits_and_ignored_punct(self):
        self.assertEqual(self.sol.reverseVowels("123abc"), "123abc")
        self.assertEqual(self.sol.reverseVowels("h3ll0W3rld"), "h3ll0W3rld")
        self.assertEqual(self.sol.reverseVowels("!a@b#c$d%e"), "!e@b#c$d%a")

    def test_symbols_reversed_with_vowels(self):
        self.assertEqual(self.sol.reverseVowels("h.e.l.l.o"), "h.o.l.l.e")

    def test_long_string(self):
        s = "a" * 1000 + "b" * 1000 + "e"
        expected = "e" + "a" * 999 + "b" * 1000 + "a"
        self.assertEqual(self.sol.reverseVowels(s), expected)

    def test_two_vowels_swap(self):
        self.assertEqual(self.sol.reverseVowels("ab"), "ab")
        self.assertEqual(self.sol.reverseVowels("abce"), "ebca")

    def test_idempotent_double_application(self):
        for s in ["aefih", "IceCreAm", "abcdefg"]:
            self.assertEqual(self.sol.reverseVowels(self.sol.reverseVowels(s)), s)

    def test_uppercase_mixed(self):
        self.assertEqual(self.sol.reverseVowels("LEETCODE"), "LEOTCEDE")

    def test_result_length_and_non_vowels_position(self):
        s = "aefih"
        result = self.sol.reverseVowels(s)
        self.assertEqual(len(result), len(s))
        self.assertEqual(result[2], "f")


if __name__ == "__main__":
    unittest.main()

# Tags: Two Pointers, String
