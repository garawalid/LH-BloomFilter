from lhbf import BloomFilter
import unittest
from numpy.testing import assert_array_equal


class BloomTest(unittest.TestCase):

    @property
    def bf(self):
        bf = BloomFilter(m=100, k=2)
        examples = [1, 2, 3, 4, 5, 6]

        for e in examples:
            bf.add(e)

        return bf

    def test_bloom_str(self):
        bf = BloomFilter(m=200, k=2)

        examples = ["a", "b", "c", "d", "e"]
        for e in examples:
            bf.add(e)

        not_included = ["h", "g", "k", "l"]

        for e in not_included:
            assert (bf.might_contain(e) == False)

    def test_bloom_int(self):
        bf = BloomFilter(m=200, k=2)
        examples = [1, 2, 3, -4, -5, 6]

        for e in examples:
            bf.add(e)

        not_included = [10, 11, 15, 16, 19]

        for e in not_included:
            assert (bf.might_contain(e) == False)

        assert (bf.might_contain(-4) == True)

    def test_bloom_none(self):
        bf = BloomFilter(m=200, k=2)
        examples = [1, 2, None, -4, -5, 6]

        for e in examples:
            bf.add(e)

        not_included = [10, 11, 15, 16, 19]

        for e in not_included:
            assert (bf.might_contain(e) == False)

        assert (bf.might_contain(None) == True)

    def test_estimate_fpp(self):
        bf = BloomFilter(m=200, k=2)
        examples = [1, 2, 3, -4, -5, 6]

        for e in examples:
            bf.add(e)
        fpp_expected = 0.003391369548660095
        fpp = bf.estimate_fpp()
        assert (fpp == fpp_expected)
        assert (fpp >= 0.0 and fpp <= 1.0)

    def test_combine(self):
        bf1 = BloomFilter(m=100, k=2)
        examples = [1, 2, 3, 4, 5, 6]

        for e in examples:
            bf1.add(e)

        bf2 = BloomFilter(m=100, k=2)
        examples = [100, 200, 300, 400]

        for e in examples:
            bf2.add(e)

        bf1.combine(bf2)

        not_included = [10, 11, 15, 16, 19]

        for e in not_included:
            assert (bf1.might_contain(e) == False)

        assert (bf1.might_contain(4) == True)
        assert (bf1.might_contain(300) == True)

        bf1 = BloomFilter(m=80, k=2)
        bf2 = BloomFilter(m=90, k=2)

        msg = "Bloom filter should have the same parameters (m, k)"
        with self.assertRaises(ValueError, msg=msg):
            bf1.combine(bf2)

    def test_save_load(self):

        self.bf.save('bf.npy')
        bf_new = BloomFilter().load('bf.npy')

        assert_array_equal(bf_new.vector, self.bf.vector)
        assert (bf_new.m == self.bf.m)
        assert (bf_new.k == self.bf.k)
        assert (bf_new.n == self.bf.n)
