'''
#РЕШУ ЕГЭ №

def f(n):
    if n > 1:
        return f(n - 1) + n
    else:
        return 1


print(f(40))
'''

'''
#РЕШУ ЕГЭ №4645

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n > 2:
        return f(n - 1) * n + f(n - 2) * (n - 1)


print(f(5))
'''

'''
#РЕШУ ЕГЭ №4656

def f(n):
    if n == 1:
        return 0
    elif n > 1:
        return f(n - 1) + n


def g(n):
    if n == 1:
        return 1
    elif n > 1:
        return g(n - 1) * n


print(f(5) + g(5))
'''

'''
# СБОРНИК КРЫЛОВА ВАР1 ЗАД16

def f(n):
    if n < 3:
        return n
    elif n > 2 and n % 2 == 0:
        return 2 * (n - 1) + f(n - 1) + 2
    elif n > 2 and n % 2 != 0:
        return 2 * (n + 1) + f(n - 2) - 5


print(f(32))
'''

'''
# СБОРНИК КРЫЛОВА ВАР2 ЗАД16

def f(n):
    if n < 3:
        return n
    elif n > 2 and n % 2 == 0:
        return 3 * (n - 1) + f(n - 1) + 5
    elif n > 2 and n % 2 != 0:
        return 3 * (n + 1) + f(n - 2) - 2


print(f(35))
'''

'''
# СБОНИК КРЫЛОВА ВАР3 ЗАД16

def f(n):
    if n < 3:
        return 1
    elif n > 2 and n % 2 != 0:
        return f(n - 1) + f(n - 2)
    elif n > 2 and n % 2 == 0:
        return sum(f(i) for i in range(1, n))


print(f(24))
'''

