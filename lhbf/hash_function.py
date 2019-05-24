def hash_int(x, p):
    if x < 0:
        x *= -1
    return (x * 2654435769) >> (32 - p)


def hash_str(x, p, m):
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
