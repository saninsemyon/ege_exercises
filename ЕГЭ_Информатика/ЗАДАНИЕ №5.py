'''
# тренировочный вариант № 221107

res = []
for n in range(1, 1000):
    s = bin(n)[2:]
    s += s[-1]
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if int(s, 2) > 130:
        res.append(n)
print(min(res))

# 17
'''

'''
# решу егэ №8094

res = []
for n in range(1, 1000):
    s = bin(n)[2:]
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    if int(s, 2) > 43:
        res.append(int(s, 2))
print(min(res))

# 46
'''

'''
# решу егэ №7663

res = []
for i in range(100, 1000):
    mn = []
    s = str(i)
    s_sum1 = int(s[0]) + int(s[1])
    s_sum2 = int(s[1]) + int(s[2])
    mn.append(s_sum1)
    mn.append(s_sum2)
    mn_sum = int(str(max(mn)) + str(min(mn)))
    res.append(mn_sum)
    if mn_sum == 1412:
        print(i)

# 395
'''

'''
# решу егэ №15791

res = []
for n in range(1, 1000):
    s = bin(n)[2:]
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    if int(s, 2) > 97:
        res.append(int(s, 2))
print(min(res))

# 102
'''

'''
# поляков №3906 (№44215)

res = []
for n in range(60, 1000):
    s = bin(n)[2:]
    if s.count('1') == s.count('0'):
        s += s[-1]
    elif s.count('1') > s.count('0'):
        s += '0'
    elif s.count('1') < s.count('0'):
        s += '1'
    if s.count('1') == s.count('0'):
        s += s[-1]
    elif s.count('1') > s.count('0'):
        s += '0'
    elif s.count('1') < s.count('0'):
        s += '1'
    if s.count('1') == s.count('0'):
        s += s[-1]
    elif s.count('1') > s.count('0'):
        s += '0'
    elif s.count('1') < s.count('0'):
        s += '1'
    if int(s, 2) % 2 == 0 and int(s, 2) % 4 != 0:
        res.append(n)
print(min(res))

# 67
'''