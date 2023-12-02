'''
#решу егэ №48394

a = '0123456789ABCDE'
for x in a:
    f = int(f'4C{x}4', 15) + int(f'{x}62A', 13)
    if f % 121 == 0:
        print(f // 121)
        break

#234
'''

'''
#решу егэ №48395
a = '0123456789ABCDEFGHI'
for x in a:
    f = int(f'28{x}2', 18) + int(f'93{x}5', 12)
    if f % 133 == 0:
        print(f // 133)
        break
#229
'''

'''
# решу егэ №48392
for x in '12345678':
    for y in '012345678':
        f = int(f'2{y}66{x}', 9) + int(f'{x}0{y}1', 12)
        if f % 170 == 0:
            print(x, y, f // 170)
# 169
'''

'''
# решу егэ №48393
for x in '01234567':
    for y in '01234567':
        f = int(f'{y}04{x}5', 11) + int(f'253{x}{y}', 8)
        if f % 117 == 0:
            print(x, y, f // 117)
# 224
'''

'''
#решу егэ №48385
for x in '0123456789abc':
    for y in '0123456789abc':
        f = int(f'8{x}78{y}', 13) + int(f'79{x}{y}7', 18)
        if f % 9 == 0:
            print(x, y, f // 9)
#113024
'''

'''
# решу егэ №48386
for x in '0123456789abcde':
    for y in '0123456789abcde':
        f = int(f'90{x}4{y}', 15) + int(f'91{x}{y}2', 16)
        if f % 56 == 0:
            print(x, y, f // 56)
# 18754
'''

'''
# решу егэ №48387
for x in '0123456789a':
    for y in '0123456789a':
        f = int(f'{x}341{y}', 11) + int(f'56{x}1{y}', 19)
        if f % 305 == 0:
            print(x, y, f // 305)
# 2778
'''
