"""
Лабораторная работа по программированию №8
1 семестр; октябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 6:
В матрице выполнить транспонирование квадратной матрицы.
"""


def main():
    # Блок 0: Ввод матрицы.
    print('Вводите матриц построчно, пробелами разделяя элементы\nВвод заканчивается пустой строкой\n')

    matrix = []
    while line := input('> '):
        matrix.append([x for x in line.split()])

    # Блок 1: Обработка матрицы.
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Блок 2: Вывод
    for line in matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(2), end=', ')
        print('\b\b]')


if __name__ == '__main__':
    main()