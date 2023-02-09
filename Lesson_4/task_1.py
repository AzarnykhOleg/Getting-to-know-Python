# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа:
# n - кол-во элементов первого множества,
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random


# функция, генерирующая список целых чисел заданного размера.
def list_generator(array_size):
    array_of_elements = []
    for i in range(array_size):
        array_of_elements.append(random.randrange(0, 10))
    return array_of_elements


# функция, формирующая без повторений в порядке возрастания все те числа, которые встречаются в обоих заданных списках.
def combined_list(array_1, array_2):
    combined_array = sorted(list(set(i for i in array_1 if i in array_2)))
    return combined_array


array_1 = list_generator(int(input('Введите количество элементов в массиве: ')))
print(array_1)
array_2 = list_generator(int(input('Введите количество элементов в массиве: ')))
print(array_2)
print(f'Искомые числа: {combined_list(array_1, array_2)}')
