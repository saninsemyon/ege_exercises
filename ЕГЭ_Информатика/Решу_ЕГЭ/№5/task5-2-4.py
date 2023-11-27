'''
Улитка ползёт вверх по столбу высотой n метров. Каждый день она проползает вверх
на 3 метра, а каждую ночь съезжает вниз на 2 метра. За сколько дней она доползёт
до вершины столба.

Для введённого n вычислите количество дней, необходимых для того, чтобы улитка
добралась до вершины столба.
'''

height = int(input())

#height = 5
current_height = 0
day = 0

while current_height < height:
    current_height = current_height + 3
    day += 1
    if current_height >= height:
        break
    current_height = current_height - 2

print(day)
