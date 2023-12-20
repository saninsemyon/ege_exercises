with open('../../files_for_tasks/17.txt') as f:
    s = [int(x) for x in f]
    n = []
    maxi = 0
    for count in range(len(s)):
        s[count] = int(s[count])
    for count in range(len(s) - 1):
        for j in range(count + 1, len(s)):
            if ((s[count] - s[j]) % 45 == 0) and (s[count] % 18 == 0 or s[j] % 18 == 0):
                n.append(s[count] + s[j])
                maxi = max(maxi, abs(s[count] - s[j]))
print(len(n), maxi)