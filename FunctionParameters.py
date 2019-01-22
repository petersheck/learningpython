def f(a):
    a = 99
    
b = 88
f(b)
print(b)

def changer(a, b):
    a = 2
    b[0] = 'spam'

X = 1
L = [1, 2]
print(X, L)
changer(X, L)
print(X, L)


def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y

X = 1
L = [1, 2]
print(X, L)
X, L = multiple(X, L)
print(X, L)

def defaults(a, b=2, c=3):
    print(a, b, c)
    
defaults(1)
defaults(a=1)
defaults(1, 4)
defaults(1, 4, 5)
defaults(1, c=6)
