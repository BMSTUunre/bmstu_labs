"""
Лабораторная работа по программированию №8
1 семестр; октябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 4:
В матрице переставить местами столбцы с максимальной и минимальной суммой
элементов.
"""


def main():
    # Блок 0: Ввод матрицы.
    print('Вводите матрицу построчно, пробелами разделяя элементы\nВвод заканчивается пустой строкой\n')

    matrix = []
    while line := input('> '):
        matrix.append([int(x) for x in line.split()])

    # Блок 1: Обработка матрицы.
    max_sum, min_sum = 0, 0
    max_sum_col_index, min_sum_col_index = -1, -1

    for col_index in range(len(matrix[0])):
        sum_count = 0

        for line in matrix:
            sum_count += line[col_index]

        if sum_count < min_sum or min_sum_col_index == -1:
            min_sum, min_sum_col_index = sum_count, col_index

        if sum_count > max_sum or max_sum_col_index == -1:
            max_sum, max_sum_col_index = sum_count, col_index

    if max_sum_col_index == -1:
        print('Все столбцы тухлые ;/')
        return

    for line in matrix:
        line[max_sum_col_index], line[min_sum_col_index] = line[min_sum_col_index], line[max_sum_col_index]

    # Блок 2: Вывод
    print(f'Перемещены строки с индексами {min_sum_col_index} и {max_sum_col_index}.')
    for line in matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(2), end=', ')
        print('\b\b]')

if __name__ == '__main__':
    main()