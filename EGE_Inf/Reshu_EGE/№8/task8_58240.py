from itertools import product
alphabet = '012345678'
k = 0
for count in product(alphabet, repeat=5):
    if count[0] != '0' and int(count[0]) > int(count[1]) > int(count[2]) > int(count[3]) > int(count[4]):
        k += 1
print(k)