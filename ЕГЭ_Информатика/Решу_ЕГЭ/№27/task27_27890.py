f = open('27-B_1(1).txt')
n = int(f.readline())
max_sum = 0
razn = []
for s in f:
    a, b = map(int, s.split())
    max_sum += max(a, b)
    if abs(a - b) % 5 != 0:
        razn.append(abs(a - b))
if max_sum % 5 != 0:
    print(max_sum)
else:
    print(max_sum - min(razn))


