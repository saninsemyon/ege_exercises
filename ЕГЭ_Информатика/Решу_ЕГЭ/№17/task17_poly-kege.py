with open ('../../Файлы_для_задач/17-345.txt') as f:
    s = [int(x) for x in f]
    maxi = max(t for t in s if t % 100 == 52)
    mini = min(t for t in s if t % 100 == 52)
    n = []
    for i in range(len(s) - 1):
        if ((s[i] < maxi - mini) and (s[i + 1] >= maxi - mini)) or ((s[i + 1] < maxi - mini) and (s[i] >= maxi - mini)):
            n.append(s[i] + s[i + 1])
print(len(n), max(n))

