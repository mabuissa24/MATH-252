def modpow(a,n,m):
    # Returns a^n(mod m) 
    if n < 0:
        aInverse = inverse(a, m)
        if aInverse is None:
            print('Something went wrong')
        print("a * a^(-1) is ", ((a * aInverse) % m))
        a, n = aInverse, -n
    return modPowHelper(a, n, m)


def modPowHelper(a, n, m):
    # A helper method to compute the modular power
    if n == 1:  # Base case 
        return a
    sqrt = modPowHelper(a, n // 2, m) # Recursive step 
    ans = (sqrt * sqrt) % m
    if n % 2 == 1:
        ans = ans * a
    return ans % m


def inverse(a, b):  # Return the inverse of a mod b using the Euclidean algorithm 
    first = [a, 1, 0]
    second = [b, 0, 1]
    while second[0] > 0:
        temp = second
        a = first[0]
        b = second[0]
        ratio = a // b
        second = [a % b, first[1] - ratio * second[1], first[2] - ratio * second[2]]
        first = temp
    if first[0] != 1:
        return None
    else:
        return first[1]
