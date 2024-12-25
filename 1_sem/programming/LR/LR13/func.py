import os


fields = ('N', 'Surname', 'Group', 'Where is the problem', 'The problem itself')


def file_permissions(name):
    perm = ''
    if os.access(name, os.R_OK):
        perm += 'r'
    else:
        perm += '-'
    if os.access(name, os.W_OK):
        perm += 'w'
    else:
        perm += '-'
    if os.access(name, os.X_OK):
        perm += 'x'
    else:
        perm += '-'
    return perm


def find_key_index(key):
    match key:
        case 'N':
            key_index = 0
        case 'Surname':
            key_index = 1
        case 'Group':
            key_index = 2
        case 'Where is the problem':
            key_index = 3
        case 'The problem itself':
            key_index = 4
    return key_index


def get_val(prompt):
    while True:
        try:
            val = int(input(prompt))
            while val < 0 or val > 6:
                val = int(input(prompt))
            else:
                return val
        except ValueError:
            print('Некорректный ввод')


def get_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print('Некорректный ввод')


def menu():
    print('\033[0m{}'.format('+' + '-' * 84 + '+'))
    print('|' + ' ' * 40 + 'MENU' + ' ' * 40 + '|')
    print('+' + '-' * 28 + '+' + '-' * 55 + '+')
    print('|' + '{:^28}'.format('1') + '|' + '{:^55}'.format('Выбрать файл для работы') + '|')
    print('+' + '-' * 28 + '+' + '-' * 55 + '+')
    print('|' + '{:^28}'.format('2') + '|' + '{:^55}'.format('Инициализировать БД') + '|')
    print('+' + '-' * 28 + '+' + '-' * 55 + '+')
    print('|' + '{:^28}'.format('3') + '|' + '{:^55}'.format('Вывести содержимое БД') + '|')
    print('+' + '-' * 28 + '+' + '-' * 55 + '+')
    print('|' + '{:^28}'.format('4') + '|' + '{:^55}'.format('Добавить запись в конец БД') + '|')
    print('+' + '-' * 28 + '+' + '-' * 55 + '+')
    print('|' + '{:^28}'.format('5') + '|' + '{:^55}'.format('Поиск по одному полю') + '|')
    print('+' + '-' * 28 + '+' + '-' * 55 + '+')
    print('|' + '{:^28}'.format('6') + '|' + '{:^55}'.format('Поиск по двум полям') + '|')
    print('+' + '-' * 28 + '+' + '-' * 55 + '+')
    print('|' + '{:^28}'.format('0') + '|' + '{:^55}'.format('Завершение программы') + '|')
    print('+' + '-' * 28 + '+' + '-' * 55 + '+')
    print('\033[0m'.format())


def choose_file():
    name = input('Введите имя файла, с которым хотите начать работу: ', )
    if os.path.isfile(name) and name != '':
        permissions = file_permissions(name)
        if permissions == 'rw-' or permissions == 'rwx':
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


def display_content(name):
    with open(name, 'r') as database:
        for line in database:
            if line.strip():
                line_in = [x for x in line.split('|')]
                print(f'{line_in[0]:^3}|{line_in[1]:^15}|{line_in[2]:^7}|{line_in[3]:^20}|{line_in[4]:^24}|')



def add_end(name):
    line_count = 0
    with open(name, 'r+') as database:
        for i in database:
            last_line = i
            line_count += 1
        database.seek(0, 2)
        surname = input("Фамилия студента: ", )
        group = get_int("Группа: ")
        where_is_the_problem = input('Где проблема: ')
        the_problem_itself = input('Что именно за проблема: ')
        if line_count == 0:
            line_count = 1
        new_line = f'{line_count}|{surname}|{group}|{where_is_the_problem}|{the_problem_itself}|\n'
        database.write(new_line)


def search_one(name):
    key = input('Искать по: ', )
    if key in fields:
        key_index = find_key_index(key)
        keyword = input('Ищем: ', )
        with open(name, 'r+') as database:
            for line in database:
                if line.strip():
                    line_in = [x for x in line.split('|')]
                    if keyword == line_in[key_index]:
                        print(f'{line_in[0]:^3}|{line_in[1]:^15}|{line_in[2]:^7}|{line_in[3]:^20}|{line_in[4]:^24}|')
    else:
        print('Такого поля нет')


def search_two(name):
    key1, key2 = input('Искать по: ', ).split(',')
    while key2 == key1:
        key2 = input('Поля не могут совпадать', )
    if key1 in fields and key2 in fields:
        key1_index = find_key_index(key1)
        key2_index = find_key_index(key2)
        keyword1 = input('Ищем в первом поле: ', )
        keyword2 = input('Ищем во втором поле: ', )
        with open(name, 'r+') as database:
            for line in database:
                if line.strip():
                    line_in = [x for x in line.split('|')]
                    if keyword1 == line_in[key1_index] and keyword2 == line_in[key2_index] :
                        print(f'{line_in[0]:^3}|{line_in[1]:^15}|{line_in[2]:^7}|{line_in[3]:^20}|{line_in[4]:^24}|')
    else:
        print('Какого-то из полей нет(((')
