s = '0123456789abcde'
for x in s:
    k1 = '123' + x + '5'
    k2 = '1' + x + '233'
    f = int(k1, 15) + int(k2, 15)
    if f % 14 == 0:
        print(f // 14)
        break

