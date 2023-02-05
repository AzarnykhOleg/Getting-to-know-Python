# Задача 10:
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
import random

number_of_coins = int(input('Введите количество монет на столе: '))
list_of_coins = []
for i in range(number_of_coins):
    list_of_coins.append(random.choice([0, 1]))
print(f'{number_of_coins} => {list_of_coins}')
sum_list_of_coins = sum(list_of_coins)
if sum_list_of_coins == number_of_coins or sum_list_of_coins == 0:
    print('Не надо переворачивать ни одной монеты.')
elif (number_of_coins / 2) <= (number_of_coins - sum_list_of_coins):
    print(f'Надо перевернуть {sum_list_of_coins} монет.')
else:
    print(f'Надо перевернуть {number_of_coins - sum_list_of_coins} монет.')
