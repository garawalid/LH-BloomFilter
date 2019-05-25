def hash_int(x, p):
    """
    Compute the hash of an integer. The hashing method is Knuth multiplicative hash.

    Parameters
    ----------
    x : int
        element
    p : int
        Prime number used for shifting. Recommended p is 53 or 31.

    Returns
    -------
    hash : hash value of x
    """
    if x < 0:
        x *= -1
    if 0 <= p <= 32:
        return (x * 2654435769) >> (32 - p)
    else:
        raise ValueError("The prime number p should be between 0 and 32.")


def hash_str(x, p, m):
    """
       Compute the hash of a string with polynomial rolling hash function.

       Parameters
       ----------
       x : str
           element
       p : int
           Prime number. Recommended p is 53.
       m : int
           The size of hashing space. Usually, The size of the bloom filter.

       Returns
       -------
       hash : hash value of x
       """
    hash_value = 0
    p_i = p
    for c in x:
        hash_value += (ord(c) * p_i) % m
        p_i = (p_i * p) % m

    try:
        hash_value = int(hash_value)
        return hash_value
    except:
        raise TypeError("Can't cast {} to integer".format(type(hash_value)))
