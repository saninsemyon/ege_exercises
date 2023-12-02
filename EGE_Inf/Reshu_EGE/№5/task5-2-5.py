'''
a = int(input())
if a < 100:
    b = a % 10
    c = a // 10
    print(b + c)
elif a >= 100:
    b = a % 10
    c = a // 100
    d = (a % 10) % 10
    print(b + c + d)
'''

# На вход подаётся число. Необходимо вычислить и вывести сумму цифр этого числа.

num = int(input())

#num = 999
num_str = str(num)
num_len = len(num_str)
summ = 0

# Iterate over the string
for element in num_str:
    mynum = int(element)
    summ += mynum

print(summ)
