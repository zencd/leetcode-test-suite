# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Easy

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.firstUniqChar("leetcode"), 0)

    def test_example_2(self):
        self.assertEqual(self.sol.firstUniqChar("loveleetcode"), 2)

    def test_example_3(self):
        self.assertEqual(self.sol.firstUniqChar("aabb"), -1)

    def test_single_character(self):
        self.assertEqual(self.sol.firstUniqChar("a"), 0)

    def test_all_same_characters(self):
        self.assertEqual(self.sol.firstUniqChar("aaaa"), -1)

    def test_first_unique_before_end(self):
        self.assertEqual(self.sol.firstUniqChar("abca"), 1)

    def test_all_unique(self):
        self.assertEqual(self.sol.firstUniqChar("abcdef"), 0)

    def test_unique_in_middle(self):
        self.assertEqual(self.sol.firstUniqChar("zzabczz"), 2)

    def test_two_unique_characters(self):
        self.assertEqual(self.sol.firstUniqChar("aababc"), 5)

    def test_only_one_unique(self):
        self.assertEqual(self.sol.firstUniqChar("aabbaa"), -1)

    def test_unique_is_last_char(self):
        self.assertEqual(self.sol.firstUniqChar("aabbccz"), 6)

    def test_long_string_no_unique(self):
        s = "ab" * 50000
        self.assertEqual(self.sol.firstUniqChar(s), -1)

    def test_long_string_unique_at_end(self):
        s = "ab" * 49999 + "z"
        self.assertEqual(self.sol.firstUniqChar(s), 99998)

    def test_first_char_repeats_later(self):
        self.assertEqual(self.sol.firstUniqChar("abcabcabd"), 8)

    def test_all_letters_present_twice(self):
        s = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
        self.assertEqual(self.sol.firstUniqChar(s), -1)

    def test_unique_after_duplicates(self):
        self.assertEqual(self.sol.firstUniqChar("aabbcde"), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Queue, Counting
