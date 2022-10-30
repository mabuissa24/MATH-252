import math


def extractKey(p,g,A,d1,s11,s12,d2,s21,s22):
    aFactor, M = linearCong(s21 * s12 - s11 * s22, d2 * s12 - d1 * s22, p - 1)
    a = aFactor
    while True:
        a = a + M
        if modpow(g, a, p) == A:
            return a


def linearCong(m,b,N):
    gcd = math.gcd(m, N)
    # m / gcd * x = b / gcd + kN / gcd
    if b % gcd != 0:
        return None
    m = m // gcd
    b = b // gcd
    N = N // gcd
    mInv = inverse(m, N)
    sol = (b * mInv) % N
    return sol, N

    # The function should either "return None" or "return r,M", where the solution is x = r momod M.


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