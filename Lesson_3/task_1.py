# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X.

import random

array_size = int(input('Введите количество элементов в массиве: '))
array_of_elements = []
for i in range(array_size):
    array_of_elements.append(random.randrange(0, 10))
print(array_of_elements)
specified_element = int(input('Введите элемент для подсчёта количества его вхождений в массив: '))
count = 0
for j in array_of_elements:
    if j == specified_element:
        count += 1
print(f"В списке число {specified_element} встречается {count} раз.")

# ИЛИ ТАК:
# count = array_of_elements.count(specified_element)
# print(f"В списке число {specified_element} встречается {count} раз.")
