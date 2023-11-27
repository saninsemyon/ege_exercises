with open('../../Файлы_для_задач/17.txt') as f:
    s = [int(x) for x in f]
    n = []
    maxi = 0
    for i in range(len(s)):
        s[i] = int(s[i])
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if ((s[i] - s[j]) % 45 == 0) and (s[i] % 18 == 0 or s[j] % 18 == 0):
                n.append(s[i] + s[j])
                maxi = max(maxi, abs(s[i] - s[j]))
print(len(n), maxi)