"""
Лабораторная работа по программированию №8
1 семестр; октябрь 2024 года
Коростылев Егор ИУ7-14Б 2 вариант

Задача 3:
В матрице найти столбец, имеющий наименьшее количество отрицательных элементов.
"""


def main():
    # Блок 0: Ввод матрицы.
    print('Вводите матрицу построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')

    matrix = []
    while line := input('> '):
        matrix.append([int(x) for x in line.split()])

    # Блок 1: Обработка матрицы.
    neg_count = -1
    min_column_index = 0

    for col_index in range(len(matrix[0])):
        cur_count = 0

        for line_index in range(len(matrix)):
            if matrix[line_index][col_index] < 0:
                cur_count += 1

        if cur_count < neg_count or neg_count == -1:
            neg_count, min_column_index = cur_count, col_index

    if neg_count == -1:
        print('Все столбцы тухлые ;/')
        return

    # Блок 2: Вывод столбца
    print(f'Индекс столбца, являющегося ответом - {min_column_index}\n+-----+')
    for line_index in range(len(matrix)):
        x = matrix[line_index][min_column_index]
        print(f'|{x:^5}|')
    print('+-----+')


if __name__ == '__main__':
    main()