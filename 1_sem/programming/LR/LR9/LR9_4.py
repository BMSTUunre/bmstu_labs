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
    print('Вводите матрицу D построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')
    d_matrix = []
    while line := input('> ').strip():
        d_matrix.append([int(x) for x in line.split()])

    print('Вводите элементы списка I по одному, ввод всего списка оканчивается пустой строкой')
    i_list = []
    while new_line := input('> ').strip():
        while not new_line.isalnum() or int(new_line) > len(d_matrix) :
            print('чет значение не похоже на адекватное введи новое')
            new_line = input('> ')
        i_list.append(int(new_line))


    # 1:
    r_list = [None for _ in range(len(i_list))]
    for index in i_list:
        for x in d_matrix[index]:
            if r_list[index] is None or x > r_list[index]:
                r_list[index] = x

    sum_avg = 0
    for x in r_list:
        sum_avg += x

    average_r_list = sum_avg / len(r_list) if sum_avg else 0

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

    print("\nAvg for R list:", average_r_list)


if __name__ == '__main__':
    main()