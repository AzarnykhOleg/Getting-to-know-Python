# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X.

import random

array_size = int(input('Введите количество элементов в массиве: '))
array_of_elements = []
for i in range(array_size):
    array_of_elements.append(random.randrange(0, 100))
print(array_of_elements)
specified_element = int(input('Задайте число для поиска в массиве элемента, самого близкого по значению: '))
difference_of_elements = abs(specified_element - array_of_elements[0])
desired_index = 0
for i in range(array_size):
    if abs(specified_element - array_of_elements[i]) < difference_of_elements:
        difference_of_elements = abs(specified_element - array_of_elements[i])
        desired_index = i
print(f'Самый близкий по величине элемент к числу "{specified_element}" - {array_of_elements[desired_index]}.')
