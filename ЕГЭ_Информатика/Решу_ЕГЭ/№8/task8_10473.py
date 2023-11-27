from itertools import product
words = product('1234', repeat=5)
k = 0
for w in words:
    word = ''.join(w)
    if word.count('1') == 2:
        k += 1
print(k)