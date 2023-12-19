'''
# решу егэ №7933
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(2 * x - 1, y)


print(f(2, 9))
# 57
'''

'''
# решу егэ №13418
def f(x, y):
    if x > y or x == 26:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(2 * x + 1, y)


print(f(1, 27))
# 13
'''

'''
#решу егэ №11358
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
print(f(3, 10) * f(10, 12))
# 60
'''

'''
# решу егэ №59846

def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x - 2, y) + f(x - 3, y) + f(x // 3, y)


print(f(20, 3))
# 76
'''

'''
# решу егэ №59816

def f(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y) + f(x * 3, y)


print(f(7, 14) * f(14, 20))

# 18
'''

'''
# решу егэ №59772
def f(x, y):
    if x > y or x == 9 or x == 15:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y) + f(x * 3, y)


print(f(3, 18))

# 31
'''

'''
# решу егэ №59771
def f(x, y):
    if x > y or x == 9:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(x + 3, y) + f(x * 3, y)


print(f(3, 15) * f(15, 25))

# 63
'''

'''
# решу егэ №59770

def f(x, y):
    if x > y or x == 8:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
print(f(3, 14) * f(14, 18))

# 360
'''

'''
# рандом
def f(x, y):
    if x > y or x == 24:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(2 * x + 1, y)
print(f(1, 25))

# 10
'''

'''
# статград 23.1

def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y)
print(f(1, 10) * f(10, 23))

# 42
'''

'''
# статград 23.13
def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    z = 0
    if x > 4:
        z = f(x % 4, y)
    return f(x - 1, y) + f(x - 3, y) + z
print(f(22, 2))

# 1873
'''

'''
# статград №23.4

def c2(x):
    if str(x)[-2] != 9:
        return x + 10
    return x


def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1

    return f(x + 1, y) + f(c2(x), y)


print(f(12, 36))
# 31
'''

'''
# статград №23.24
def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x - 1, y) + f(x - 3, y) + f(x // 3, y)


print(f(22, 2))

#2196
'''
