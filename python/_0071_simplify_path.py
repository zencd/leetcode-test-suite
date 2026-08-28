# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/
# Medium

class Solution:
    def simplifyPath(self, path: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSimplifyPath(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_trailing_slash(self):
        self.assertEqual(self.solution.simplifyPath("/home/"), "/home")

    def test_multiple_consecutive_slashes(self):
        self.assertEqual(self.solution.simplifyPath("/home//foo/"), "/home/foo")

    def test_double_period(self):
        self.assertEqual(
            self.solution.simplifyPath("/home/user/Documents/../Pictures"),
            "/home/user/Pictures",
        )

    def test_parent_from_root(self):
        self.assertEqual(self.solution.simplifyPath("/../"), "/")

    def test_ellipsis_is_valid_name(self):
        self.assertEqual(
            self.solution.simplifyPath("/.../a/../b/c/../d/./"), "/.../b/d"
        )

    def test_root_only(self):
        self.assertEqual(self.solution.simplifyPath("/"), "/")

    def test_single_directory(self):
        self.assertEqual(self.solution.simplifyPath("/home"), "/home")

    def test_single_period_only(self):
        self.assertEqual(self.solution.simplifyPath("/./"), "/")

    def test_current_directory_in_path(self):
        self.assertEqual(self.solution.simplifyPath("/a/./b"), "/a/b")

    def test_multiple_periods_not_special(self):
        self.assertEqual(self.solution.simplifyPath("/four/dot//....//.."), "/four/dot")

    def test_four_dots_is_valid_name(self):
        self.assertEqual(self.solution.simplifyPath("/...."), "/....")

    def test_many_parents_from_root(self):
        self.assertEqual(self.solution.simplifyPath("/..../.."), "/")

    def test_parent_exceeding_depth_ignored(self):
        self.assertEqual(self.solution.simplifyPath("/a/b/../../.."), "/")

    def test_parent_then_new_subdir(self):
        self.assertEqual(self.solution.simplifyPath("/a/b/../c/../../d"), "/d")

    def test_leading_slashes(self):
        self.assertEqual(self.solution.simplifyPath("///home"), "/home")

    def test_interior_multiple_slashes(self):
        self.assertEqual(self.solution.simplifyPath("/a///b////c"), "/a/b/c")

    def test_current_directory_at_start(self):
        self.assertEqual(self.solution.simplifyPath("/./home"), "/home")

    def test_current_directory_in_middle(self):
        self.assertEqual(self.solution.simplifyPath("/a/./b/./c"), "/a/b/c")

    def test_current_directory_at_end(self):
        self.assertEqual(self.solution.simplifyPath("/a/b/."), "/a/b")

    def test_deep_path(self):
        self.assertEqual(self.solution.simplifyPath("/a/b/c/d/e/f"), "/a/b/c/d/e/f")

    def test_mixed_periods_and_slashes(self):
        self.assertEqual(self.solution.simplifyPath("/a/.//../b/./c/../../d/.."), "/")

    def test_all_slashes(self):
        self.assertEqual(self.solution.simplifyPath("////"), "/")

    def test_dots_in_name_preserved(self):
        self.assertEqual(self.solution.simplifyPath("/file.txt/../dir2"), "/dir2")

    def test_name_with_dots_kept(self):
        self.assertEqual(self.solution.simplifyPath("/a.b/c.d"), "/a.b/c.d")

    def test_single_char_directories(self):
        self.assertEqual(self.solution.simplifyPath("/a/b/c/../d"), "/a/b/d")

    def test_parent_at_various_positions(self):
        self.assertEqual(self.solution.simplifyPath("/a/../a/b"), "/a/b")

    def test_name_with_underscore_and_digits(self):
        self.assertEqual(
            self.solution.simplifyPath("/dir_1/sub_2/../sub_3"), "/dir_1/sub_3"
        )

    def test_upper_and_lower_case_names(self):
        self.assertEqual(
            self.solution.simplifyPath("/Home/USER/documents"), "/Home/USER/documents"
        )


if __name__ == "__main__":
    unittest.main()

# Tags: String, Stack
