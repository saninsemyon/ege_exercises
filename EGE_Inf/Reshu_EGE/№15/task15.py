for A in range(0, 500):
    for x in range(0, 500):
        for y in range(0, 500):
            a = True
            if ((y + 2 * x < A) or (x > 30) or (y > 20)) == False:
                a == False
                break
            if a == True:
                print(A)
                break
