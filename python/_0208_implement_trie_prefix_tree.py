# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Medium

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        raise Exception("Not solved yet")

    def insert(self, word: str) -> None:
        raise Exception("Not solved yet")

    def search(self, word: str) -> bool:
        raise Exception("Not solved yet")

    def startsWith(self, prefix: str) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_empty_trie_search(self):
        trie = Trie()
        self.assertFalse(trie.search("a"))
        self.assertFalse(trie.search("abc"))

    def test_empty_trie_starts_with(self):
        trie = Trie()
        self.assertFalse(trie.startsWith("a"))
        self.assertFalse(trie.startsWith("apple"))

    def test_insert_then_search(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))

    def test_search_not_inserted(self):
        trie = Trie()
        trie.insert("apple")
        self.assertFalse(trie.search("app"))
        self.assertFalse(trie.search("apply"))
        self.assertFalse(trie.search("bpple"))
        self.assertFalse(trie.search("applepie"))

    def test_starts_with(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.startsWith("app"))
        self.assertTrue(trie.startsWith("ap"))
        self.assertTrue(trie.startsWith("a"))
        self.assertTrue(trie.startsWith("apple"))
        self.assertFalse(trie.startsWith("apply"))
        self.assertFalse(trie.startsWith("bpple"))
        self.assertFalse(trie.startsWith("banana"))

    def test_insert_word_then_search_word(self):
        trie = Trie()
        trie.insert("apple")
        self.assertFalse(trie.search("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))
        self.assertTrue(trie.search("apple"))

    def test_example_sequence(self):
        trie = Trie()
        trie.insert("apple")
        results = [trie.search("apple"), trie.search("app"), trie.startsWith("app")]
        trie.insert("app")
        results.append(trie.search("app"))
        self.assertEqual(results, [True, False, True, True])

    def test_startswith_after_prefix_inserted(self):
        trie = Trie()
        trie.insert("app")
        self.assertTrue(trie.startsWith("app"))
        self.assertTrue(trie.startsWith("a"))
        self.assertFalse(trie.startsWith("apple"))

    def test_insert_empty_string(self):
        trie = Trie()
        trie.insert("")
        self.assertTrue(trie.search(""))
        trie2 = Trie()
        self.assertFalse(trie2.search(""))

    def test_search_empty_without_insert(self):
        trie = Trie()
        self.assertFalse(trie.search(""))

    def test_starts_with_empty(self):
        trie = Trie()
        trie.insert("a")
        self.assertTrue(trie.startsWith(""))

    def test_duplicate_insert(self):
        trie = Trie()
        trie.insert("cat")
        trie.insert("cat")
        trie.insert("cat")
        self.assertTrue(trie.search("cat"))
        self.assertTrue(trie.startsWith("cat"))

    def test_single_char_words(self):
        trie = Trie()
        trie.insert("a")
        self.assertTrue(trie.search("a"))
        self.assertTrue(trie.startsWith("a"))
        self.assertFalse(trie.search("b"))
        self.assertFalse(trie.startsWith("b"))

    def test_shared_prefixes(self):
        trie = Trie()
        words = ["cat", "catfish", "concatenate"]
        for w in words:
            trie.insert(w)
        for w in words:
            self.assertTrue(trie.search(w))
        self.assertTrue(trie.startsWith("cat"))
        self.assertTrue(trie.startsWith("c"))
        self.assertTrue(trie.startsWith("concatenate"))
        self.assertFalse(trie.startsWith("dog"))
        self.assertFalse(trie.search("cats"))
        self.assertFalse(trie.search("catfis"))

    def test_overlapping_prefix_and_word(self):
        trie = Trie()
        trie.insert("a")
        trie.insert("aa")
        trie.insert("aaa")
        self.assertTrue(trie.search("a"))
        self.assertTrue(trie.search("aa"))
        self.assertTrue(trie.search("aaa"))
        self.assertFalse(trie.search("aaaa"))
        self.assertTrue(trie.startsWith(""))

    def test_many_words(self):
        trie = Trie()
        words = ["bat", "ball", "band", "banana", "apple", "application", "app", "ap"]
        for w in words:
            trie.insert(w)
        for w in words:
            self.assertTrue(trie.search(w))
        self.assertFalse(trie.search("ban"))
        self.assertFalse(trie.search("ballz"))
        self.assertTrue(trie.startsWith("ban"))
        self.assertTrue(trie.startsWith("appl"))
        self.assertFalse(trie.startsWith("zzz"))

    def test_word_removed_from_search_by_prefix_boundary(self):
        trie = Trie()
        trie.insert("dog")
        self.assertTrue(trie.search("dog"))
        self.assertFalse(trie.search("dogs"))
        trie.insert("dogs")
        self.assertTrue(trie.search("dogs"))
        self.assertTrue(trie.search("dog"))

    def test_max_length_word(self):
        trie = Trie()
        long_word = "a" * 2000
        trie.insert(long_word)
        self.assertTrue(trie.search(long_word))
        self.assertTrue(trie.startsWith("a" * 1999))
        self.assertFalse(trie.search("a" * 2001))
        self.assertFalse(trie.startsWith("a" * 2001))

    def test_all_letters(self):
        trie = Trie()
        import string

        for ch in string.ascii_lowercase:
            trie.insert(ch)
        for ch in string.ascii_lowercase:
            self.assertTrue(trie.search(ch))


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Design, Trie
