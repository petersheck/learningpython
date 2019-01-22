s = 'abc'
t = 'def'
print(len(s))
print(s + t)
print(s * 4)
print('-' * 80)
myjob = 'developer'
z = ''
for c in myjob:
    z = z + c + ' '
print(z)
print(myjob[0], myjob[-2])

print(myjob[1:3], myjob[1:], myjob[:-1])
n = len(myjob)
print(myjob[::2])
print(myjob[0:n:2])
print(myjob[1:n:2])
print(myjob[::-1])
print('This is %d %s bird' % (1, 'funny'))
print('This is {} {} bird'.format(1, 'crazy'))
S = 'spam'
print(S.find('pa'))
S = 'spammy'
L = list(S)
print(L)
L[3] = 'x'
L[4] = 'x'
print(L)
S = ''.join(L)
print(S)
