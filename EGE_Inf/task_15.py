'''
# решу егэ №59752
for a in range(200):
    c = 0
    for x in range(200):
        for y in range(200):
            if (x + 2 * y < a) or (y < x) or (y > 60) == True:
                c += 1
    if c == 40000:
        print(a)
        break
# 181
'''

'''
# решу егэ №33094
for a in range(100, 0, -1):
    c = 0
    for x in range(1, 100):
        if (a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 18 != 0))) == True:
            c += 1
    if c == 99:
        print(a)
        break
# 45
'''

'''
# решу егэ №60257
for a in range(300):
    c = 0
    for x in range(300):
        for y in range(300):
            if (((x + 2 * y) < a) or (y > x) or (x > 60)) == True:
                c += 1
    if c == 90000:
        print(a)
        break
# 181
'''

# решу егэ №38590
for a in range(50):
    c = 0
    for d in range(17, 59):
        for c in range(29, 81):
            for x in range(50):
                if (x == d) <= ((x != c) and (x != a)) <= (x != d) == True:
                    c += 1
    if c == 104550:
        print(a)
#
