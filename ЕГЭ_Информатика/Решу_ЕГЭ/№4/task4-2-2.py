a = int(input())
b = int(input())
c = int(input())
if a == 0:
    if b == 0:
        if c == 0:
            print('БЕСКОНЕЧНО')
        else:
            print('РЕШЕНИЯ НЕТ')
    else:
        (-c / b)
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('РЕШЕНИЙ НЕТ')
    elif d == 0:
        print(-b / (2 * a))
    elif d > 0:
        print(-b + (d ** 0.5) / (2 * a), -b - (d ** 0.5) / (2 * a))

d.__abs__()




