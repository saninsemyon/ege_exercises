#(y + 2x < A) ∨ (x > 30) ∨ (y > 20)


for a in range(0, 600):
    k = 0
    for x in range(0, 600):
        for y in range(0, 600):
            if (y + 2 * x < a) or (x > 30) or (y > 20):
                k += 1
    if k == 360000:
        print(a)
        break

