import sqlite3
import sys
import scripts

# Создание базы данных телефонного справочника
scripts.create_table("""CREATE TABLE IF NOT EXISTS people(
                                                id INTEGER PRIMARY KEY,
                                                lastname TEXT DEFAULT NONE,
                                                name TEXT DEFAULT NONE,
                                                sername TEXT DEFAULT NONE,
                                                groupspeople INTEGER DEFAULT NONE,
                                                FOREIGN KEY (groupspeople) REFERENCES groups_of_people (id));""")
scripts.create_table(""" DROP TABLE IF EXISTS groups_of_people;""")
scripts.create_table("""CREATE TABLE IF NOT EXISTS groups_of_people(
                                                id INTEGER PRIMARY KEY,
                                                name_of_group TEXT DEFAULT NONE);""")
scripts.create_table(""" DROP TABLE IF EXISTS phone_ownership;""")
scripts.create_table("""CREATE TABLE IF NOT EXISTS phone_ownership(
                                                id INTEGER PRIMARY KEY,
                                                name_of_phone TEXT DEFAULT NONE);""")
scripts.create_table("""CREATE TABLE IF NOT EXISTS phone_number(
                                                id INTEGER PRIMARY KEY,
                                                phone_number INTEGER DEFAULT NONE,
                                                phone_ownership_id INTEGER DEFAULT NONE,
                                                people_id INTEGER DEFAULT NONE,
                                                FOREIGN KEY (phone_ownership_id) REFERENCES phone_ownership (id),
                                                FOREIGN KEY (people_id) REFERENCES people (id));""")
# Заполнеие постоянными данными таблиц базы данных
scripts.data_entry("""INSERT INTO groups_of_people (name_of_group) VALUES ('Друзья')""")
scripts.data_entry("""INSERT INTO groups_of_people (name_of_group) VALUES ('Работа')""")
scripts.data_entry("""INSERT INTO groups_of_people (name_of_group) VALUES ('Семья')""")
scripts.data_entry("""INSERT INTO groups_of_people (name_of_group) VALUES ('Коллеги')""")
scripts.data_entry("""INSERT INTO groups_of_people (name_of_group) VALUES ('Без группы')""")
scripts.data_entry("""INSERT INTO phone_ownership (name_of_phone) VALUES ('Домашний')""")
scripts.data_entry("""INSERT INTO phone_ownership (name_of_phone) VALUES ('Рабочий')""")
scripts.data_entry("""INSERT INTO phone_ownership (name_of_phone) VALUES ('Сотовый')""")
scripts.data_entry("""INSERT INTO phone_ownership (name_of_phone) VALUES ('Другое')""")
# scripts.data_entry("""INSERT INTO people (lastname, name, sername, groupspeople) VALUES
#                         ('Служба', "спасения", "112", "1"),
#                         ('Азрных', "Олег", "Вячеславович", "2"),
#                         ('Попов', "Иван", "Владимирович", "3"),
#                         ('Иванов', "Иван", "Иванович", "4"),
#                         ('Фролов', "Илья", "Владимирович", "1"),
#                         ('Фис', "Фролович", "Потолок", "2"),
#                         ('Ильдус', "Фарид", "Кролович", "3"),
#                         ('Амаякен', "Акоп", "Карапетович", "4"),
#                         ('Фигня', "Нефантаз", "Каримович", "1"),
#                         ('Алексейцев', "Алексей", "Михаилович", "2"),
#                         ('Владимиров', "Владимр", "Олегович", "3"),
#                         ('Колесов', "Иван", "Тараканович", "4")""")
# scripts.data_entry("""INSERT INTO phone_number (phone_number, phone_ownership_id, people_id) VALUES
#                         ('11111111', 1, 2),
#                         ('222222222', 1, 3),
#                         ('33333333', 1, 2),
#                         ('44444444', 1, 3),
#                         ('555555555', 1, 4),
#                         ('66666666666', 1, 5),
#                         ('77777777777', 1, 4),
#                         ('88888888888', 1, 6),
#                         ('9999999999', 1, 7),
#                         ('00000000000', 1, 8),
#                         ('121212121212', 1, 9),
#                         ('343434343434', 1, 10)""")


# Основная программа
print('\nДОБРО ПОЖАЛОВАТЬ В ТЕЛЕФОННЫЙ СПРАВОЧНИК')
conn = sqlite3.connect('telephone_directory.db')
cur = conn.cursor()


while True:
    scripts.print_menu()
    choice = int(input('Ваш выбор => '))
    if choice == 1:
        scripts.addcontact()
        continue
    elif choice == 2:
        scripts.displaybook()
        continue
    elif choice == 3:
        scripts.editcontacts()
        continue
    elif choice == 4:
        scripts.deletecontacts()
        continue
    elif choice == 5:
        scripts.findcontacts()
        continue
    elif choice == 0:
        print('Программа завершена.\n')
        conn.close()
        sys.exit(0)
    else:
        print('Пожалуйста, следуйте инструкциям')
