with open ('../../files_for_tasks/17-345.txt') as f:
    s = [int(x) for x in f]
    maxi = max(t for t in s if t % 100 == 52)
    mini = min(t for t in s if t % 100 == 52)
    n = []
    for count in range(len(s) - 1):
        if ((s[count] < maxi - mini) and (s[count + 1] >= maxi - mini)) or ((s[count + 1] < maxi - mini) and (s[count] >= maxi - mini)):
            n.append(s[count] + s[count + 1])
print(len(n), max(n))

