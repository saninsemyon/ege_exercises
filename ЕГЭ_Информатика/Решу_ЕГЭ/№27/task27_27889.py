f = open('../../Файлы_для_задач/27-A_demo.txt')
n = int(f.readline())
min_sum = 0
razn = []
for s in f:
    a, b = map(int, s.split())
    min_sum += min(a, b)
    if abs(a - b) % 3 != 0:
        razn.append(abs(a - b))
print(min_sum)
print(min_sum + min(razn))












200157478