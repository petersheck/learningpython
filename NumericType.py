from decimal import Decimal
from fractions import Fraction
a = 1234
print(a)
b = 1.23
print(b)
c = 0o177
print(c)
d = 0x9ff
print(d)
e = 3+4j
print(e)
f = Decimal('1.0')
print(f)
g = Fraction(1, 3)
print(g)
print(a or b)
print(a and b)
print(not c)
print(a // b)
x = 17
div = x // 10
print(div)
rem = x % 10
rnd10 = 0
print(rem)
if rem < 5:
    rnd10 = div * 10
else:
    rnd10 = (div + 1) * 10
print(rnd10)
print(2 ** rnd10)
h = 40 + 3.14
print(h)
print(int(h))
print(float(h))


a = 3
b = 4
print(a + 1, a - 1)
print(b * 3, b / 2)
print(a % 2, b ** 2)
print(2 + 4.0, 2.0 ** b)

X = 2
Y = 4
Z = 6

print(X < Y < Z)
print(X < Y and Y < Z)
print(X < Y > Z)
print(X < Y and Y > Z)

print(1 == 2 < 3)

import math
print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))
print(math.trunc(5 / float(-2)))
print(int(5 / float(-2)))

print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144), math.sqrt(2))


import random
print(random.random())
print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 10))

movie = ['Life of Brian', 'Holy Grail', 'Meaning of Life']
print(random.choice(movie))
print(random.choice(movie))

suits = ['hearts', 'clubs', 'diamonds', 'spades']
print(suits)
random.shuffle(suits)
print(suits)

x = Fraction(1, 3)
y = Fraction(4, 6)
print(x)
print(y)
print(x + y)
print(x - y)
print(x * y)
z = Fraction(".25")
print(z)
z = Fraction("1.25")
print(z)

x = set("abcde")
print(x)
y = set("bdxyz")
print(y)
print("set difference = {}".format(x - y))
print(x | y)
print(x & y)
print(x ^ y)
print(x > y, x < y)
