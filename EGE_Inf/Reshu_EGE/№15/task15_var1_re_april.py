for a in range(0, 1000):
    a_norm = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x < 6) <= (x ** 2 < a) and (y ** 2 <= a) <= (y <= 6)) == False:
                a_norm == False
                break
        if a_norm == False:
            break
    if a_norm == True:
        print(a)