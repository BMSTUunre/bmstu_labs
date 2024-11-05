"""
Лабораторная работа по программированию №9
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 5:
    Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и
В. Вывести все матрицы в виде матриц.
"""

def main():
    # 0:
    print('Вводите матрицу A построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')
    a_matrix = []
    while line := input('> '):
        a_matrix.append([int(x) for x in line.split()])

    print('Вводите матрицу B построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')
    b_matrix = []
    while line := input('> '):
        b_matrix.append([int(x) for x in line.split()])

    if len(a_matrix) != len(b_matrix) or len(a_matrix[0]) != len(b_matrix[0]):
        print('Матрицы тухлые.')
        return


    # 1: Да, это можно сделать длиннее, но нафига если и так понятно
    c_matrix = [[a_matrix[i][j] * b_matrix[i][j] for j in range(len(a_matrix[i]))] for i in range(len(a_matrix))]


    # 2:
    print('Матрица A:')
    for line in a_matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')

    print('Матрица B:')
    for line in b_matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')

    print('Матрица C:')
    for line in c_matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')


if __name__ == '__main__':
    main()