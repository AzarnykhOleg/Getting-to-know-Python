# Найдите сумму цифр любого вещественного или целого числа.

any_number = float(input('Введите число: '))
sum_of_numbers = 0
while int(any_number) - any_number != 0:
    any_number = any_number * 10
while any_number // 10 != 0:
    sum_of_numbers += any_number % 10
    any_number = any_number // 10
sum_of_numbers += any_number
print(int(sum_of_numbers))
