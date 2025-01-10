from os import access, R_OK, W_OK
from os.path import isfile
from struct import unpack, pack
from sys import getsizeof

from prettytable import PrettyTable, TableStyle


def main_table() -> None:
    table = PrettyTable()
    table.field_names = ['№', 'Func']
    table.add_rows([
        [1, 'Выбрать файл для работы'],
        [2, 'Инициализировать БД'],
        [3, 'Вывести содержимое БД'],
        [4, 'Добавить запись в БД'],
        [5, 'Удалить запись из БД'],
        [6, 'Поиск по одному полю'],
        [7, 'Поиск по двум полям'],
        [0, 'Завершение программы']])

    table.set_style(TableStyle(16))

    print(table)


columns = ['id', 'username', 'user_id', 'role', 'is_banned']
line_format = f'h{"c" * 10}l{"c" * 5}?' # short .{10} long ["admin" / " user"] bool
bytes_in_line = 30


def display_content(file_name: str) -> None:
    table = PrettyTable()
    table.field_names = columns

    with (open(file_name, 'rb') as database): 
        for i in range(file_len(file_name)):
            database.seek(bytes_in_line * i)
            raw = database.read(bytes_in_line)
            if raw:
                line = unpack_line(raw)
                table.add_row(line)

    table.set_style(TableStyle(16))
    print(table)


def print_row(line: list) -> None:
    table = PrettyTable()
    table.field_names = columns

    table.add_row(line)

    table.set_style(TableStyle(16))
    print(table)


def file_permissions(file_name: str) -> str:
    perm = 'r' if access(file_name, R_OK) else '-'
    perm += 'w' if access(file_name, W_OK) else '-'
    return perm


def key_index(key: str) -> int:
    if key in columns:
        return columns.index(key)
    return -1 


def input_int(text: str) -> int:
    while True:
        try:
            val = int(input(text).strip())
            return val
        except ValueError:
            print('Попробуйте еще раз')


def init(file_name: str) -> None:
    if isfile(file_name) or file_permissions(file_name) != 'rw':
        file = open(file_name, 'wb')
        file.close()


def choose_file() -> str:
    file_name = input('Введите имя файла, c которым хотите начать работу: ', )
    if file_name != '' and ' ' not in file_name and '/' not in file_name:
        if not file_name.endswith('.bin'):
            file_name += '.bin'
        if not file_name.startswith(r'./1_sem/programming/LR/LR14/'):
            file_name = './1_sem/programming/LR/LR14/' + file_name
        return file_name
    print('Мимокрокодил')
    return choose_file()


def unpack_line(raw_line) -> list:
    unpacked = list(unpack(line_format, raw_line))
    encoded_name = ''.join([i.decode('utf-8') for i in unpacked[1:11]]).strip()
    encoded_role = ''.join([i.decode('utf-8') for i in unpacked[12:17]]).strip()
    line = [unpacked[0], encoded_name, unpacked[11], encoded_role, unpacked[17]]
    return line


def pack_line(id: int, username: str, user_id: int, 
              role: str, is_blocked: bool) -> bytes:
    bytes_name = [bytes(i, 'utf-8') for i in username]
    bytes_role = [bytes(i, 'utf-8') for i in role]
    
    return pack(line_format, id, *bytes_name, user_id, *bytes_role, is_blocked)


def file_len(file_name: str) -> int:
    with open(file_name, "rb") as file:
        length = getsizeof(file.readline()) // bytes_in_line
        return length


def move_lines(file_name: str, line_ind: int, insert_line: bytes) -> None:
    with open(file_name, "rb+") as orig_file:
        with open(file_name, 'rb') as read_file:
            orig_file.seek(bytes_in_line * line_ind)
            orig_file.write(insert_line)
            for i in range(line_ind, file_len(file_name)):
                read_file.seek(bytes_in_line * i)
                orig_file.write(read_file.read(bytes_in_line))


def add_line(file_name: str) -> None:
    id = input_int("Введите id записи\n> ")
    username = input("Введите username пользователя\n> ")[:10].ljust(10, ' ')
    user_id = input_int("Введите user_id пользователя\n> ")
    db_len = file_len(file_name)
    line_ind = input_int(f"Введите индекс строки, в которую хотите вставить запись\nТекущая длина {db_len - 1}\n> ")

    while True:
        i = input_int("Введите параметр role\n0 - user\n1 - admin\n> ")
        match i:
            case 1:
                role = 'admin'
                break
                
            case 0:
                role = ' user'
                break


    while True:
        i = input_int("Введите флаг is_blocked\n0 - false\n1 - true\n> ")
        match i:
            case 1:
                is_blocked = True
                break
            case 0:
                is_blocked = False
                break

    insert_line = pack_line(id, username, user_id, role, is_blocked)
    if line_ind >= db_len:
        with open(file_name, 'rb+') as file:
            file.write(insert_line)
        return
    line_ind = max(0, line_ind)
    move_lines(file_name, line_ind, insert_line)


def del_line(file_name: str) -> None:
    db_len = file_len(file_name)
    line_ind = input_int(f"Введите индекс записи, которую хотите удалить\nТекущая длина {db_len - 1}\n> ")
    line_ind = max(0, line_ind)
    line_ind = min(line_ind, db_len - 1)
    
    with open(file_name, 'rb+') as orig_file:
        with open(file_name, "rb") as read_file:
            orig_file.seek(bytes_in_line * line_ind)
            for j in range(line_ind + 1, db_len):
                read_file.seek(bytes_in_line * j)
                orig_file.write(read_file.read(bytes_in_line))
        orig_file.truncate(bytes_in_line * (db_len - 2))


def search_one(file_name: str) -> None:
    print('Выберите поле из ключей:')
    print(*[c for c in columns], sep=' ')
    key = input('> ') 
    if key.isalpha():
        while (key_ind := key_index(key)) == -1:
                print('Мимокрокодил')
                key = input('> ') 
    else:
        key_ind = key_index(key)
        
    value = input("Что ищем?\n> ").strip()

    is_found = False
    
    with open(file_name, 'rb') as file:
        for i in range(file_len(file_name)):
            raw = file.read(bytes_in_line)
            if raw:
                line = unpack_line(raw)
                if str(line[key_ind]) == value:
                    if not is_found:
                        print("Результаты:")
                        is_found = True
                    print_row(line)
    if not is_found:
        print('Ничего не найдено :((((')


def search_two(file_name: str) -> None:
    print('Выберите поля из ключей:')
    print(*[c for c in columns], sep=' ')
    key1 = input('Ключ 1\n> ') 
    if key1.isalpha():
        while (key1_ind := key_index(key1)) == -1:
                print('Мимокрокодил')
                key1 = input('> ') 
    else:
        key1_ind = key_index(key1)
    
    value1 = input("Что ищем?\n> ").strip()
    
    key2 = input('Ключ 2\n> ') 
    if key2.isalpha():
        while (key2_ind := key_index(key2)) == -1:
                print('Мимокрокодил')
                key2 = input('> ') 
    else:
        key2_ind = key_index(key2)
        
    value2 = input("Что ищем?\n> ").strip()

    is_found = False

    with open(file_name, 'rb') as file:
        for i in range(file_len(file_name)):
            raw = file.read(bytes_in_line)
            if raw:
                line = unpack_line(raw)
                if str(line[key1_ind]) == value1 and str(line[key2_ind]) == value2:
                    if not is_found:
                        print("Результаты:")
                        is_found = True
                    print_row(line)
    if not is_found:
        print('Ничего не найдено :((((')
