from itertools import product
alphabet = '0123'
k = 0
for w in product(alphabet, repeat=3):
    if (w[0] != '0') and (int(w[0]) + int(w[-1]) > int(w[1])):
        k += 1
print(k)
