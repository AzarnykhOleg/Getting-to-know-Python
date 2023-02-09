# Ззадача RLE необязательная.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# (где только буквы присутствуют для простоты), например, декодирование.
# https://stepik.org/lesson/21300/step/2

def data_encoding(some_str):
    encoding = ""
    i = 0
    while i < len(some_str):
        count = 1
        while i + 1 < len(some_str) and some_str[i] == some_str[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + some_str[i]
        i += 1
    return encoding


def decoding_data(some_str):
    decoding = ""
    j = 0
    while j < len(some_str):
        if some_str[j].isalpha():
            decoding += some_str[j] * int(some_str[:j])
            some_str = some_str[(j + 1):]
            j = 0
        else:
            j += 1
    return decoding


some_str = 'rrrrrrrrtttttttttttttyyyyyyyyyyuuuuuuDDDDDuuuuuuttttttttttrrrrrGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGrrrr'
print(some_str)
some_str = data_encoding(some_str)
print(some_str)
some_str = decoding_data(some_str)
print(some_str)
