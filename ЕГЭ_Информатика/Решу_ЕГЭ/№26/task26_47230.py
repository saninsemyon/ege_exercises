with open ('../../Файлы_для_задач/26(1).txt') as f:
    n = [int(x) for x in f]
    n = sorted(n[1:], reverse=True)
    k, mini = 1, n[0]
    for i in range(1, len(n)):
        if n[i] + 3 <= mini:
            k += 1
            mini = n[i]
print(k, mini)