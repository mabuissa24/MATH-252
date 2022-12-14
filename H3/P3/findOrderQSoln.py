import random

def findOrderQ(q,p):
    # Returns the order of q mod p
    if (p - 1) % q != 0:
        return None
    a = int(p * random.random())
    b = 1
    i = 0
    while b == 1 and i < 50:
        b = modpow(a, ((p - 1)//q), p)
        i = i + 1
    return b


def modpow(a,n,m):
    if n < 0:
        aInverse = inverse(a, m)
        if aInverse is None:
            print('Something went wrong')
        print("a * a^(-1) is ", ((a * aInverse) % m))
        a, n = aInverse, -n

    return modPowHelper(a, n, m)


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

