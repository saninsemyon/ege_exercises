'''
# решу егэ, № 9365

s = 68 * '8'
while '222' in s or '888' in s:
    if '222' in s:
        s = s.replace('222', '8', 1)
    if '888' in s:
        s = s.replace('888', '2', 1)
s = int(s)
print(s)

#28
'''

'''
# решу егэ №11270

s = '1' + '9' * 100
while '19' in s or '299' in s or '3999' in s:
    if '19' in s:
        s = s.replace('19', '2', 1)
    if '299' in s:
        s = s.replace('299', '3', 1)
    if '3999' in s:
        s = s.replace('3999', '1', 1)
print(s)

#39
'''

'''
# вариант 1, крылов, чуркина

s = '2' * 2 + '1' * 2023 + '2' * 2
while '211' in s or '112' in s:
    s = s.replace('11', '1', 1)
    if '21' in s:
        s = s.replace('21', '12', 1)
    else:
        s = s.replace('12', '1', 1)
print(s)

#121222
'''

'''
# вариант 13, крылов, чуркина

s = '1' + '5' * 25
while '15' in s or '1' in s:
    if '15' in s:
        s = s.replace('15', '5551', 1)
    else:
        if '1' in s:
            s = s.replace('1', '5', 1)
print(s.count('5'))

# 76
'''

'''
# решу егэ №23912

a = '>' + '1' * 10 + '2' * 20 + '3' * 30
while '>1' in a or '>2' in a or '>3' in a:
    if '>1' in a:
        a.replace('>1', '22>', 1)
    if '>2' in a:
        a.replace('>2', '2>', 1)
    if '>3' in a:
        a.replace('>3', '1>', 1)
print(a.count('1') + a.count('2') + a.count('3'))

# не робит
'''