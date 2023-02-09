# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
# число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

import random


# функция, генерирующая список целых чисел заданного размера.
def list_generator(array_size):
    array_of_elements = []
    for i in range(array_size):
        array_of_elements.append(random.randrange(10, 20))
    return array_of_elements


# функция, считающая максимальный сбор ягод.
def maximum_yield(berry_harvest):
    maximum_berries = 0
    for i in range(len(berry_harvest)):
        if berry_harvest[i] + berry_harvest[i-1] + berry_harvest[i-2] > maximum_berries:
            maximum_berries = berry_harvest[i] + berry_harvest[i-1] + berry_harvest[i-2]
    return maximum_berries


number_bushes = int(input('Введите количество кустов черники в грядке: '))
berry_harvest = list_generator(number_bushes)
print(berry_harvest)
print(maximum_yield(berry_harvest))
