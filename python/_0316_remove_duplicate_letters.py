# 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/
# Medium

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.removeDuplicateLetters("bcabc"), "abc")

    def test_example2(self):
        self.assertEqual(self.sol.removeDuplicateLetters("cbacdcbc"), "acdb")

    def test_single_char(self):
        self.assertEqual(self.sol.removeDuplicateLetters("a"), "a")

    def test_all_same(self):
        self.assertEqual(self.sol.removeDuplicateLetters("aaa"), "a")

    def test_no_duplicates(self):
        self.assertEqual(self.sol.removeDuplicateLetters("abc"), "abc")

    def test_reversed(self):
        self.assertEqual(self.sol.removeDuplicateLetters("cba"), "cba")

    def test_zzj_kk(self):
        self.assertEqual(self.sol.removeDuplicateLetters("bbcaac"), "bac")

    def test_already_sorted_with_dups(self):
        self.assertEqual(self.sol.removeDuplicateLetters("aab"), "ab")

    def test_long_single_repeats(self):
        self.assertEqual(self.sol.removeDuplicateLetters("a" * 10000), "a")

    def test_all_letters_once(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.sol.removeDuplicateLetters(s), s)

    def test_alternating(self):
        self.assertEqual(self.sol.removeDuplicateLetters("abab"), "ab")

    def test_need_to_pop_many(self):
        self.assertEqual(self.sol.removeDuplicateLetters("ecabbaac"), "eabc")

    def test_lexicographically_smallest(self):
        self.assertEqual(self.sol.removeDuplicateLetters("dcba"), "dcba")
        self.assertEqual(self.sol.removeDuplicateLetters("abcd"), "abcd")

    def test_mixed_order(self):
        self.assertEqual(self.sol.removeDuplicateLetters("cbabca"), "abc")

    def test_result_has_unique_chars(self):
        s = "cbacdcbc"
        res = self.sol.removeDuplicateLetters(s)
        self.assertEqual(len(res), len(set(res)))
        self.assertEqual(set(res), set(s))

    def test_case_50(self):
        self.assertEqual(self.sol.removeDuplicateLetters("adbbcac"), "adbc")


if __name__ == "__main__":
    unittest.main()

# Tags: String, Stack, Greedy, Monotonic Stack
