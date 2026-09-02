# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/
# Medium

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        raise Exception("Not solved yet")


import unittest


def validate(s: str, result: str) -> tuple:
    if Counter(s) != Counter(result):
        return False, "result does not contain the same characters"
    seen = {}
    prev = float("inf")
    i = 0
    n = len(result)
    while i < n:
        ch = result[i]
        j = i
        while j < n and result[j] == ch:
            j += 1
        if ch in seen:
            return False, "character %r is not grouped together" % ch
        seen[ch] = j - i
        if seen[ch] > prev:
            return False, "frequencies are not non-increasing"
        prev = seen[ch]
        i = j
    return True, ""


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assertValid(self, s: str):
        result = self.sol.frequencySort(s)
        ok, reason = validate(s, result)
        self.assertTrue(ok, "%r -> %r: %s" % (s, result, reason))
        return result

    def test_tree(self):
        self.assertValid("tree")

    def test_cccaaa(self):
        result = self.assertValid("cccaaa")
        self.assertTrue(result in ("cccaaa", "aaaccc"), "got %r" % result)

    def test_aabb(self):
        result = self.assertValid("Aabb")
        self.assertTrue(result in ("bbAa", "bbaA"), "got %r" % result)

    def test_single_character(self):
        result = self.sol.frequencySort("a")
        self.assertEqual(result, "a")

    def test_all_same(self):
        result = self.sol.frequencySort("aaaaaa")
        self.assertEqual(result, "aaaaaa")

    def test_all_distinct(self):
        result = self.assertValid("abcdef")
        self.assertEqual(len(set(result)), 6)
        self.assertEqual(len(result), 6)

    def test_case_sensitive_letters(self):
        s = "AaA"
        result = self.assertValid(s)
        self.assertEqual(result, "AAa")

    def test_case_tie(self):
        s = "AAbb"
        result = self.assertValid(s)
        self.assertTrue(result == "AAbb" or result == "bbAA", "got %r" % result)

    def test_digits(self):
        result = self.assertValid("11223333")
        self.assertEqual(result, "33331122")

    def test_mixed_letters_and_digits(self):
        self.assertValid("a1b2a3b2a1")

    def test_two_frequencies(self):
        result = self.assertValid("aabbcccee")
        self.assertEqual(result[0], "c")
        self.assertTrue(result.startswith("ccc"))

    def test_large_input(self):
        s = "a" * 100000 + "b" * 99999 + "c" * 70000
        result = self.assertValid(s)
        self.assertEqual(len(result), 269999)
        self.assertTrue(result.startswith("a" * 100000))

    def test_palindrome(self):
        self.assertValid("aba")

    def test_unicode_digits(self):
        self.assertValid("0")

    def test_result_is_string(self):
        self.assertIsInstance(self.sol.frequencySort("abc"), str)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting
