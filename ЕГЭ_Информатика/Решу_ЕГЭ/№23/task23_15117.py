def f(x, y):
    if x > y or x == 15:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y)

print(f(3, 9) * f(9, 20))

#520