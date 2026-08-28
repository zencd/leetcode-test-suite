# 30. Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Hard

from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestFindSubstring(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(
            sorted(solution.findSubstring("barfoothefoobarman", ["foo", "bar"])), [0, 9]
        )

    def test_example2(self):
        solution = Solution()
        self.assertEqual(
            solution.findSubstring(
                "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]
            ),
            [],
        )

    def test_example3(self):
        solution = Solution()
        self.assertEqual(
            sorted(
                solution.findSubstring(
                    "barfoofoobarthefoobarman", ["bar", "foo", "the"]
                )
            ),
            [6, 9, 12],
        )

    def test_single_word(self):
        solution = Solution()
        self.assertEqual(sorted(solution.findSubstring("a", ["a"])), [0])

    def test_single_word_not_found(self):
        solution = Solution()
        self.assertEqual(solution.findSubstring("a", ["b"]), [])

    def test_single_word_multiple_occurrences(self):
        solution = Solution()
        self.assertEqual(sorted(solution.findSubstring("aaaa", ["aa"])), [0, 1, 2])

    def test_duplicate_words(self):
        solution = Solution()
        self.assertEqual(solution.findSubstring("abab", ["ab", "ab"]), [0])

    def test_duplicate_words_not_found(self):
        solution = Solution()
        self.assertEqual(solution.findSubstring("ab", ["ab", "ab"]), [])

    def test_empty_like_result(self):
        solution = Solution()
        self.assertEqual(solution.findSubstring("abc", ["def"]), [])

    def test_substring_longer_than_needed(self):
        solution = Solution()
        self.assertEqual(sorted(solution.findSubstring("abcabc", ["abc", "abc"])), [0])

    def test_adjacent_matches(self):
        solution = Solution()
        self.assertEqual(
            sorted(solution.findSubstring("ababab", ["ab", "ab", "ab"])), [0]
        )

    def test_interleaved_matches(self):
        solution = Solution()
        self.assertEqual(
            sorted(solution.findSubstring("abcabcabc", ["ab", "ca"])), [0, 3]
        )

    def test_word_longer_than_string(self):
        solution = Solution()
        self.assertEqual(solution.findSubstring("ab", ["abc"]), [])

    def test_exact_match(self):
        solution = Solution()
        self.assertEqual(solution.findSubstring("barfoo", ["foo", "bar"]), [0])

    def test_match_at_end(self):
        solution = Solution()
        self.assertEqual(solution.findSubstring("xxfoobar", ["bar", "foo"]), [2])

    def test_one_character_words(self):
        solution = Solution()
        self.assertEqual(sorted(solution.findSubstring("abab", ["a", "b"])), [0, 1, 2])

    def test_same_words_all(self):
        solution = Solution()
        self.assertEqual(solution.findSubstring("aaaa", ["a", "a", "a", "a"]), [0])

    def test_no_solution_case(self):
        solution = Solution()
        self.assertEqual(
            solution.findSubstring(
                "lingmaaplussolution", ["ling", "ma", "aplus", "solution"]
            ),
            [],
        )

    def test_repeated_valid_with_extra(self):
        solution = Solution()
        self.assertEqual(
            sorted(solution.findSubstring("foofoofoofoo", ["foo", "foo"])),
            [0, 3, 6],
        )

    def test_case_sensitive(self):
        solution = Solution()
        self.assertEqual(solution.findSubstring("BARFOO", ["bar", "foo"]), [])

    def test_many_words(self):
        solution = Solution()
        words = ["ab"] * 10
        self.assertEqual(sorted(solution.findSubstring("ab" * 10, words)), [0])

    def test_mixed_invalid_word_break(self):
        solution = Solution()
        self.assertEqual(
            sorted(solution.findSubstring("xxababab", ["ab", "ab", "ab"])),
            [2],
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Sliding Window
