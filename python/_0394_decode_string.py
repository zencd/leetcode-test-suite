# 394. Decode String
# https://leetcode.com/problems/decode-string/
# Medium

class Solution:
    def decodeString(self, s: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.decodeString("3[a]2[bc]"), "aaabcbc")

    def test_example2(self):
        self.assertEqual(self.sol.decodeString("3[a2[c]]"), "accaccacc")

    def test_example3(self):
        self.assertEqual(self.sol.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_single_char(self):
        self.assertEqual(self.sol.decodeString("a"), "a")

    def test_single_repeat(self):
        self.assertEqual(self.sol.decodeString("3[a]"), "aaa")

    def test_only_letters(self):
        self.assertEqual(self.sol.decodeString("abc"), "abc")

    def test_repeat_of_letters(self):
        self.assertEqual(self.sol.decodeString("10[abcd]"), "abcd" * 10)

    def test_nested_deep(self):
        self.assertEqual(self.sol.decodeString("2[3[a]]"), "aaaaaa")

    def test_nested_mixed(self):
        self.assertEqual(self.sol.decodeString("3[2[x]2[y]]"), "xxyy" * 3)

    def test_multi_digit(self):
        self.assertEqual(self.sol.decodeString("100[a]"), "a" * 100)

    def test_multi_digit_nested(self):
        self.assertEqual(self.sol.decodeString("12[3[a]]"), "aaa" * 12)

    def test_letters_between_groups(self):
        self.assertEqual(self.sol.decodeString("ab2[c]"), "abcc")

    def test_nested_after_letters(self):
        self.assertEqual(self.sol.decodeString("2[a2[b3[c]]]d"), "abcccbccc" * 2 + "d")

    def test_single_digit_inner(self):
        self.assertEqual(self.sol.decodeString("a5[6[b]]"), "a" + "b" * 30)

    def test_large_repeat(self):
        self.assertEqual(self.sol.decodeString("300[a]"), "a" * 300)

    def test_consecutive_groups(self):
        self.assertEqual(self.sol.decodeString("2[a]3[b]"), "aabbb")

    def test_mixed_nested_and_outer(self):
        self.assertEqual(self.sol.decodeString("2[2[2[a]]]"), "a" * 8)

    def test_letters_inside_outer(self):
        self.assertEqual(self.sol.decodeString("a2[b]"), "abb")

    def test_deeply_nested_chain(self):
        self.assertEqual(self.sol.decodeString("2[2[2[2[a]]]]"), "a" * 16)

    def test_output_length_boundary(self):
        s = "2[100[2[a]]]300[ab]"
        self.assertEqual(len(self.sol.decodeString(s)), 1000)

    def test_validity_all_digits_in_range(self):
        self.assertEqual(len(self.sol.decodeString("300[2[a]]")), 600)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Stack, Recursion
