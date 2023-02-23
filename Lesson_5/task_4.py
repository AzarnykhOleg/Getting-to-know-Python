# задача калькулятор необязательная.
# Решать только через рекурсию!.
# Пользоваться встроенными функциями вычисления таких выражений нельзя,
# если только для проверки вашего алгоритма.
# на вход подается строка из операторов / * + - и целых чисел.
# Надо посчитать результат введенного выражения.
# Например,
# на входе
# 1+9/3*7-4
# на выходе
# 18

task_condition = input('Введите пример => ')


def calculator(task_condition):
    for el in task_condition:
        previous_character = task_condition.index(el)
        next_character = task_condition.index(el)
        i = task_condition.index(el)
        j = i
        k = i
        if el != "/" and el != "*" and el != "+" and el != "-":
            continue
        elif el == "/" or el == "*":
            while (task_condition[j - 1]).isdigit() and previous_character > 0:
                previous_character = j - 1
                j -= 1
            while next_character < (len(task_condition) - 1) and (task_condition[k + 1]).isdigit():
                next_character = k + 1
                k += 1
            if el == "/":
                calculation = int(
                    int(task_condition[previous_character:i]) / int(task_condition[i + 1:next_character + 1]))
            else:
                calculation = int(task_condition[previous_character:i]) * int(task_condition[i + 1:next_character + 1])
            task_condition = f'{task_condition[:previous_character]}{calculation}{task_condition[next_character + 1:]}'
            return calculator(task_condition)
        elif "/" not in task_condition and "*" not in task_condition and (el == "+" or el == "-"):
            while (task_condition[j - 1]).isdigit() and previous_character > 0:
                previous_character = j - 1
                j -= 1
            while next_character < (len(task_condition) - 1) and (task_condition[k + 1]).isdigit():
                next_character = k + 1
                k += 1
            if el == "+":
                calculation = int(
                    int(task_condition[previous_character:i]) + int(task_condition[i + 1:next_character + 1]))
            else:
                calculation = int(task_condition[previous_character:i]) - int(task_condition[i + 1:next_character + 1])
                # if calculation < 0: ЗДЕСЬ ДОЛЖНО БЫТЬ РЕШЕНИЕ ПРОБЛЕМЫ ОТРИЦАТЕЛЬНЫХ ЧИСЕЛ
            task_condition = f'{task_condition[:previous_character]}{calculation}{task_condition[next_character + 1:]}'
            return calculator(task_condition)
    return task_condition

print(task_condition)
print(calculator(task_condition))
