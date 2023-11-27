'''
#вар 1, крылов, чуркина

print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (x and (y <= z) and ((not y) <= ((not z) == w)))
                print(w, x, y, z, int(f))
# x z y w
'''

'''
#вар 3, крылов, чуркина

print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = not (y <= (not (z <= w))) and ((not z) <= ((not w) == x))
                print(w, x, y, z, int(f))
# y w z x
'''

'''
#вар 13, крылов, чуркина

print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = ((x == (not y)) or (x == (not z))) and w and (y <= z)
                print(w, x, y, z, int(f))
# x z y w
'''

'''
# статград, досрок, 2023
print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (x and (not y)) or (y == z) or (not w)
                print(w, x, y, z, int(f))
# x w z y 
'''

'''
# решу егэ, №60244

print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (x and (not y)) or (y == z) or (not w)
                print(w, x, y, z, int(f))
# w z y x
'''
