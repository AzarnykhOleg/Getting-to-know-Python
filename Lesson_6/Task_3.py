# Задача HARD SORT необязательная.
# Задайте двумерный массив из целых чисел.
# Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
#
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
#
# После сортировки
# 1 2 3 4
# 5 7 9 10

import random

number_of_rows = int(input("Задайте количество строк массива => "))
number_of_columns = int(input("Задайте количество стольбцов массива => "))
specified_array = []
pre_sorted_array = []
sorted_array = []
for el in range(number_of_rows):
    el_1 = [random.randint(-50, 50) for i in range(number_of_columns)]
    specified_array.append(el_1)
for el in specified_array:
    for el_1 in el:
        pre_sorted_array.append(el_1)
pre_sorted_array.sort()
for el in range(number_of_rows):
    el_1 = pre_sorted_array[:number_of_columns]
    sorted_array.append(el_1)
    del pre_sorted_array[:number_of_columns]

print('\n'.join('     '.join(str(cell) for cell in row) for row in specified_array))
print('-----------------------------------------------------------------')
print('\n'.join('     '.join(str(cell) for cell in row) for row in sorted_array))
