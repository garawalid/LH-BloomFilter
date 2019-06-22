import warnings

import numpy as np

from lhbf.hash_function import hash_str, hash_int


class BloomFilter():

    def __init__(self, m=10000, k=3):
        if m < 50:
            raise warnings.warn("Please choose a higher m to reduce the probability of two random elements colliding")
        self.m = m  # length of victor
        self.k = k  # number of hash functions
        self.vector = np.zeros(self.m, dtype=np.bool)  # vector of bits
        self.n = 0  # number of elements added to the bloom filter

    def estimate_fpp(self):
        return (1 - np.exp(-self.k * self.n / self.m)) ** self.k

    def _compute_hash(self, x):
        """
        Compute k hashes for x

        Parameters
        ----------
        x : str, int or None
            element

        Returns
        -------
        hash_values : list of hashes
        """
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
        """
        Add element x to the bloom filter

        Parameters
        ----------
        x : str, int or None
            element
        """
        hash_values = self._compute_hash(x)
        self.n += 1
        for idx in hash_values:
            self.vector[idx] = True

    def might_contain(self, x):
        """
        Check if x belongs to the bloom filter

        Parameters
        ----------
        x : str, int or None
            element

        Returns
        -------
        False means that the element definitely doesn't exist.
        True means that the element may exist
        """
        hash_values = self._compute_hash(x)

        for idx in hash_values:
            # If any result is equals to zero, then the element definitely doesn't exist.
            if bool(self.vector[idx]) == False:
                return False
        return True

    def combine(self, bloom_filter):
        """
        Combine two bloom filters

        Parameters
        ----------
        bloom_filter : BloomFilter
            Bloom filter to add
        """
        if self.m == bloom_filter.m and self.k == bloom_filter.k:
            self.vector = np.logical_or(self.vector, bloom_filter.vector)
        else:
            raise ValueError("Bloom filters should have the same parameters (m, k)")

    def save(self, file):
        """
        Save the bloom filter as binary file

        Parameters
        ----------
        file : file, str, or pathlib.Path
            File or filename to which the data is saved.  If file is a file-object,
            then the filename is unchanged.  If file is a string or Path, a ``.npy``
            extension will be appended to the file name if it does not already
            have one.
        """

        data = np.array([self.m, self.k, self.n])
        data = np.concatenate((data, self.vector), axis=0)
        np.save(file, data)

    def load(self, file):
        """
        Load a bloom filter from binary file

        Parameters
        ----------
        file : str
            The file to read. It should be in ``.npy`` foramt.
        """

        # Todo : check if the file is a bloom filter.
        data = np.load(file)
        self.m = data[0]
        self.k = data[1]
        self.n = data[2]
        self.vector = data[3:]

        return self
