for count in range(174457, 174505 + 1):
    a = []
    for j in range(2, count):
        if count % j == 0:
            a.append(j)
        if len(a) > 2:
            break
    if len(a) == 2:
        print(a)

'''
[3, 58153]
[7, 24923]
[59, 2957]
[13, 13421]
[149, 1171]
[5, 34897]
[211, 827]
[2, 87251]
'''