"""
    Лабораторная работа по программированию №14
    1 семестр; декабрь 2024 года
    Коростылев Егор ИУ7-14Б

    Задача:
            Требуется написать программу, которая позволит с помощью меню выполнить
        следующие действия:
        
            1. Выбрать файл для работы
            
            2. Инициализировать базу данных
            
            3. Вывести содержимое базы данных
            
            4. Добавить запись в произвольное место базы данных (пользователь указывает
                номер позиции, в которую должна быть вставлена запись)
            
            5. Удалить произвольную запись из базы данных (пользователь указывает номер удаляемой записи)
            
            6. Поиск по одному полю
            
            7. Поиск по двум полям
"""


from func import *


def main():
    file_name = None
    while True:
        if file_name is None:
            print('ФАЙЛ НЕ ВЫБРАН, АВТОМАТИЧЕСКИЙ ВЫБОР ПУНКТА НОМЕР 1')
            file_name = choose_file()
        main_table()
        command = input_int('Выберите команду: ')
        if command == 0:
            print("Удачи в жизненном пути.")
            break
        else:
            match command:
                case 1:
                    file_name = choose_file()
                case 2:
                    init(file_name)
                case 3:
                    display_content(file_name)
                case 4:
                    add_line(file_name)
                case 5:
                    del_line(file_name)
                case 6:
                    search_one(file_name)
                case 7:
                    search_two(file_name)

if __name__ == '__main__':
    main()
