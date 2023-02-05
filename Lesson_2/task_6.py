# Задача 5 - HARD необязательная
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в N-мерном пространстве.
# Сначала задается N с клавиатуры, потом задаются координаты точек.
import math

dimension_of_space = int(input('Введите размерность пространства => '))
intermediate_result = 0.0
for i in range(dimension_of_space):
    coordinate_1 = float(input(f'Введите координату {i + 1} первой точки => '))
    coordinate_2 = float(input(f'Введите координату {i + 1} второй точки => '))
    intermediate_result += (coordinate_1 - coordinate_2) ** 2
print(f'Расстояние между точками = {math.sqrt(intermediate_result)}')
