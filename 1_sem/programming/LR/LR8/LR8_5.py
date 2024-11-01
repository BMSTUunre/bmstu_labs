"""
Лабораторная работа по программированию №8
1 семестр; октябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 5:
В матрице найти максимальное значение в квадратной матрице над главной диагональю
и
минимальное - под побочной диагональю.
"""


def main():
    # Блок 0: Ввод матрицы.
    print('Вводите матриц построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')

    matrix = []
    while line := input('> '):
        matrix.append([int(x) for x in line.split()])

    # Блок 1: Обработка матрицы.
    if len(matrix) < 3 or len(matrix[0]) < 3:
        print('Вся таблица тухлая ;/')

    max_up_main = matrix[0][-1]

    for line_i in range(len(matrix) - 1):
        for col_i in range(line_i + 1, len(matrix[line_i])):
            if matrix[line_i][col_i] > max_up_main:
                max_up_main = matrix[line_i][col_i]

    min_under_alt = matrix[-1][-1]

    for line_i in range(1, len(matrix)):
        for col_i in range(len(matrix[line_i]) - line_i, len(matrix[line_i])):
            if matrix[line_i][col_i] < min_under_alt:
                min_under_alt = matrix[line_i][col_i]

    # Блок 2: Вывод
    print('Максимальный элемент над главной диагональю -', max_up_main)
    print('Минимальный элемент под побочной диагональю -', min_under_alt)


if __name__ == '__main__':
    main()