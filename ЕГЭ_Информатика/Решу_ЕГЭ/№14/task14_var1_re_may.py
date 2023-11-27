s = 125 + 25 ** 3 + 5 ** 9
f = 0
while s:
    if s % 5 == 0:
        f += 1
    s //= 5
print(f)

#7