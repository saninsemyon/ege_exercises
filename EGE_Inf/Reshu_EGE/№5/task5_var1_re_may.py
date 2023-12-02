for n in range(1, 100):
    s = bin(n)[2:]
    s = str(s)
    if s[-1] == '0': # Определение чётности бинарного числа по последней цифре
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    d = int(s, 2)
    print("d: ", d)
    if d > 52:
        print(n)
        break