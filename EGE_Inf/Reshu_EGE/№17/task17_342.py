with open ('../../files_for_tasks/17-342.txt') as f:
    s = [int(x) for x in f]
    mini = min([t for t in s if t % 37 == 0])
    maxi = max([t for t in s if t % 73 == 0])
    n = []
    for count in range(len(s) - 1):
        if (maxi > s[count] > mini) and (maxi >= s[count + 1] >= mini) or (maxi >= s[count] >= mini) and (maxi > s[count + 1] > mini):
            n.append(s[count] + s[count + 1])
print(len(n), min(n))