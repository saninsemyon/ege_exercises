with open ('../../Файлы_для_задач/17(3).txt') as f:
    s = [int(x) for x in f]
    max_sum = []
    n = 0
    for x in range(len(s) - 1):
        if ((abs(s[x] - s[x + 1])) % 2 == 0) and (s[x] % 19 == 0 or s[x + 1] % 19 == 0):
            n += 1
            max_sum.append(s[x] + s[x + 1])
    print(n, max(max_sum))
