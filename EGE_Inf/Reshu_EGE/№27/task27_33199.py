# Набор данных состоит из троек натуральных чисел.
# Необходимо распределить все числа на три группы,
# при этом в каждую группу должно попасть ровно одно число из каждой исходной тройки.
# Сумма всех чисел в первой группе должна быть чётной, во второй — нечётной.
# Определите максимально возможную сумму всех чисел в третьей группе.

# 20
# 15 18 20
# 18 6 3
# 11 20 17

f = open('../../files_for_tasks/27-A.txt')
n = int(f.readline())
sum_min = sum_ave = sum_max = 0
min_diff = 100000

for count in range(n):
    a, b, c = map(int, f.readline().split())
    #print(a, b, c)
    ma = max(a, b, c)
    mi = min(a, b, c)

    sum_max += ma
    sum_min += mi
    average = a + b + c - ma - mi
    sum_ave += average

    if ma - average < min_diff and ma - average != 0 and ma - average % 2 != 0 and ma - mi % 2 != 0:
        min_diff = ma - average

if (sum_ave % 2) == (sum_min % 2):
    print(1, sum_max - min_diff, min_diff)
else:
    print(2, sum_max, min_diff)
