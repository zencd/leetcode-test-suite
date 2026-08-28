# 38. Count and Say
# https://leetcode.com/problems/count-and-say/
# Medium

import unittest


class Solution:
    def countAndSay(self, n: int) -> str:
        raise Exception("Not solved yet")


class TestCountAndSay(unittest.TestCase):
    def test_n1(self):
        self.assertEqual(Solution().countAndSay(1), "1")

    def test_n2(self):
        self.assertEqual(Solution().countAndSay(2), "11")

    def test_n3(self):
        self.assertEqual(Solution().countAndSay(3), "21")

    def test_n4(self):
        self.assertEqual(Solution().countAndSay(4), "1211")

    def test_n5(self):
        self.assertEqual(Solution().countAndSay(5), "111221")

    def test_n6(self):
        self.assertEqual(Solution().countAndSay(6), "312211")

    def test_n7(self):
        self.assertEqual(Solution().countAndSay(7), "13112221")

    def test_n8(self):
        self.assertEqual(Solution().countAndSay(8), "1113213211")

    def test_n9(self):
        self.assertEqual(Solution().countAndSay(9), "31131211131221")

    def test_n10(self):
        self.assertEqual(Solution().countAndSay(10), "13211311123113112211")

    def test_n30_length(self):
        self.assertEqual(len(Solution().countAndSay(30)), 4462)

    def test_result_digits_only(self):
        self.assertTrue(Solution().countAndSay(10).isdigit())

    def test_result_string_type(self):
        self.assertIsInstance(Solution().countAndSay(1), str)

    def test_all_valid_n_are_digits(self):
        for n in range(1, 15):
            self.assertTrue(Solution().countAndSay(n).isdigit())


if __name__ == "__main__":
    unittest.main()

# Tags: String
