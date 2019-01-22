import math

def findPrimeV2(y):
    n = math.sqrt(y)
    i = 2;
    while i <= n:
        r = y % i
        print(y, i, r)
        if r == 0:
            print(y, 'has factor', i)
            break
        i += 1
    else:
        print(y, 'is prime')

findPrimeV2(104729)
findPrimeV2(34443524541)
