x = 25 ** 5 + 5 ** 14 - 5
k = 0
while x > 0:
    if x % 5 == 4:
        k += 1
    x //= 5
print(k)