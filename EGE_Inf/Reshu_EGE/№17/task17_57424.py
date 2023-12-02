with open('../../files_for_tasks/1_17.txt') as f:
    s = [int(x) for x in f]
    max_c = []
    n = []
    for c in (s):
        if len(str(s[c])) == 2:
            max_c.append(c)
print(max_c)


'''
             if (((len(str(s[c]))) == 2 and (len(str(s[c + 1]) != 2))) or ((len(str(s[c]))) != 2 and (len(str(s[c + 1]) == 2)))) and (str(s[c]) + str(s[c] + 1) % max_c == 0):
            n.append(c[0] and c[0] + 1)
print(len(n))
            '''

