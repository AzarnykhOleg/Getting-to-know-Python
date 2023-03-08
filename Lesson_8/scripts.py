import sqlite3

conn = sqlite3.connect('telephone_directory.db')
cur = conn.cursor()


# PRAGMA foreign_keys = ON;
# Функция создания таблицы
def create_table(table_description):
    cur = conn.cursor()
    cur.execute(table_description)
    cur.close()


# Функция заполнения таблицы
def data_entry(entering_data_into_tab):
    cur = conn.cursor()
    cur.execute(entering_data_into_tab)
    conn.commit()
    cur.close()


# Функция вывода меню в консоль
def print_menu():
    print('\nВыберите один из следующих пунктов:')
    print('1. Добавить новый контакт')
    print('2. Показать все контакты')
    print('3. Редактировать контакты')
    print('4. Удалить контакты')
    print('5. Найти контакты')
    print('0. Выйти из телефонного справочника')


# Функция добавления контакта в телефонный справочник
def addcontact():
    while True:
        lastname = input("Введите фамилию => ")
        if len(lastname) != 0:
            break
        else:
            print("Введите фамилию => ")
    while True:
        name = input("Введите имя => ")
        if len(name) != 0:
            break
        else:
            print("Введите имя => ")
    while True:
        sername = input("Введите отчество => ")
        if len(sername) != 0:
            break
        else:
            print("Введите отчество => ")
    while True:
        print("\nК какой группе контактов отнести?")
        print('Выберите один из следующих пунктов:')
        print('1. Друзья')
        print('2. Работа')
        print('3. Семья')
        print('4. Коллеги')
        print('5. Без группы')
        groupspeople = int(input("Ваш выбор => "))
        if groupspeople in range(1, 6):
            break
        else:
            print("\n\nОшибочный ввод.")
    cur.execute('''INSERT INTO people (lastname, name, sername, groupspeople) VALUES (?,?,?,?)''',
                (lastname, name, sername, groupspeople))
    people_id = cur.execute('''SELECT id FROM people ORDER BY id DESC LIMIT 1''')
    people_id = people_id.fetchone()[0]
    while True:
        print("\nДобавить номер в телефонный справочник?")
        print('Выберите один из следующих пунктов:')
        print('1. ДА')
        print('2. НЕТ')
        answer = input("Ваш выбор => ")
        if answer == "2":
            break
        else:
            while True:
                phone_number = input("Введите номер телефона => ")
                if not phone_number.isdigit():
                    print("Номер телефона может состоять только из цифр. Введите номер телефона => ")
                    continue
                else:
                    break
            while True:
                print("\nТип номера телефона.")
                print('Выберите один из следующих пунктов:')
                print('1. Домашний')
                print('2. Рабочий')
                print('3. Сотовый')
                print('4. Другое')
                phone_ownership_id = int(input("Ваш выбор => "))
                if phone_ownership_id in range(1, 5):
                    break
                else:
                    print("\n\nОшибочный ввод.")
            cur.execute('''INSERT INTO phone_number (phone_number, phone_ownership_id, people_id) VALUES (?,?,?)''',
                        (phone_number, phone_ownership_id, people_id))
            conn.commit()
    print("Контакт успешно добавлен в телефонный справочник.")


# Функция просмотра телефонного справочника
def displaybook():
    cur.execute('''SELECT lastname, name, sername, name_of_group, name_of_phone, phone_number FROM people
                   JOIN phone_number ON phone_number.people_id = people.id
                   JOIN phone_ownership ON phone_ownership.id = phone_number.phone_ownership_id
                   JOIN groups_of_people ON groups_of_people.id = people.groupspeople
                   ORDER BY lastname
        ''')
    results = cur.fetchall()
    for contact in results:
        print(f'\n{contact[0]} {contact[1]} {contact[2]}\nГруппа: {contact[3]}\n{contact[4]} телефон: {contact[5]}')


# Функция выбора поиска/удаления/редактирования контакта
def key_pair_reception(str):
    print(f'\nСделайте выбор {str}:')
    print('1. По фамилии')
    print('2. По имени')
    print('3. По отчеству')
    print('4. По номеру телефона')
    print('0. Вернуться в меню')
    n = int(input('Ваш выбор => '))
    if n == 1:
        field = "lastname"
    elif n == 2:
        field = "name"
    elif n == 3:
        field = "sername"
    elif n == 4:
        field = "phone_number"
    elif n == 0:
        return print_menu()
    else:
        return None
    keyword = input(f'\nВведите {field}: ')
    keypair = f'{field} = "{keyword}"'
    return keypair


# Функция редактирования контакта
def editcontacts():
    s = key_pair_reception('поиска')
    u = key_pair_reception('обновления')
    if s != None:
        if "phone_number" not in s and "phone_number" not in u:
            sql = f'UPDATE people SET {u} WHERE {s}'
            cur.execute(sql)
            conn.commit()
            print(f'Запись {s} изменена.\n')
        elif "phone_number" in s and "phone_number" in u:
            sql = f'UPDATE phone_number SET {u} WHERE {s}'
            cur.execute(sql)
            conn.commit()
            print(f'Запись {s} изменена.\n')
        elif "phone_number" in s and "phone_number" not in u:
            sql = f'SELECT people_id FROM phone_number WHERE {s}'
            s = cur.execute(sql)
            for el in s:
                for i in el:
                    sql = f'UPDATE people SET {u} WHERE people.id = {i}'
                    cur.execute(sql)
                    conn.commit()
            print(f'Запись изменена.\n')
        elif "phone_number" not in s and "phone_number" in u:
            sql = f'SELECT people.id FROM people WHERE {s}'
            s = cur.execute(sql)
            for el in s:
                for i in el:
                    sql = f'UPDATE phone_number SET {u} WHERE phone_number.people_id = {i}'
                    cur.execute(sql)
                    conn.commit()
            print(f'Запись изменена.\n')


# Функция удаления контакта
def deletecontacts():
    s = key_pair_reception('удаления')
    if s != None:
        if "phone_number" not in s:
            sql = f'SELECT people.id FROM people WHERE {s}'
            ss = cur.execute(sql)
            for el in ss:
                for i in el:
                    sql = f'DELETE FROM phone_number WHERE phone_number.people_id = {i}'
                    cur.execute(sql)
                    conn.commit()
            sql = f'DELETE FROM people WHERE {s}'
            cur.execute(sql)
            conn.commit()
            print(f'Запись удалена.\n')
        elif "phone_number" in s:
            sql = f'DELETE FROM phone_number WHERE {s}'
            cur.execute(sql)
            conn.commit()
            print(f'Запись удалена.\n')


# Функция поиска контакта
def findcontacts():
    s = key_pair_reception('searching')
    print(s)
    if s != None:
        sql = f'SELECT lastname, name, sername, name_of_group, name_of_phone, phone_number ' \
              f'FROM people JOIN phone_number ON phone_number.people_id = people.id ' \
              f'JOIN phone_ownership ON phone_ownership.id = phone_number.phone_ownership_id ' \
              f'JOIN groups_of_people ON groups_of_people.id = people.groupspeople ' \
              f'WHERE {s}'
        cur.execute(sql)
    results = cur.fetchall()
    for contact in results:
        print(f'\n{contact[0]} {contact[1]} {contact[2]}\nГруппа: {contact[3]}\n{contact[4]} телефон: {contact[5]}')