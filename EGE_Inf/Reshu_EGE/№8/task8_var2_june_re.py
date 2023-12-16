from itertools import product
a = 'АБВГД'
n = 0
for count in product(a, repeat=5):
    if (a[0] != 'A') and (count.count('А') == 1 and count.count('Б') == 1 and count.count('В') == 1 and count.count('Г') == 1 and count.count('Д') == 1):
        n += 1
print(n)

