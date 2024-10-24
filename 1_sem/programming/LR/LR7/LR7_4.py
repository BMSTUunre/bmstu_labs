"""
Лабораторная работа по программированию №7
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б 3 вариант

Задача 4:
Замена всех заглавных согласных английских букв на строчные в списке строк по варианту.
A - 65 Z - 90 a - 97 z - 122
32 (a - A)
"""


def main():
    # Блок 0: Ввод массива и создание кортежа заглавных гласных.
    print('Вводите строки массива по одной, ввод всего списка оканчивается пустой строкой')
    array = []
    glas = ("A", "E", "U", "I", "O", "Y")
    while new_line := input('> '):
        array.append(new_line)

    # Блок 1: Сама магия
    for index in range(len(array)):
        line = array[index]
        new_line = ''  # будем заменять целый элемент массива
        for letter in line:
            if (65 <= ord(letter) <= 90) and (letter in glas):  # если символ является заглавной согласной
                new_line += chr(ord(letter) + 32)  # сдвигаем по unicode таблице
            else:
                new_line += letter  # иначе не меняем
        array[index] = new_line

    return array


if __name__ == '__main__':
    print(main())
