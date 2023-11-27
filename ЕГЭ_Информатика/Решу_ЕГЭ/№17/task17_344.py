with open ('../../Файлы_для_задач/17-344.txt') as f:
    s = [int(x) for x in f]
    mini = [t for t in s if t % 103 == 0]
    n = []
    for i in range(len(s) - 1):
        if (s[i] + s[i + 1]) % 2 == 0 and (abs(s[i] - abs(s[i + 1])) % min(mini) == 0):
            # print('append: ' + str(s[i] + s[i + 1]))
            n.append(s[i] + s[i + 1])
print(len(n), max(n))
