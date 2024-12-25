from func import *


def main():
    menu()
    file_name = None
    command = 7
    db = 'БД_лаб13.txt'
    while command != 0:
        command = get_val('выберите команду: ')
        match command:
            case 1:
                file_name = choose_file()
            case 2:
                create_or_overwrite(file_name, db)
            case 3:
                if file_name is None:
                    display_content(db)
                else:
                    display_content(file_name)
            case 4:
                if file_name is None:
                    add_end(db)
                else:
                    add_end(file_name)
            case 5:
                if file_name is None:
                    search_one(db)
                else:
                    search_one(file_name)
            case 6:
                if file_name is None:
                    search_two(db)
                else:
                    search_two(file_name)
    else:
        exit()


if __name__ == '__main__':
    main()
