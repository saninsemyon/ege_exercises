print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x or not(z)) and (x == not(w)) and (x <= y))
                if f == 0:
                print(x, y, z, w)