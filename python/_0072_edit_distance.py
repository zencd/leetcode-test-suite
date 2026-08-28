# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/
# Medium

import unittest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        raise Exception("Not solved yet")


class TestMinDistance(unittest.TestCase):
    def test_example_horse_ros(self):
        self.assertEqual(Solution().minDistance("horse", "ros"), 3)

    def test_example_intention_execution(self):
        self.assertEqual(Solution().minDistance("intention", "execution"), 5)

    def test_both_empty(self):
        self.assertEqual(Solution().minDistance("", ""), 0)

    def test_first_empty(self):
        self.assertEqual(Solution().minDistance("", "abc"), 3)

    def test_second_empty(self):
        self.assertEqual(Solution().minDistance("abc", ""), 3)

    def test_identical(self):
        self.assertEqual(Solution().minDistance("abc", "abc"), 0)

    def test_single_insert(self):
        self.assertEqual(Solution().minDistance("a", "ab"), 1)

    def test_single_delete(self):
        self.assertEqual(Solution().minDistance("ab", "a"), 1)

    def test_single_replace(self):
        self.assertEqual(Solution().minDistance("a", "b"), 1)

    def test_both_single_same(self):
        self.assertEqual(Solution().minDistance("a", "a"), 0)

    def test_all_replacements(self):
        self.assertEqual(Solution().minDistance("abc", "xyz"), 3)

    def test_insert_and_replace(self):
        self.assertEqual(Solution().minDistance("abc", "axc"), 1)

    def test_kitten_sitting(self):
        self.assertEqual(Solution().minDistance("kitten", "sitting"), 3)

    def test_flipped_operands(self):
        self.assertEqual(
            Solution().minDistance("ros", "horse"),
            Solution().minDistance("horse", "ros"),
        )

    def test_repeated_chars(self):
        self.assertEqual(Solution().minDistance("aaaa", "a"), 3)

    def test_repeated_chars_mismatch(self):
        self.assertEqual(Solution().minDistance("aaaa", "bbbb"), 4)

    def test_long_words(self):
        word1 = "a" * 500
        word2 = "b" * 500
        self.assertEqual(Solution().minDistance(word1, word2), 500)

    def test_large_insertion(self):
        word1 = "abc"
        word2 = "abxxyzccc"
        self.assertEqual(Solution().minDistance(word1, word2), 6)

    def test_symmetry(self):
        sol = Solution()
        self.assertEqual(
            sol.minDistance("flaw", "lawn"),
            sol.minDistance("lawn", "flaw"),
        )


if __name__ == "__main__":
    unittest.main()

# Tags: String, Dynamic Programming
