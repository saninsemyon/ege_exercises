#(x·y < 100) ∨ (y ≥ A) ∨ (x > A)


for A in range (0, 1000):
    a_podhodit = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (x * y < 100) or (y >= A) or (x > A) == False:
                a_podhodit = False
                break
        if a_podhodit == True:
            print(A)
            break
