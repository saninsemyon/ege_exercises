s = 9 ** 8 + 3 ** 5 - 9
f = 0
while s:
    if s % 3 == 2:
        f += 1
    s //= 3
print(f)

#3
