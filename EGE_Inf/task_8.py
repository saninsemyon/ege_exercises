'''
# решу егэ №59745

from itertools import *

num = 0
c = 0
for i in product(sorted('АЛГОРИТМ'), repeat=5):
    num += 1
    if i.count('И') >= 2 and i[0] != 'Г' and num % 2 != 0:
        c += 1
print(c)

#2429
'''

'''
#решу егэ №7667

from itertools import *
c = 0
for i in product('ЕГЭ', repeat=5):
    s = ''.join(i)
    if i[0] == 'Е' or i[0] == 'Э':
        c += 1
print(c)

#162
'''

'''
#решу егэ №8098

from itertools import *

c = 0
for i in product('СЛОН', repeat=5):
    s = ''.join(i)
    if i.count('С') == 1:
        c += 1
print(c)

#405
'''

'''
#решу егэ №60250

from itertools import *
c = 0
for i in product('01234567', repeat=5):
    s = ''.join(i)
    if i.count('1') == 0 and i[0] != i[1] != i[2] != i[3] != i[4]  :
        c += 1
    print(s)
print(c)

#дорешать
'''

'''
# решу егэ №3193
from itertools import *

c = 0
for i in product(sorted('АОУ'), repeat=5):
    s = ''.join(i)
    c += 1
    if c == 210:
        print(s)
        break

# УОУАУ
'''

from itertools import *

m = []
s = []
for count in product('012345678', repeat=5):
    s.append(int(count))
    for j in range(len(s)):
        c1 = 0
        for k in range(0, j + 1):
            if k < j:
                c1 += 1
        if c1 == 10:
            m.append(j)
print(len(m))
