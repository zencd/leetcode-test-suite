# 395. Longest Substring with At Least K Repeating Characters
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Medium

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.longestSubstring("aaabb", 3), 3)

    def test_example2(self):
        self.assertEqual(self.sol.longestSubstring("ababbc", 2), 5)

    def test_all_satisfy(self):
        self.assertEqual(self.sol.longestSubstring("a", 1), 1)

    def test_k_greater_than_length(self):
        self.assertEqual(self.sol.longestSubstring("aab", 4), 0)

    def test_k_one_returns_full_length(self):
        self.assertEqual(self.sol.longestSubstring("abcabc", 1), 6)

    def test_single_character_repeated(self):
        self.assertEqual(self.sol.longestSubstring("aaaa", 4), 4)

    def test_single_character_repeated_not_enough(self):
        self.assertEqual(self.sol.longestSubstring("aaa", 4), 0)

    def test_mixed_all_meet(self):
        self.assertEqual(self.sol.longestSubstring("aabbbcc", 2), 7)

    def test_only_substring_meets(self):
        self.assertEqual(self.sol.longestSubstring("ababacb", 3), 0)

    def test_split_on_invalid_char(self):
        self.assertEqual(self.sol.longestSubstring("aaabbbcccd", 3), 9)

    def test_invalid_in_middle(self):
        self.assertEqual(self.sol.longestSubstring("abac", 2), 0)

    def test_two_valid_parts(self):
        self.assertEqual(self.sol.longestSubstring("aaabbbaaccc", 3), 11)

    def test_two_valid_parts_with_gap(self):
        self.assertEqual(self.sol.longestSubstring("aaabbbaaccccdd", 3), 12)
        self.assertEqual(self.sol.longestSubstring("aaabcdddee", 3), 3)

    def test_no_character_meets(self):
        self.assertEqual(self.sol.longestSubstring("abcdef", 2), 0)

    def test_all_distinct_k1(self):
        self.assertEqual(self.sol.longestSubstring("abcdef", 1), 6)

    def test_eceba(self):
        self.assertEqual(self.sol.longestSubstring("eceba", 2), 0)

    def test_long_uniform_string(self):
        s = "a" * 10000
        self.assertEqual(self.sol.longestSubstring(s, 9999), 10000)

    def test_long_uniform_string_shortfall(self):
        s = "a" * 9999
        self.assertEqual(self.sol.longestSubstring(s, 10000), 0)

    def test_long_mixed(self):
        s = "ab" * 5000
        self.assertEqual(self.sol.longestSubstring(s, 2), 10000)

    def test_long_mixed_k3(self):
        s = ("ab" * 5000) + "c"
        self.assertEqual(self.sol.longestSubstring(s, 3), 10000)

    def test_recursion_limit_check(self):
        s = "".join(
            chr(ord("a") + ((i >> j) & 1)) for j in range(10) for i in range(200)
        )
        res = self.sol.longestSubstring(s, 2)
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, len(s))

    def test_deep_recursion_split(self):
        s = ""
        expected = 0
        n = 100
        for i in range(n):
            s += chr(ord("a") + i % 3)
        res = self.sol.longestSubstring(s, 3)
        self.assertIsInstance(res, int)
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, len(s))

    def test_k_zero_not_in_constraints_but_still_consistent(self):
        self.assertEqual(self.sol.longestSubstring("abc", 0), 3)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Divide and Conquer, Sliding Window
