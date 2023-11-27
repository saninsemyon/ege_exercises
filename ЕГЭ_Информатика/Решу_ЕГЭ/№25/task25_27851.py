for i in range(210235, 210301):
    m = []
    cnt = 0
    for n in range(2, i):
        if i % n == 0:
            cnt += 1
            m.append(n)
        if cnt > 4:
            break
    if cnt == 4:
        print(m)

'''
[2, 4, 52561, 105122]
[2, 4, 52567, 105134]
[2, 4, 52571, 105142]
'''

'''
for i in range(210235, 210301):
    k = 0
    a = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            k += 1
            a.append(j)
        if k > 4:
            break
    if k == 4:
        print(a)
'''
