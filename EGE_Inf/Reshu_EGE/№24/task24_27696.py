f = open('../../files_for_tasks/zadanie24_2.txt')
s = f.readline()
maximum = curent = 1
for count in range(len(s) - 1):
    if s[count] == 'L' and s[count + 1] == 'L':
        curent += 1
        maximum = max(maximum, curent)
    else:
        curent = 1
print(maximum)