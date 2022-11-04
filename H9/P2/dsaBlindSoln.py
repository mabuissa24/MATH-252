import random


def dsaBlind(p,q,g,A):
    # Creates a blind forgery for a DSA public key (the signature is valid but the text is unreadable)
    i = random.randint(1, q)
    j = random.randint(1, q)
    while modpow(j, -1, q) is None:
        j = random.randint(1, q)
    s1 = (modpow(g, i, p) * modpow(A, j, p)) % p % q
    s2 = (modpow(j, -1, q) * s1) % p % q
    d = (s1 * i * modpow(j, -1, q)) % q
    return d,s1,s2


def modpow(a,n,m):
    if n < 0:
        aInverse = inverse(a, m)
        a, n = aInverse, -n

    return modPowHelper(a, n, m) % m


def modPowHelper(a, n, m):
    if n == 1:  # BASE CASE
        return a
    if n == 0: # BASE CASE
        return 1
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
