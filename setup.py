from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name='LessHash-BloomFilter',
        version='0.0.1',
        packages=find_packages(exclude=['tests']),
        license='Apache License v2',
        maintainer='Walid Gara',
        maintainer_email="",
        description = 'Fast Bloom Filter',
        url="https://github.com/garawalid/LH-BloomFilter"
    )
