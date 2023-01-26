# Найдите сумму цифр трехзначного числа.

three_digit_number = int(input('Введите трёхзначное число: '))
sum_of_numbers = 0
if three_digit_number / 1000 < 0.1 or three_digit_number / 1000 >= 1:
    print('Введено неверное значение.')
else:
    for i in (10, 100, 1000):
        sum_of_numbers += three_digit_number % i // (i/10)
    print(int(sum_of_numbers))
