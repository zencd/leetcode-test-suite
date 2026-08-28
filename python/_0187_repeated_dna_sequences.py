# 187. Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/
# Medium

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        raise Exception("Not solved yet")


import unittest


def reference(s: str) -> List[str]:
    cnt = {}
    for i in range(len(s) - 9):
        w = s[i : i + 10]
        cnt[w] = cnt.get(w, 0) + 1
    return [w for w, c in cnt.items() if c > 1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        self.assertEqual(
            sorted(self.sol.findRepeatedDnaSequences(s)), ["AAAAACCCCC", "CCCCCAAAAA"]
        )

    def test_example2(self):
        s = "AAAAAAAAAAAAA"
        self.assertEqual(self.sol.findRepeatedDnaSequences(s), ["AAAAAAAAAA"])

    def test_one_char(self):
        self.assertEqual(self.sol.findRepeatedDnaSequences("A"), [])

    def test_nine_chars(self):
        self.assertEqual(self.sol.findRepeatedDnaSequences("ACGTACGTA"), [])

    def test_exactly_ten_chars(self):
        self.assertEqual(self.sol.findRepeatedDnaSequences("ACGTACGTAC"), [])

    def test_ten_chars_all_A(self):
        self.assertEqual(self.sol.findRepeatedDnaSequences("AAAAAAAAAA"), [])

    def test_eleven_all_A(self):
        self.assertEqual(
            self.sol.findRepeatedDnaSequences("AAAAAAAAAAA"), ["AAAAAAAAAA"]
        )

    def test_no_repeats(self):
        s = "ACGTGCGTACG"
        self.assertEqual(self.sol.findRepeatedDnaSequences(s), [])

    def test_multiple_repeats(self):
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        result = self.sol.findRepeatedDnaSequences(s)
        self.assertEqual(len(result), 2)
        self.assertIn("AAAAACCCCC", result)
        self.assertIn("CCCCCAAAAA", result)

    def test_all_same_twelve(self):
        s = "AAAAAAAAAAAA"
        self.assertEqual(self.sol.findRepeatedDnaSequences(s), ["AAAAAAAAAA"])

    def test_all_same_sixteen(self):
        s = "A" * 16
        self.assertEqual(self.sol.findRepeatedDnaSequences(s), ["AAAAAAAAAA"])

    def test_duplicate_not_listed_twice(self):
        s = "AAAAAAAAAAAAAAAA"
        self.assertEqual(self.sol.findRepeatedDnaSequences(s).count("AAAAAAAAAA"), 1)

    def test_overlapping_repeats(self):
        s = "AAAAACCCCCAAAAACCCCC"
        expected = reference(s)
        self.assertEqual(sorted(self.sol.findRepeatedDnaSequences(s)), sorted(expected))

    def test_distinct_repeated_sequences(self):
        s = "ACCGCACCGCACCGC"
        self.assertEqual(
            sorted(self.sol.findRepeatedDnaSequences(s)), sorted(reference(s))
        )

    def test_result_strings_valid(self):
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        for seq in self.sol.findRepeatedDnaSequences(s):
            self.assertEqual(len(seq), 10)
            self.assertTrue(all(c in "ACGT" for c in seq))

    def test_long_random_no_crash(self):
        import random

        random.seed(42)
        s = "".join(random.choice("ACGT") for _ in range(100000))
        result = self.sol.findRepeatedDnaSequences(s)
        self.assertIsInstance(result, list)
        self.assertEqual(set(result), set(reference(s)))

    def test_matches_reference_on_generated_cases(self):
        import random

        random.seed(7)
        for trial in range(200):
            n = random.randint(1, 60)
            s = "".join(random.choice("ACGT") for _ in range(n))
            self.assertEqual(
                set(self.sol.findRepeatedDnaSequences(s)),
                set(reference(s)),
                "mismatch for %r" % s,
            )

    def test_boundary_lengths(self):
        for s in ("ACGT", "ACGTACGT", "ACGTACG", ""):
            self.assertEqual(self.sol.findRepeatedDnaSequences(s), [])


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash Function, Z Algorithm, Boyer–Moore String-Search Algorithm
