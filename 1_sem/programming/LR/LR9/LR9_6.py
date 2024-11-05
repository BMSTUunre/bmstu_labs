"""
Лабораторная работа по программированию №9
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 6:
    Дана матрица символов. Преобразовать её следующим образом: заменить все
согласные латинские буквы на заглавные, а все гласные латинские буквы на
строчные. Вывести матрицу до преобразования и после.

A - 65 Z - 90 a - 97 z - 122
32 (A - a)
"""

def main():
    # 0:
    print('Вводите матрицу построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')
    matrix = []
    while line := input('> ').strip():
        matrix.append([str(x)[0] for x in line.split()])

    # 1:
    print('Матрица до:')
    print(*matrix, sep='\n')

    # 2:
    glas = ("A", "E", "U", "I", "O", "Y")

    for line in matrix:
        for index in range(len(line)):
            if 65 <= ord(line[index].upper()) <= 90:
                if line[index].upper() in glas:
                    line[index] = line[index].lower()
                else:
                    line[index] = line[index].upper()

    # 3:
    print('Матрица после:')
    print(*matrix, sep='\n')


if __name__ == '__main__':
    main()