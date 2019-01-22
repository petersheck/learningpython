def summation(L):
    if not L:
        return 0;
    else:
        return L[0] + summation(L[1:]);

n = summation([1, 2, 3, 4, 5])
print(n)

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

n = sumtree([1, [2, 3, [4, 5], 6, [7, 8, [9, 10]]]])
print(n)

def breathFirst(L):
    tot = 0;
    queue = list(L)
    while queue:
        front = queue.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            queue.extend(front)
    return tot


n = breathFirst([1, [2, 3, [4, 5], 6, [7, 8, [9, 10]]]])
print(n)

def depthFirst(L):
    tot = 0;
    stack = list(L)
    while stack:
        front = stack.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            stack[:0] = front
    return tot

n = depthFirst([1, [2, 3, [4, 5], 6, [7, 8, [9, 10]]]])
print(n)
