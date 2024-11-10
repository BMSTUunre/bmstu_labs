"""
Лабораторная работа по программированию №9
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 2:
    Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
вводить. Транспонирование не применять.
"""

def main():
    # Блок 0: Ввод матрицы.
    print('Вводите матрицу построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')
    matrix = []
    while line := input('> '):
        matrix.append([int(x) for x in line.split()])  #

    if len(matrix) != len(matrix[0]):
        print('Матрица не квадратная')
        return

    print("\nИсходная:")
    for line in matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')

    # разворот по часовой:
    n = len(matrix)
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            (matrix[i][j],
             matrix[j][n - i - 1],
             matrix[n - i - 1][n - j - 1],
             matrix[n - j - 1][i]) = (matrix[j][n - i - 1],
                                      matrix[n - i - 1][n - j - 1],
                                      matrix[n - j - 1][i],
                                      matrix[i][j])

    print("\nПромежуточная:")
    for line in matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')

    # разворот против часовой
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            (matrix[i][j], 
             matrix[j][n - i - 1], 
             matrix[n - i - 1][n - j - 1], 
             matrix[n - j - 1][i]) = (matrix[n - j - 1][i], 
                                 matrix[i][j], 
                                 matrix[j][n - i - 1],
                                 matrix[n - i - 1][n - j - 1])

    # итоговая:
    print('\nИтоговая:')
    for line in matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')


if __name__ == '__main__':
    main()
'''
1  2  3  4
5  6  7  8
1  2  3  4
5  6  7  8

[  4,   8,   4,   8]
[  3,   7,   3,   7]
[  2,   6,   2,   6]
[  1,   5,   1,   5]

'''