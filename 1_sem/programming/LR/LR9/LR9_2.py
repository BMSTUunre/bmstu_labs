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
        matrix.append([int(x) for x in line.split()])

    print("\nИсходная:")
    for line in matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')

    # 1 по часовой:
    for layer in range(len(matrix) // 2):
        first = layer
        last = len(matrix) - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top

    print("\nПромежуточная:")
    for line in matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')

    # 2: против часовой
    for layer in range(len(matrix) // 2):
        first = layer
        last = len(matrix) - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[i][last]
            matrix[i][last] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[last - offset][first]
            matrix[last - offset][first] = top

    # 4 итоговая:
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

5  1  5  1
6  2  6  2
7  3  7  3
8  4  8  4

'''