# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Medium

class WordDictionary:
    def __init__(self):
        raise Exception("Not solved yet")

    def addWord(self, word: str) -> None:
        raise Exception("Not solved yet")

    def search(self, word: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example(self):
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        self.assertFalse(wd.search("pad"))
        self.assertTrue(wd.search("bad"))
        self.assertTrue(wd.search(".ad"))
        self.assertTrue(wd.search("b.."))

    def test_empty_dictionary(self):
        wd = WordDictionary()
        self.assertFalse(wd.search("a"))
        self.assertFalse(wd.search("."))
        self.assertFalse(wd.search(".."))

    def test_exact_match(self):
        wd = WordDictionary()
        wd.addWord("apple")
        self.assertTrue(wd.search("apple"))
        self.assertFalse(wd.search("app"))
        self.assertFalse(wd.search("apples"))
        self.assertFalse(wd.search("apply"))

    def test_word_prefix_of_another(self):
        wd = WordDictionary()
        wd.addWord("ab")
        self.assertFalse(wd.search("a"))
        wd.addWord("a")
        self.assertTrue(wd.search("a"))

    def test_single_letter(self):
        wd = WordDictionary()
        wd.addWord("a")
        self.assertTrue(wd.search("a"))
        self.assertTrue(wd.search("."))
        self.assertFalse(wd.search(".."))

    def test_all_dots(self):
        wd = WordDictionary()
        wd.addWord("cat")
        self.assertTrue(wd.search("..."))
        self.assertFalse(wd.search(".."))

    def test_dot_matches_any_letter(self):
        wd = WordDictionary()
        wd.addWord("dog")
        self.assertTrue(wd.search(".og"))
        self.assertTrue(wd.search("d.g"))
        self.assertTrue(wd.search("do."))
        self.assertFalse(wd.search(".ga"))
        self.assertFalse(wd.search("dox"))

    def test_multiple_dots(self):
        wd = WordDictionary()
        wd.addWord("hello")
        self.assertTrue(wd.search("h..lo"))
        self.assertTrue(wd.search("...lo"))
        self.assertTrue(wd.search("hell."))
        self.assertFalse(wd.search("hellz"))
        self.assertFalse(wd.search("helo."))
        self.assertFalse(wd.search("h..lx"))

    def test_dot_does_not_match_empty(self):
        wd = WordDictionary()
        wd.addWord("hi")
        self.assertFalse(wd.search("."))
        self.assertTrue(wd.search(".."))

    def test_multiple_words_same_prefix(self):
        wd = WordDictionary()
        for w in ["cat", "cot", "cut", "cart"]:
            wd.addWord(w)
        self.assertTrue(wd.search("c.t"))
        self.assertTrue(wd.search("ca."))
        self.assertFalse(wd.search("cta"))
        self.assertFalse(wd.search("c..a"))

    def test_dots_at_every_position_combo(self):
        wd = WordDictionary()
        wd.addWord("abc")
        expected = {
            "abc": True,
            ".bc": True,
            "a.c": True,
            "ab.": True,
            "..c": True,
            "a..": True,
            "...": True,
            ".a.": False,
            "b..": False,
            "abd": False,
            "ab": False,
            "abcd": False,
            "": False,
        }
        for pattern, expected_result in expected.items():
            self.assertEqual(wd.search(pattern), expected_result, pattern)

    def test_add_and_search_interleaved(self):
        wd = WordDictionary()
        self.assertFalse(wd.search("test"))
        wd.addWord("test")
        self.assertTrue(wd.search("test"))
        self.assertTrue(wd.search(".est"))
        wd.addWord("temp")
        self.assertTrue(wd.search("te.."))
        self.assertTrue(wd.search(".emp"))
        self.assertFalse(wd.search("..tp"))

    def test_two_dots_no_match(self):
        wd = WordDictionary()
        wd.addWord("abc")
        self.assertFalse(wd.search("a..d"))
        self.assertFalse(wd.search("d..c"))
        self.assertFalse(wd.search("b.."))

    def test_repeated_add_does_not_break(self):
        wd = WordDictionary()
        wd.addWord("abc")
        wd.addWord("abc")
        self.assertTrue(wd.search("abc"))
        self.assertTrue(wd.search(".bc"))

    def test_distinguishing_words_differ_by_one_letter(self):
        wd = WordDictionary()
        wd.addWord("a")
        wd.addWord("b")
        self.assertTrue(wd.search("."))
        self.assertTrue(wd.search("a"))
        self.assertFalse(wd.search("c"))

    def test_long_word(self):
        wd = WordDictionary()
        word = "a" * 25
        wd.addWord(word)
        self.assertTrue(wd.search(word))
        self.assertTrue(wd.search("." + "a" * 24))
        self.assertFalse(wd.search("a" * 24))
        self.assertFalse(wd.search("a" * 26))

    def test_search_pattern_longer_than_word(self):
        wd = WordDictionary()
        wd.addWord("go")
        self.assertFalse(wd.search("g.."))
        self.assertFalse(wd.search(".ot"))


if __name__ == "__main__":
    unittest.main()

# Tags: String, Depth-First Search, Design, Trie
