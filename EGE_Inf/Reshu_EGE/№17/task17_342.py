with open ('../../files_for_tasks/17-342.txt') as f:
    s = [int(x) for x in f]
    mini = min([t for t in s if t % 37 == 0])
    maxi = max([t for t in s if t % 73 == 0])
    n = []
    for i in range(len(s) - 1):
        if (maxi > s[i] > mini) and (maxi >= s[i + 1] >= mini) or (maxi >= s[i] >= mini) and (maxi > s[i + 1] > mini):
            n.append(s[i] + s[i + 1])
print(len(n), min(n))