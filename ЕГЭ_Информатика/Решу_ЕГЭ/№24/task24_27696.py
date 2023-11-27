f = open('../../Файлы_для_задач/zadanie24_2.txt')
s = f.readline()
maximum = curent = 1
for i in range(len(s) - 1):
    if s[i] == 'L' and s[i + 1] == 'L':
        curent += 1
        maximum = max(maximum, curent)
    else:
        curent = 1
print(maximum)