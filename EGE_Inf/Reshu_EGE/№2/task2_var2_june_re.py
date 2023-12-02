print('x y z')
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            F = (x == z) or (x <= (y and z))
            if F == 0:
                print(x, y, z)
