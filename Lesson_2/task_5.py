# задача 4 НЕГА необязательная
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

given_number = int(input('Введите число => '))
list_of_fibonacci_numbers = [1, 0, 1]
for i in range(given_number - 1):
    next_number = list_of_fibonacci_numbers[-1] + list_of_fibonacci_numbers[-2]
    list_of_fibonacci_numbers.append(next_number)
    previous_number = list_of_fibonacci_numbers[1] - list_of_fibonacci_numbers[0]
    list_of_fibonacci_numbers.insert(0, previous_number)
print(list_of_fibonacci_numbers)
