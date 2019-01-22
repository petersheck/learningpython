def findPrime(y):
    x = y // 2
    while x > 1:
        r = y % x
        print(y, x, r)
        if r == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')

findPrime(104729)
findPrime(34443524541)
