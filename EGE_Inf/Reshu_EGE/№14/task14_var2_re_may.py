s = 49 ** 7 + 7 ** 20 - 28
f = 0
while s:
    if s % 7 == 6:
        f += 1
    s //= 7
print(f)

#12