from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()


if __name__ == "__main__":

    setup(
        name='LessHash-BloomFilter',
        version='0.0.3',
        packages=find_packages(exclude=['tests']),
        license='Apache License v2',
        maintainer='Walid Gara',
        maintainer_email="",
        description = 'Fast Bloom Filter',
        url="https://github.com/garawalid/LH-BloomFilter",
        download_url ="https://github.com/garawalid/LH-BloomFilter/archive/v0.0.3.tar.gz",
        long_description=long_description,
        long_description_content_type='text/markdown'
    )
