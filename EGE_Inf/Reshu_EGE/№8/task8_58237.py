from itertools import product
alphabet = product('0123456', repeat=4)
k = 0
for w in alphabet:
    word = ''.join(w)
    if word[3] > word[2] and word[2] > word[1] and word[1] > word[0]:
        k += 1
print(k)