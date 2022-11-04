import math


def factor(n):
    # Returns p and q with p,q > 1 and pq = n.
    sqrt = math.ceil(math.sqrt(n))
    for i in range(2, sqrt):
        if n % i == 0:
            return i, n // i
