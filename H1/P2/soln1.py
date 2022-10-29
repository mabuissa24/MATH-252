def numdivs(n):
    count = 0
    d = 1
    while d*d < n:
        if n%d == 0:
            count += 2
        d += 1
        if d*d == n:
            count += 1
    return count
