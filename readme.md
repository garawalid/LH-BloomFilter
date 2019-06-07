## Less Hash Bloom Filter
[![Build Status](https://travis-ci.com/garawalid/LH-BloomFilter.svg?branch=master)](https://travis-ci.com/garawalid/LH-BloomFilter)

Less Hash Bloom Filter is fast bloom filter suitable for Big Data. 

The computation of hash functions and checking the existence of an element is a major computation overhead. 
Also, bloom filter requires multiple independent hash functions, and well-designed hash functions are computation-intensive like MD5, SHA-1 [1].  

In this implementation, we use a different technique to generate the k hash functions from only two. Therefore, the bloom filter is fast.

### Install

Install Less Hash Bloom Filter with pip as follows:
```
$ pip install LessHash-BloomFilter
```

### Usage

LHBF needs to know the size of bloom filter `m` and number of hash functions `k`.

**Note:** You should use high `m` to avoid the collision of hash functions. The probability of two random strings colliding is ~ 1/m



```python
from lhbf import BloomFilter

# Create a bloom filter 
bf = BloomFilter(m=200, k=2)

# Add an element
bf.add("a")

# Check if element exists
bf.might_contain("a")

# Estimate flase positive probability 
bf.estimate_fpp()

# Combine two bloom filters
bf2 = BloomFilter(m=200, k=2)
bf.combine(bf2)

```

### Details

+ Hash functions used: 
    + For integer, we use **Knuth multiplicative hash** [2]
    + For string, we use **polynomial rolling hash function** [3]

+ k hash functions:  

    Using two hash functions, we calculate the k hash functions as follows: 
    
    *g<sub>i</sub>(x) = h<sub>1</sub>(x) + i x h<sub>2</sub>(x) mod m, where 0 &le; i &le; k-1*  
    
    It has been proved that using this method does not increase the asymptotic false positive probability [4].


### Contributing
You're welcome to submit pull requests with any changes for this repository at any time. I'll be very glad to see any contributions.


### References

+ [1] Luo, Lailong, et al. Optimizing bloom filter: challenges, solutions, and comparisons. IEEE Communications Surveys & Tutorials (2018).  
+ [2] Knuth, Donald Ervin. The art of computer programming: sorting and searching. Vol. 3. Pearson Education, 1997.
+ [3] Karp, Richard M., and Michael O. Rabin. Efficient randomized pattern-matching algorithms. IBM journal of research and development 31.2 (1987): 249-260.  
+ [4] Kirsch, Adam, and Michael Mitzenmacher. Less hashing, same performance: building a better bloom filter. European Symposium on Algorithms. Springer, Berlin, Heidelberg, 2006.
