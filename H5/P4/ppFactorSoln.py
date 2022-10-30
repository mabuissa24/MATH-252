def ppFactor(N):
    # Your code here: make a list "factors"
    factors = []
    index = -1
    for i in range(2, 2**16):
        if N % i == 0:
            factors.append(1)
            index += 1
        while N % i == 0:
            N = N // i
            factors[index] = factors[index] * i
    return factors
