f = open('../../files_for_tasks/24(2).txt')
s = f.readline()
maximum = curent = 1
sogl = 'b, c, d, f'
glas = 'a, o'
n = []
for count in s:
    if s[count] == sogl and s[count + 1] == sogl and s[count + 2] == glas:
        n += 1
    else:
        n == 0
print(n)