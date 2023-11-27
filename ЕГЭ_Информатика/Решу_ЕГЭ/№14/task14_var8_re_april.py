x = 9 ** 8 * 3 ** 20 - 3 ** 10 - 3
k = 0
while x > 0:
    if x % 3 == 2:
        k += 1
    x //= 3
print(k)