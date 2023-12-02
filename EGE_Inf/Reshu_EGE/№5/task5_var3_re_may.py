for num in range(1, 1000):
    b = bin(num)[2:-1]
    if num % 2 != 0:
        b += '10'
    elif num % 2 == 0:
        b += '01'
    b = int(b, 2)
    if b == 2018:
        print(num)


#работает



