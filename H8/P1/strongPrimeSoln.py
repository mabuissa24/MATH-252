import math
import random

def strongPrime(qbits,pbits):
    # Returns a prime with qbits bits, a prime with pbits bits, and a larger prime p such that the first divides p - 1 and the second divides p + 1
    q1 = randPrime(2 ** (qbits - 1), 2 ** qbits)
    q2 = randPrime(2 ** (qbits - 1), 2 ** qbits)
    a = crt(1, q1, -1, q2)
    kLowBound = (2 ** (pbits - 1) - a) // (q1 * q2) + 1
    kUpBound = (2 ** pbits - a) // (q1 * q2)
    for k in range(kLowBound, kUpBound):
        p = a + k * q1 * q2
        if isPrime(p, 10):
            return q1, q2, p
    return strongPrime(qbits, pbits)


def randPrime(lowBound, upBound):
    while True:
        p = random.randint(lowBound, upBound)
        if isPrime(p, 10):
            return p


def crt(a1,m1,a2,m2):
    if m1 < m2:
        temp1, temp2 = a1, m1
        a1, m1 = a2, m2
        a2, m2 = temp1, temp2
    i = ((a2 - a1) * modpow(m1, -1, m2)) % m2
    x = a1 + m1 * i
    return x


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


def is_witness(a,n):
    """Tells whether a is a M-R witness for n"""
    m = n-1
    while (m%2 == 0): m //= 2
    a = pow(a,m,n)
    if a == 1: return False
    while (m != n-1):
        if (a == n-1): return False
        a = (a*a)%n
        m *= 2
    return True

def isPrime(n, num_trials=10):
    if (n <= 2): return (n == 2)
    for i in range(num_trials):
        a = random.randint(2,n-1)
        if is_witness(a,n): return False
    return True
