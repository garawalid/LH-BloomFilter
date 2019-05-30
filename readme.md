## Less Hash Bloom Filter

Less Hash Bloom Filter is fast bloom filter suitable for Big Data. 

The computation of hash functions and checking the existence of an element is a major computation overhead. 
Also, bloom filter requires multiple independent hash functions, and well-designed hash functions are computation-intensive like MD5, SHA-1 [1].  

In this implementation, we use a different technique to generate the k hash functions from only two. Therefore, the bloom filter is fast.

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
     
    <img src="http://www.sciweavers.org/tex2img.php?eq=g_i%28x%29%20%3D%20h_1%28x%29%20%2B%20i%20%5Ctimes%20h_2%28x%29%20%5Cmod%20m%20%5Ctextrm%7B%2C%20where%20%7D%200%20%20%20%5Cleq%20%20i%20%20%20%5Cleq%20%20k-1&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="g_i(x) = h_1(x) + i \times h_2(x) \mod m \textrm{, where } 0   \leq  i   \leq  k-1" width="442" height="19" />
    
    It has been proved that using this method doesn't increase the asymptotic false positive probability [4].


### Contributing
You're welcome to submit pull requests with any changes for this repository at any time. I'll be very glad to see any contributions.


### References

[1] []()
[2] []()
[3] []()
[4] []()
