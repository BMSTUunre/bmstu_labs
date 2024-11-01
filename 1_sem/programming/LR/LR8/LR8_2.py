"""
Лабораторная работа по программированию №8
1 семестр; октябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 2:
В матрице переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.
"""


def main():
    # Блок 0: Ввод матрицы.
    print('Вводите матрицу построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')
    matrix = []
    while line := input('> '):
        matrix.append([int(x) for x in line.split()])

    # Блок 1: Обработка матрицы.
    max_line_index, min_line_index = -1, -1
    max_count = -1
    min_count = -1

    for i in range(len(matrix)):
        cur_count = 0

        for x in matrix[i]:
            if x < 0:
                cur_count += 1

        if cur_count > max_count:
            max_line_index, max_count = i, cur_count

        if cur_count < min_count or min_count == -1:
            min_line_index, min_count = i, cur_count


    if max_count == -1 or max_count == -1:
        print('Все строки тухлые ;/')
        return

    matrix[max_line_index], matrix[min_line_index] = matrix[min_line_index], matrix[max_line_index]

    # Блок 2: Вывод строки
    print(f'Перемещены строки с индексами {min_line_index} и {max_line_index}.')
    for line in matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')


if __name__ == '__main__':
    main()
'''
2 2 2 2 2
0 0 0 0 0 
-1 -1 -1 -1 -1
-1 -1 0 0 0 
-1 2 2 2 2 
'''