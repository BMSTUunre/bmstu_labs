"""
Лабораторная работа по программированию №8
1 семестр; октябрь 2024 года
Коростылев Егор ИУ7-14Б 3 вариант

Задача 1:
В матрице найти строку, имеющую наибольшее количество чётных элементов.
"""


def main():
    # Блок 0: Ввод матрицы.
    print('Вводите матрицу построчно, пробелами разделяя элементы\nВвод заканчивается пустой строкой\n')

    matrix = []
    while line := input('> '):
        matrix.append([int(x) for x in line.split()])

    # Блок 1: Обработка матрицы.
    odd_count = 0
    line_index = -1
    for cur_i in range(len(matrix)):
        cur_count = 0

        for x in matrix[cur_i]:
            if abs(x) % 2 == 0:
                cur_count += 1

        if cur_count > odd_count:
            line_index = cur_i
            odd_count = cur_i

    # Блок 2: Вывод найденной строки
    if line_index == -1:
        print('Все строки тухлые ;/')
        return

    print(matrix[line_index])


if __name__ == '__main__':
    main()