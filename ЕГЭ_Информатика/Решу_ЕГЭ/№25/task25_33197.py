# Тип 25 №
# #33197
# Рассмотрим произвольное натуральное число, представим его всеми возможными способами в виде произведения двух натуральных
# чисел и найдём для каждого такого произведения разность сомножителей. Например, для числа 16 получим: 16  =  16*1  =  8*2  =  4*4, множество разностей содержит числа 15, 6 и 0. Найдите все натуральные числа, принадлежащие отрезку [1 000 000; 2 000 000], у которых составленное описанным способом множество разностей будет содержать не меньше трёх элементов, не превышающих 100. В ответе перечислите найденные числа в порядке возрастания.


cnt = []
for i in range(1000, 2001):
    cnt.append(i - 1)
    if (int(i ** (0.5)) ** 2) == i:
        cnt.append(0)
        for j in range(2, i):
            if i // j != 0 and i // j < 100:
                cnt.append(j - (i // j))
if len(cnt) >= 3:
    print(cnt)





