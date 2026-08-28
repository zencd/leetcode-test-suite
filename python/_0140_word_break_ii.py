# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/
# Hard

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_one(self):
        res = set(
            self.sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        )
        self.assertEqual(res, {"cats and dog", "cat sand dog"})

    def test_example_two(self):
        res = set(
            self.sol.wordBreak(
                "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
            )
        )
        self.assertEqual(
            res,
            {
                "pine apple pen apple",
                "pineapple pen apple",
                "pine applepen apple",
            },
        )

    def test_example_three(self):
        res = self.sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        self.assertEqual(res, [])

    def test_single_letter(self):
        self.assertEqual(self.sol.wordBreak("a", ["a"]), ["a"])

    def test_single_letter_no_match(self):
        self.assertEqual(self.sol.wordBreak("a", ["b"]), [])

    def test_single_word_whole_string(self):
        self.assertEqual(self.sol.wordBreak("abc", ["abc"]), ["abc"])

    def test_reuse_of_words(self):
        res = set(self.sol.wordBreak("aaaa", ["a", "aa", "aaaa"]))
        expected = {
            "a a a a",
            "a a aa",
            "a aa a",
            "aa a a",
            "aa aa",
            "aaaa",
        }
        self.assertEqual(res, expected)

    def test_empty_result_mixed(self):
        res = self.sol.wordBreak("ab", ["a", "b", "ab"])
        expected = {"a b", "ab"}
        self.assertEqual(set(res), expected)

    def test_duplicates_in_dictionary_ignored(self):
        res = self.sol.wordBreak("ab", ["ab"])
        self.assertEqual(res, ["ab"])

    def test_word_longer_than_suffix(self):
        self.assertEqual(self.sol.wordBreak("abc", ["abcd"]), [])

    def test_no_split_possible_but_single_word(self):
        self.assertEqual(self.sol.wordBreak("leet", ["leet"]), ["leet"])

    def test_multiple_segmentations_long(self):
        res = set(self.sol.wordBreak("aaaaaaaaaaa", ["a", "aa", "aaa"]))
        count = self._composition_count(11)
        self.assertEqual(len(res), count)
        for sentence in res:
            self.assertTrue(
                all(part in {"a", "aa", "aaa"} for part in sentence.split(" "))
            )

    @staticmethod
    def _composition_count(n, parts=(1, 2, 3)):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = sum(dp[i - p] for p in parts if i - p >= 0)
        return dp[n]

    def test_all_sentences_valid(self):
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        for sentence in self.sol.wordBreak(s, wordDict):
            parts = sentence.split(" ")
            self.assertTrue(all(p in wordDict for p in parts))
            self.assertEqual("".join(parts), s)

    def test_max_length_string(self):
        wordDict = ["a", "ab", "abc", "abcd", "abcde"]
        res = self.sol.wordBreak("a" * 20, wordDict)
        self.assertTrue(len(res) > 0)
        for sentence in res:
            self.assertEqual("".join(sentence.split(" ")), "a" * 20)

    def test_word_not_reusable_more_than_needed(self):
        res = self.sol.wordBreak("catcat", ["cat"])
        self.assertEqual(res, ["cat cat"])

    def test_single_split(self):
        self.assertEqual(self.sol.wordBreak("ab", ["ab", "b"]), ["ab"])

    def test_two_word_split(self):
        self.assertEqual(self.sol.wordBreak("abb", ["ab", "b"]), ["ab b"])

    def test_order_irrelevance(self):
        r1 = set(
            self.sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        )
        r2 = set(
            self.sol.wordBreak("catsanddog", ["dog", "sand", "and", "cats", "cat"])
        )
        self.assertEqual(r1, r2)

    def test_empty_sentence_not_returned(self):
        res = self.sol.wordBreak("a", ["a"])
        self.assertNotIn("", res)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, String, Dynamic Programming, Backtracking, Trie, Memoization
