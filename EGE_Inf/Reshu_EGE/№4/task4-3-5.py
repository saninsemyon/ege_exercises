x = int(input())
if x > 0:
    y = 5 * x - 10
elif x == 0:
    y = 2
elif x < 0:
    y = 2 * abs(x) + 5
print(y)

