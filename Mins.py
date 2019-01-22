def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(res, *rest):
    for arg in rest:
        if arg < res:
            res = arg
    return res

def min3(*args):
    return sorted(args)[0]

print(min1([2, 2], [1, 1], [3, 3]))
print(min2([2, 2], [1, 1], [3, 3]))
print(min3([2, 2], [1, 1], [3, 3]))



print(min1(3, 4, 1, 2))
print(min2(3, 4, 1, 2))
print(min3(3, 4, 1, 2))


print(min1(['a'], {'a':'a'}, 'a', ('a')))
print(min2(['a'], {'a':'a'}, 'a', ('a')))
print(min3(['a'], {'a':'a'}, 'a', ('a')))
