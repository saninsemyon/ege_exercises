print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not(x) <= y) and (not(y) == z) and w)
                print(x, y, z, w, f)

