L1 = []
print(L1)
L2 = [123, 'abc', 1.23, {}]
print(L2)
L3 = ['Bob', 40.0, ['dev', 'mgr']]
print(L3)
L4 = list('spam')
print(L4)
L5 = list(range(-4, 4))
print(L5)
L6 = L2 + L3
print(L6)
print(L6[6][0] + L6[6][1])
L7 = [1, 2, 3]
for x in L7:
    print(x)
L7.sort(reverse=True)
print(L7)
