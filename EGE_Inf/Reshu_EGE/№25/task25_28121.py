cnt = 0
for count in range(2422000, 2422081):
    m = 0
    for n in range(2, count):
        if count % n == 0:
            m += 1
            break
    if m == 0:
        cnt += 1
        print(count, cnt)

# Ответ
'''
2422027 1
2422033 2
2422037 3
2422073 4
'''

# Модифицированное решение с Решу ЕГЭ
'''
m = 0
for i in range(2422000, 2422081):
    k = 0
    for j in range(2, i):
        if i % j == 0:
            k += 1
            break
    if k == 0:
        m += 1
        print(i, m)
'''
