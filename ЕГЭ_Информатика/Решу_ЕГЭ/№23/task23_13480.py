def f(x, y):
    if x > y or x == 26:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(2 * x + 1, y)

print(f(1, 27))

#13