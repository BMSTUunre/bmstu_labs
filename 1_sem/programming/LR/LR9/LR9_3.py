"""
Лабораторная работа по программированию №9
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 3:
    Даны две матрицы A и B, в которых количество столбцов одинаково.
Подсчитать для каждого столбца матрицы А количество элементов, больших
среднего арифметического элементов соответствующего столбца матрицы В.
    Вывести полученные значения. Затем преобразовать матрицу В путем
умножения всех элементов столбца матрицы на посчитанное для этого столбца
значение, если оно ненулевое. Вывести преобразованную матрицу в виде
матрицы.
"""


def main():
    # Блок 0: Ввод матриц.
    print('Вводите матрицу A построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')

    a_matrix = []
    while line := input('> ').strip():
        a_matrix.append([int(x) for x in line.split()])

    print('Вводите матрицу B построчно, пробелами разделяя элементы\nВвод заканчивается пусто строкой\n')

    b_matrix = []
    while line := input('> ').strip():
        b_matrix.append([int(x) for x in line.split()])

    # 1:
    average_b_list = [0 for _ in range(len(b_matrix[0]))]

    for j in range(len(b_matrix[0])):
        column_sum = 0
        for i in range(len(b_matrix)):
            column_sum += b_matrix[i][j]

        average_b_list[j] = column_sum / (i + 1) if column_sum else 0

    # 2:
    print("Матрица А:")
    for line in a_matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(6), end=', ')
        print('\b\b]')

    # 3:
    print('\nCounter:', end='\n ')
    for j in range(len(a_matrix[0])):
        counter = 0
        for i in range(len(a_matrix)):
            if a_matrix[i][j] > average_b_list[j]:
                counter += 1
        print(str(counter).rjust(6), end='  ')

    print('\nAvg B columns:', end='\n ')
    for x in average_b_list:
        print('{:>6.2f}'.format(x), end='  ')




if __name__ == '__main__':
    main()

