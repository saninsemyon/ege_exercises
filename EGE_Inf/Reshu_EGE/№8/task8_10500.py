from itertools import product
words = '12345'
k = 0
for w in product(words, repeat=5):
    if w.count('1') == 3:
        k += 1
print(k)