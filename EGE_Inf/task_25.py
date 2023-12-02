# НАЧАЛО РЕШЕНИЯ!

t, b = 0, 0

'''
'РЕШУ ЕГЭ №27422'

a = 174457
b = 174505
for i in range(a, b + 1):
    c = 0
    diff = []
    for j in range(2, i):
        if i % j == 0:
            c += 1
            diff.append(j)
    if c == 2:
        print(*diff)
'''

'''
'РЕШУ ЕГЭ №27850'

a = 245690
b = 245756
ind = []
all = []
valid = []
for i in range(a, b + 1):
    c = 0
    all.append(i)
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
    if c == 2:
        ind.append(all.index(i) + 1)
        valid.append(i)
print(*ind, sep='\n')
print()
print(*valid, sep='\n')
'''

'''
'РЕШУ ЕГЭ №27853'

a = 312614
b = 312651
for i in range(a, b + 1):
    c = 0
    diff = []
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
            diff.append(j)
    if c == 6:
        print(*diff)
'''

'''
'РЕШУ ЕГЭ №28124'

c1 = 0
valid = []
for i in range(568023, 569230 + 1):
    c2 = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c2 += 1
    if c2 > c1:
        c1 = c2
        valid.append(i)
print(c1, max(valid))
'''

'''
'РЕШУ ЕГЭ №33527'

a = 101000000
b = 102000000
valid = []
for i in range(a, b + 1):
    c = 0
    for j in range(2, i + 1, 2):
        if i % j == 0:
            c += 1
    if c == 3:
        valid.append(i)
print(*valid, sep='\n')
'''

'''
'РЕШУ ЕГЭ №36038'

valid = []
mvalid = []
for i in range(452022, 452065):
    deliteli = []
    for j in range(2, i):
        if i % j == 0:
            deliteli.append(j)
    if len(deliteli) > 0:
        maxi = max(deliteli)
        mini = min(deliteli)
        m = maxi + mini
        if m % 7 == 3:
            valid.append(i)
            mvalid.append(m)
    else:
        m = 0
        continue
print(valid)
print(mvalid)
'''

#решу егэ №29673

