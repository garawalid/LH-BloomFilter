from hash_function import hash_int, hash_str
import numpy as np


class BloomFilter():

    def __init__(self, m, k):
        self.m = m  # length of victor
        self.k = k  # number of hash functions
        self.vector = np.zeros(self.m, dtype=np.bool)
        self.n = 0  # number of elements added to the bloom filter

    def estimate_fpp(self):
        return (1 - np.exp(-self.k * self.n / self.m)) ** self.k

    def _compute_hash(self, x):

        if x is None:
            x = 0

        if isinstance(x, str):
            h1_value = hash_str(x, p=53, m=self.m)
            h2_value = hash_str(x, p=31, m=self.m)

        elif isinstance(x, int):

            h1_value = hash_int(x, p=3)
            h2_value = hash_int(x, p=11)

        hash_values = []

        for i in range(0, self.k):
            hash_values.append((h1_value + i * h2_value) % self.m)

        return hash_values

    def add(self, x):
        hash_values = self._compute_hash(x)
        self.n += 1
        for idx in hash_values:
            self.vector[idx] = True

    def might_contain(self, x):
        hash_values = self._compute_hash(x)

        for idx in hash_values:
            # if any result is equals to zero, then the element definitely doesn't exist.
            if bool(self.vector[idx]) == False:
                return False
        return True

    def combine(self, bloom_filter):
        if self.m == bloom_filter.m and self.k == bloom_filter.k:
            self.vector = np.logical_or(self.vector, bloom_filter.vector)
        else:
            raise ValueError("Bloom filter should have the same parameters (m, k)")
