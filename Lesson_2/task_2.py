# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import math

sum_of_numbers = int(input('Чему равна сумма чисел? => '))
product_of_numbers = int(input('Чему равно произведение чисел? => '))
discriminant = sum_of_numbers ** 2 - 4 * product_of_numbers
if discriminant < 0:
    print('Петр дал неверные подсказки.')
elif discriminant == 0:
    y = int(sum_of_numbers / 2)
    x = int(product_of_numbers / y)
    print(f'Загаданы числа {x} и {y}.')
else:
    y_1 = int((sum_of_numbers + math.sqrt(discriminant)) / 2)
    y_2 = int((sum_of_numbers - math.sqrt(discriminant)) / 2)
    x_1 = int(product_of_numbers / y_1)
    x_2 = int(product_of_numbers / y_2)
    print(f'Загаданы числа {x_1} и {y_1} или числа {x_2} и {y_2}')
