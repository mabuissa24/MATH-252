import math


def bsgs(g,h,p):
    # your code here
    return bsgsBoundedOrder(g, h, p, p - 1)


def bsgsBoundedOrder(g,h,p,q):
    n = math.ceil(math.sqrt(q))
    first = dict()
    second = dict()
    u = modpow(g, -1 * n, p)
    key1 = g
    key2 = (h * u) % p
    for i in range(1, n + 1):
        first[key1] = i
        second[key2] = i
        if key1 in second:
            j = second[key1]
            return i + n * j
        elif key2 in first:
            j = first[key2]
            return j + n * i
        key1 = (key1 * g) % p
        key2 = (key2 * u) % p
    return None


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
