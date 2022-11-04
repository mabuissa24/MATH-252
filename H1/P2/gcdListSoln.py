def gcdList(ls):
    # Returns the greatest common divisor of ls[0] and ls[1] 
    a, b = ls[0], ls[1]
    for n in ls:
        b = n
        while b != 0:
            a, b = b, a % b
    return a
