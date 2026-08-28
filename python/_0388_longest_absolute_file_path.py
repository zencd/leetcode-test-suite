# 388. Longest Absolute File Path
# https://leetcode.com/problems/longest-absolute-file-path/
# Medium

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"), 20
        )

    def test_example2(self):
        self.assertEqual(
            self.sol.lengthLongestPath(
                "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
            ),
            32,
        )

    def test_example3_only_directory(self):
        self.assertEqual(self.sol.lengthLongestPath("a"), 0)

    def test_empty_input(self):
        self.assertEqual(self.sol.lengthLongestPath(""), 0)

    def test_file_at_root(self):
        self.assertEqual(self.sol.lengthLongestPath("file.txt"), 8)

    def test_dot_in_name_treated_as_file(self):
        self.assertEqual(self.sol.lengthLongestPath("dir.name\n\tfile.txt"), 8)

    def test_multiple_files_pick_longest(self):
        inp = "a\n\tb.ext\n\tc\n\t\td\n\t\t\teee.ext"
        self.assertEqual(self.sol.lengthLongestPath(inp), 13)

    def test_single_directory_with_file(self):
        self.assertEqual(self.sol.lengthLongestPath("dir\n\tf.txt"), 9)

    def test_spaces_in_names(self):
        self.assertEqual(self.sol.lengthLongestPath("my dir\n\t my file .txt"), 20)

    def test_nested_deep(self):
        inp = "a\n\tb\n\t\tc\n\t\t\td\n\t\t\t\te.txt"
        self.assertEqual(self.sol.lengthLongestPath(inp), 13)

    def test_file_name_with_multiple_dots(self):
        self.assertEqual(self.sol.lengthLongestPath("a.txt.bak"), 9)

    def test_longer_siblings(self):
        inp = "dir\n\tshort\n\t\tfile.txt\n\tlongdirectory\n\t\tfile.txt"
        self.assertEqual(self.sol.lengthLongestPath(inp), 26)

    def test_no_files_multi_level(self):
        self.assertEqual(self.sol.lengthLongestPath("a\n\tb\n\t\tc"), 0)

    def test_mixed_levels(self):
        inp = "dir\n\tfile1.txt\n\tsub\n\t\tfile2.txt\n\tsubsub\n\t\tfile3.txt"
        self.assertEqual(self.sol.lengthLongestPath(inp), 20)


if __name__ == "__main__":
    unittest.main()

# Tags: String, Stack, Depth-First Search
