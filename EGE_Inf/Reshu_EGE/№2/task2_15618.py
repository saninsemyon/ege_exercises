print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((x and (not(y))) or (y == z) or (not(w))) == 0:
                    print(w, x, y, z)
# wzyx
