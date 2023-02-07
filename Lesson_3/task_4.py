# Задача HARD необязательная
# Имеется список чисел. Создайте список, в который попадают числа,
# описывающие максимальную возрастающую последовательность.
# Порядок элементов менять нельзя.
# Одно число - это не последовательность.
#
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

import random

array_size = int(input('Введите количество чисел в списке: '))
array_of_elements = []
for i in range(array_size):
    array_of_elements.append(random.randrange(0, 10))
print(array_of_elements)

maximum_sequence = [0, 0]

for el in array_of_elements:
    max_number = el
    while (max_number + 1) in array_of_elements:
        max_number += 1
    if (max_number - el) > (maximum_sequence[1] - maximum_sequence[0]):
        maximum_sequence[0], maximum_sequence[1] = el, max_number

if maximum_sequence[1] - maximum_sequence[0] == 0:
    print('Последовательность не найдена.')
else:
    print(f'Максимальная последовательность: {maximum_sequence}.')
