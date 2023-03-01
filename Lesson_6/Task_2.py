# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
#
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

mas = [random.randint(-50, 50) for i in range(random.randint(10, 20))]
print(*mas)
max_index = int(input("Задайте максимальное значение => "))
min_index = int(input("Задайте минимальное значение => "))
mas_index = []
if max_index >= min_index:
    for i in range(len(mas)):
        if max_index >= mas[i] >= min_index:
            mas_index.append(i)
print("Индексы:", mas_index)
