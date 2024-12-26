import os
from struct import unpack
from sys import getsizeof

from prettytable import PrettyTable, TableStyle


def main_table() -> None:

    table = PrettyTable()
    table.field_names = ['№', 'Func']
    table.add_rows([
        [1, 'Выбрать файл для работы'],
        [2, 'Инициализировать БД'],
        [3, 'Вывести содержимое БД'],
        [4, 'Добавить запись в конец БД'],
        [5, 'Поиск по одному полю'],
        [6, 'Поиск по двум полям'],
        [0, 'Завершение программы']])

    table.set_style(TableStyle(16))

    print(table)


columns = ['id', 'username', 'user_id', 'role', 'is_banned']


def display_content(name: str) -> None:
    table = PrettyTable()
    table.field_names(columns)

    with (open(name, 'r') as database):
        for line in database:
            line_in = [x.strip() for x in line.strip().split('|')]
            if line_in:
                table.add_row(line_in)

    table.set_style(TableStyle(16))
    print(table)


def print_row(line: list) -> None:
    table = PrettyTable()
    table.field_names(columns)

    table.add_row(line)

    table.set_style(TableStyle(16))
    print(table)


def file_permissions(name: str) -> str:
    perm = 'r' if os.access(name, os.R_OK) else '-'
    perm += 'w' if os.access(name, os.W_OK) else '-'
    perm += 'x' if os.access(name, os.X_OK) else '-'
    return perm


def key_index(key: str) -> int:
    if key in columns:
        return columns.index(key)
    return -1


# def get_val(prompt):
#     while True:
#         try:
#             val = int(input(prompt))
#             while val < 0 or val > 6:
#                 val = int(input(prompt))
#             else:
#                 return val
#         except ValueError:
#             print('Некорректный ввод')
#
#
def input_int(text):
    while True:
        try:
            val = int(input(text).strip())
            return val
        except ValueError:
            print('Попробуйте еще раз')



def choose_file():
    name = input('Введите имя файла, с которым хотите начать работу: ', )
    if os.path.isfile(name) and name != '':
        permissions = file_permissions(name)
        if "rw" in permissions:
            return name
        else:
            print('У файла недостаточно разрешений: ', permissions)
            return None
    else:
        print('Такого файла не существует')
        return None


def create_or_overwrite(file, Database):
    with open(Database, 'r') as database:
        if file is None:
            name = input('Введите имя для БД: ', )
            with open(name, 'a') as file:
                for line in database:
                    file.write(line)
        else:
            with open(file, 'a') as file:
                for line in database:
                    file.write(line)


def add_end(name):
    line_count = 0
    with open(name, 'r+') as database:
        for i in database:
            last_line = i
            line_count += 1
        database.seek(0, 2)
        surname = input("Фамилия студента: ", )
        group = input_int("Группа: ")
        where_is_the_problem = input('Где проблема: ')
        the_problem_itself = input('Что именно за проблема: ')
        if line_count == 0:
            line_count = 1
        new_line = f'{line_count}|{surname}|{group}|{where_is_the_problem}|{the_problem_itself}|\n'
        database.write(new_line)


def search_one(name):
    key = input('Искать по: ')
    if key in columns:
        index = key_index(key)
        keyword = input('Ищем: ')
        with open(name, 'r+') as database:
            for raw in database:
                line = unpack('c' * getsizeof(raw), raw)
                if line.strip():
                    line_in = [x for x in line.split('|')]
                    if keyword == line_in[index]:
                        print_row(line_in)
    else:
        print('Такого поля нет')


def search_two(name):
    key1, key2 = input('Искать по (введи 2 ключа через пробел):\n> ', ).split()
    while key2 == key1:
        key2 = input('Поля не могут совпадать\nВведи второй ключ \n>')
    if key1 in columns and key2 in columns:
        key1_index = key_index(key1)
        key2_index = key_index(key2)
        keyword1 = input('Ищем в первом поле: ', )
        keyword2 = input('Ищем во втором поле: ', )
        with open(name, 'r+') as database:
            for raw in database:
                line = ''.join(unpack('c' * getsizeof(raw), raw))
                line_in = [x.strip() for x in line.strip().split('|')]
                if line_in:
                    if keyword1 == line_in[key1_index] and keyword2 == line_in[key2_index] :
                        print_row(line_in)
    else:
        print('Какого-то из полей нет(((')