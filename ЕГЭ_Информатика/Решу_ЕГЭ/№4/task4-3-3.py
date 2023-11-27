
x = float(input())
y = float(input())

r = 5
num = (x ** 2) + (y ** 2)
sqrt = num ** (0.5)

if r < sqrt:
    print('НЕ ПРИНАДЛЕЖИТ')
else:
    print('ПРИНАДЛЕЖИТ')