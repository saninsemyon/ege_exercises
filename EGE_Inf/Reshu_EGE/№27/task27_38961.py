f = open('../../files_for_tasks/27-A(2).txt')
n = int(f.readline())
max_sum = []
summ = 0
rem1 = 1000000
rem2 = 1000000
rem3 = 1000000
rem4 = 1000000
rem5 = 1000000
rem6 = 1000000
rem7 = 1000000
rem8 = 1000000
rem9 = 1000000
for s in range(n):
    summ += int(s)
    if summ % 10 == 0:
        max_sum.append(summ)
    elif summ % 10 == 1 and summ % 2 == 0 and rem1 != 1000000:
        max_sum.append(summ - rem1)
    elif summ % 10 == 2 and summ % 2 == 0 and rem2 != 1000000:
        max_sum.append(summ - rem2)
    elif summ % 10 == 3 and summ % 2 == 0 and rem3 != 1000000:
        max_sum.append(summ - rem3)
    elif summ % 10 == 4 and summ % 2 == 0 and rem4 != 1000000:
        max_sum.append(summ - rem4)
    elif summ % 10 == 5 and summ % 2 == 0 and rem5 != 1000000:
        max_sum.append(summ - rem5)
    elif summ % 10 == 6 and summ % 2 == 0 and rem6 != 1000000:
        max_sum.append(summ - rem6)
    elif summ % 10 == 7 and summ % 2 == 0 and rem7 != 1000000:
        max_sum.append(summ - rem7)
    elif summ % 10 == 8 and summ % 2 == 0 and rem8 != 1000000:
        max_sum.append(summ - rem8)
    elif summ % 10 == 9 and summ % 2 == 0 and rem9 != 1000000:
        max_sum.append(summ - rem9)
    if summ % 10 == 1 and summ < rem1:
        rem1 = summ
    if summ % 10 == 2 and summ < rem2:
        rem2 = summ
    if summ % 10 == 3 and summ < rem3:
        rem3 = summ
    if summ % 10 == 4 and summ < rem4:
        rem4 = summ
    if summ % 10 == 5 and summ < rem5:
        rem5 = summ
    if summ % 10 == 6 and summ < rem6:
        rem6 = summ
    if summ % 10 == 7 and summ < rem7:
        rem7 = summ
    if summ % 10 == 8 and summ < rem8:
        rem8 = summ
    if summ % 10 == 9 and summ < rem9:
        rem9 = summ
print(max(max_sum))