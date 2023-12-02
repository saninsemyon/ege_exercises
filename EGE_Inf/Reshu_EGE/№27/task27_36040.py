f = open('27_A.txt')
n = int(f.readline())
max_sum = 0
razn = []
for s in range(n):
    a, b, c = map(int, f.readline().split())
    max_sum += max(a, b, c)
    r = max(a, b, c) - min(a, b, c)
    if r % 109 != 0:
        razn.append(r)
    else: r = max(a, b, c) - (a + b + c - max(a, b, c) - min(a, b, c))
    if r % 109 != 0:
        razn.append(r)
    if max_sum % 109 != 0:
        print(max_sum)
    else:
        print(max_sum - min(razn))
