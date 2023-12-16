with open ('../../files_for_tasks/17-344.txt') as f:
    s = [int(x) for x in f]
    mini = [t for t in s if t % 103 == 0]
    n = []
    for count in range(len(s) - 1):
        if (s[count] + s[count + 1]) % 2 == 0 and (abs(s[count] - abs(s[count + 1])) % min(mini) == 0):
            # print('append: ' + str(s[i] + s[i + 1]))
            n.append(s[count] + s[count + 1])
print(len(n), max(n))
