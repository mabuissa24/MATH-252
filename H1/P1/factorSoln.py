import math


def factor(n):
    # Your code here. Find p and q with p,q > 1 and pq = n.
    # The order of p and q does not matter (e.g. if n=35, either 3,5 or 5,3 will be accepted)
    sqrt = math.ceil(math.sqrt(n))
    for i in range(2, sqrt):
        if n % i == 0:
            return i, n // i