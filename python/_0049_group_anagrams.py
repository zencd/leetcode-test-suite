# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Medium

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        raise Exception("Not solved yet")


if __name__ == "__main__":
    import unittest

    class TestGroupAnagrams(unittest.TestCase):
        def setUp(self):
            self.sol = Solution()

        def assertGroupsEqual(self, result, expected):
            def canon(groups):
                return sorted(tuple(sorted(g)) for g in groups)

            self.assertEqual(canon(result), canon(expected))

        def test_example1(self):
            self.assertGroupsEqual(
                self.sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            )

        def test_single_empty_string(self):
            self.assertGroupsEqual(self.sol.groupAnagrams([""]), [[""]])

        def test_single_character(self):
            self.assertGroupsEqual(self.sol.groupAnagrams(["a"]), [["a"]])

        def test_multiple_empty_strings(self):
            self.assertGroupsEqual(self.sol.groupAnagrams(["", "", ""]), [["", "", ""]])

        def test_all_same_string(self):
            self.assertGroupsEqual(
                self.sol.groupAnagrams(["abc", "abc", "abc"]), [["abc", "abc", "abc"]]
            )

        def test_no_anagrams(self):
            self.assertGroupsEqual(
                self.sol.groupAnagrams(["ab", "cd", "ef"]), [["ab"], ["cd"], ["ef"]]
            )

        def test_single_chars_no_anagram(self):
            self.assertGroupsEqual(
                self.sol.groupAnagrams(["a", "b", "c"]), [["a"], ["b"], ["c"]]
            )

        def test_same_char_repeated(self):
            self.assertGroupsEqual(
                self.sol.groupAnagrams(["aa", "a", "aaa"]),
                [["aa"], ["a"], ["aaa"]],
            )

        def test_palindromes_and_anagrams(self):
            self.assertGroupsEqual(
                self.sol.groupAnagrams(["aba", "baa", "aab"]), [["aba", "baa", "aab"]]
            )

        def test_duplicates_in_groups_preserved(self):
            self.assertEqual(
                sorted(
                    [len(g) for g in self.sol.groupAnagrams(["b", "a", "a", "b", "c"])]
                ),
                [1, 2, 2],
            )

        def test_long_string(self):
            s = "a" * 100
            s2 = "b" + "a" * 99
            result = self.sol.groupAnagrams([s, s2, s])
            self.assertGroupsEqual(result, [[s, s], [s2]])

        def test_result_is_list_of_lists(self):
            result = self.sol.groupAnagrams(["eat", "tea"])
            self.assertIsInstance(result, list)
            for g in result:
                self.assertIsInstance(g, list)

        def test_input_not_mutated(self):
            strs = ["eat", "tea", "bat"]
            snapshot = list(strs)
            self.sol.groupAnagrams(strs)
            self.assertEqual(strs, snapshot)

    unittest.main()

# Tags: Array, Hash Table, String, Sorting
