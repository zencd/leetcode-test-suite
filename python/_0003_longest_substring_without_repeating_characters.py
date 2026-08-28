# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Medium

import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        raise Exception("Not solved yet")


class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_all_unique_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdefg"), 7)

    def test_example_abcabcbb(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_pwwkew(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_adbd(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("adbd"), 3)

    def test_two_repeating_pair(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abab"), 2)

    def test_dog(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("dog"), 3)

    def test_with_digits(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abc123def"), 9)

    def test_mixed_letters_digits_symbols(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a!1b!1c"), 4)

    def test_with_spaces(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a b c a"), 3)

    def test_repetition_only_at_start(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("aab"), 2)

    def test_repetition_only_at_end(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bba"), 2)

    def test_repeated_every_two(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abababab"), 2)

    def test_unique_then_duplicate(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcda"), 4)

    def test_long_unique_run_of_ten(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdefghij"), 10)

    def test_upper_and_lower_are_distinct(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("AaBb"), 4)
        self.assertEqual(self.solution.lengthOfLongestSubstring("Aa"), 2)
        self.assertEqual(self.solution.lengthOfLongestSubstring("AaAa"), 2)

    def test_punctuation(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(",. ,."), 3)

    def test_single_space(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(" "), 1)

    def test_two_spaces(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("  "), 1)

    def test_large_unique_string(self):
        s = "".join(chr(33 + i) for i in range(0, 94))
        s = s + s[:50]
        expected_max = 94
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected_max)

    def test_returns_integer(self):
        self.assertIsInstance(self.solution.lengthOfLongestSubstring("abc"), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Sliding Window
