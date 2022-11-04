import math

def linearCong(m,b,N):
    # Solves congruence mx cong b (mod N) in the form x = sol mod N 
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
