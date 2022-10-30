def disclog(g, h, p):
    gprev = g
    for i in range(2, p):
        newg = (gprev * g) % p
        gprev = newg

        if newg == h % p:
            return i
    return None


print(disclog(2, 893, 1373))
