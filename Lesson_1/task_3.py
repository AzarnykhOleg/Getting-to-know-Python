# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних
# трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.

ticket_number = int(input('Введите номер билета: '))
sum_of_first_numbers = 0
sum_of_last_numbers = 0
if ticket_number / 1000000 < 0.1 or ticket_number / 1000000 >= 1:
    print('Введено неверное значение.')
else:
    for i in (10, 100, 1000):
        sum_of_last_numbers += ticket_number % i // (i / 10)
    ticket_number = ticket_number // 1000
    for i in (10, 100, 1000):
        sum_of_first_numbers += ticket_number % i // (i / 10)
    if sum_of_last_numbers == sum_of_first_numbers:
        print('Билет счастливый!')
    else:
        print('Не повезло.')
