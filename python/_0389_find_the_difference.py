# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Easy

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.findTheDifference("abcd", "abcde"), "e")

    def test_example2(self):
        self.assertEqual(self.solution.findTheDifference("", "y"), "y")

    def test_single_char_s(self):
        self.assertEqual(self.solution.findTheDifference("a", "aa"), "a")

    def test_added_at_start(self):
        self.assertEqual(self.solution.findTheDifference("bc", "abc"), "a")

    def test_added_at_end(self):
        self.assertEqual(self.solution.findTheDifference("ab", "abb"), "b")

    def test_added_in_middle(self):
        self.assertEqual(self.solution.findTheDifference("ac", "aac"), "a")

    def test_all_same_letters(self):
        self.assertEqual(self.solution.findTheDifference("aaaa", "aaaaa"), "a")

    def test_duplicated_existing_letter(self):
        self.assertEqual(self.solution.findTheDifference("aab", "aabb"), "b")

    def test_duplicated_a_in_empty_like(self):
        self.assertEqual(self.solution.findTheDifference("a", "ba"), "b")

    def test_all_twenty_six_letters(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        t = "zabcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.solution.findTheDifference(s, t), "z")

    def test_long_strings(self):
        s = "a" * 1000
        t = "b" + "a" * 1000
        self.assertEqual(self.solution.findTheDifference(s, t), "b")

    def test_long_strings_middle_insertion(self):
        s = "xy" * 500
        t = s[:500] + "z" + s[500:]
        self.assertEqual(self.solution.findTheDifference(s, t), "z")

    def test_only_two_letters(self):
        self.assertEqual(self.solution.findTheDifference("ab", "bab"), "b")

    def test_random_seeded(self):
        import random

        for seed in range(20):
            random.seed(seed)
            n = random.randint(1, 100)
            s = "".join(random.choice("abcde") for _ in range(n))
            added = random.choice("abcdefg")
            pos = random.randint(0, n)
            t = s[:pos] + added + s[pos:]
            self.assertEqual(self.solution.findTheDifference(s, t), added)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Bit Manipulation, Sorting
