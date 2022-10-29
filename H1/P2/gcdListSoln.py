def gcdList(ls):
    a, b = ls[0], ls[1]
    for n in ls:
        b = n
        while b != 0:
            a, b = b, a % b
    return a
