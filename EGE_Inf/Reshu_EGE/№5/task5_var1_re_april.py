# Автомат обрабатывает натуральное число N (0 ≤ N ≤ 255) по следующему алгоритму:
# 1.Строится восьмибитная двоичная запись числа N.
# 2.Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).
# 3.Полученное число переводится в десятичную запись.
# 4.Из нового числа вычитается исходное, полученная разность выводится на экран.
# Какое число нужно ввести в автомат, чтобы в результате получилось 111?

for n in range(0, 500):
    b = bin(n) [2:]
    d = b.replace('0', '1', 2)
    t = int(d, 2) - n
    if t == 111:
        print(n)



