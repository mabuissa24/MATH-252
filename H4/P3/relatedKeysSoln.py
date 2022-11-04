import sys


def relatedkeys(g,p,A,c11,c12,m1,c21,c22):
    # Returns the decrypted message assuming that we know that the second ephemeral message is u(k) + v for some u and v between 1 and 100
    for u in range(1, 100):  # Find u, v that work
        for v in range(1, 100):
            rightSide = (modpow(c11, u, p) * modpow(g, v, p)) % p
            if c21 % p == rightSide:
                break
        if c21 % p == rightSide:
            break
    m2 = (modpow(m1, -1, p) * c12) % p
    m2 = (modpow(m2, u, p) * modpow(A, v, p)) % p
    m2 = modpow(m2, -1, p)
    m2 = (m2 * c22) % p
    return m2


def modpow(a,n,m):
    if n < 0:
        aInverse = inverse(a, m)
        a, n = aInverse, -n

    return modPowHelper(a, n, m) % m


def modPowHelper(a, n, m):
    if n == 1:  # BASE CASE
        return a
    sqrt = modPowHelper(a, n // 2, m)
    ans = (sqrt * sqrt) % m
    if n % 2 == 1:
        ans = ans * a
    return ans % m


def inverse(a, b):  # Return the inverse of a mod b
    first = [a, 1, 0]
    second = [b, 0, 1]
    while second[0] > 0:
        temp = second
        a = first[0]
        b = second[0]
        ratio = a // b
        second = [a % b, first[1] - ratio * second[1], first[2] - ratio * second[2]]
        first = temp
    # Your code here
    if first[0] != 1:
        return None
    else:
        return first[1]
