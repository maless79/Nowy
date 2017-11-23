def silniaZ(n):
    if n > 1:
        return n * silniaZ(n - 1)
        print (n)
    else:
        print('wynik = ', n)
        return n