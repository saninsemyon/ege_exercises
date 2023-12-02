x = 9 ** 12 + 3 ** 8 - 3
k = 0
while x > 0:
    if x % 3 == 2:
        k += 1
    x //= 3
print(k)