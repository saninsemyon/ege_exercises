from itertools import product
a = 'АБВГД'
n = 0
for i in product(a, repeat=5):
    if (a[0] != 'A') and (i.count('А') == 1 and i.count('Б') == 1 and i.count('В') == 1 and i.count('Г') == 1 and i.count('Д') == 1):
        n += 1
print(n)

