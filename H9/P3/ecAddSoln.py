def ecAdd(P,Q,A,B,p):
    if P == 0:
        return Q
    if Q == 0:
        return P
    x1 = P[0]
    y1 = P[1]
    x2 = Q[0]
    y2 = Q[1]
    if x1 == x2 and y1 == (-1 * y2):
        return 0
    if P == Q:
        slope = ((3 * x1 * x1 + A) * modpow(2 * y1, -1, p)) % p
    elif x1 == x2:
        return 0
    else:
        slope = ((y2 - y1) * modpow(x2 - x1, -1, p)) % p
    x3 = (slope * slope - x1 - x2) % p
    return x3, (slope * (x1 - x3) - y1) % p
    # Should either return 0 (for point at infinity)
    #   or return (x,y), where x,y are in Z / p Z


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

