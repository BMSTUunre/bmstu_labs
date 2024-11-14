"""
Лабораторная работа по программированию №9
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 4:
    Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
среднее арифметическое значение.
"""

def main():
    # Блок 0: Ввод матрицы и списка.
    print('Вводите матрицу D построчно, пробелами разделяя элементы\nВвод заканчивается пустой строкой\n')
    d_matrix = []
    while line := input('> ').strip():
        d_matrix.append([int(x) for x in line.split()])

    i_list = [int(i) for i in line.split('Введите элементы списка I через пробел')]


    # 1:
    r_list = [None for _ in range(len(i_list))]
    for index in i_list:
        for x in d_matrix[index]:
            if r_list[index] is None or x > r_list[index]:
                r_list[index] = x

    sum_avg = 0
    for x in r_list:
        sum_avg += x

    average_r_list = sum_avg / len(r_list) if len(r_list) else 0

    # 2:
    print("Матрица D:")
    for line in d_matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(6), end=', ')
        print('\b\b]')

    print('Массив I:')
    for x in i_list:
        print('{:>6.2f}'.format(x), end='  ')

    print('\nМассив R:')
    for x in r_list:
        print('{:>6.2f}'.format(x), end='  ')

    print("\nAvg for R list:", average_r_list)  #


if __name__ == '__main__':
    main()