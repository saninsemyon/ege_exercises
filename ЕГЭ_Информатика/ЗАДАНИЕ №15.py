for a in range(1, 100):
    for x in range(10000):
        f = ((x and 29 != 0) <= ((x and 17 == 0) <= (x and a != 0)))
        if f == 0:
            break
    else:
        print(a)