def main():
    base = 3
    mod = 43
    res = 1
    for i in range(1, mod):
        res = (res * base) % mod
        print(res)


main()

