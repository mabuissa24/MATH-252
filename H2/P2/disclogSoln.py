def disclog(g, h, p):
    # Returns the discrete log of g with base h mod p
    gprev = g
    for i in range(2, p):
        newg = (gprev * g) % p
        gprev = newg
        if newg == h % p:
            return i
    return None
