"""
Лабораторная работа по программированию №9
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 1:
Даны два одномерных целочисленных массива A и B. Сформировать матрицу M, такую что

    𝑚𝑖𝑗 = 𝑎𝑖 * 𝑏𝑗.

Определить количество полных квадратов в каждой строке матрицы.
Записать значения в массив S. Напечатать матрицу M в виде матрицы и рядом столбецS.
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


    # 1: Создание новой матрицы и ее заполнение
    if len(a_matrix) != len(b_matrix) or len(a_matrix[0]) != len(b_matrix[0]):
        print('Матрицы тухлые.')
        return


    m_matrix = [[0 for _ in range(len(a_matrix[0]))] for _ in range(len(a_matrix))]

    for i in range(len(m_matrix)):
        for j in range(len(m_matrix[i])):
            m_matrix[i][j] = a_matrix[i][j] * b_matrix[i][j]

    # 2:
    s_list = [0 for _ in range(len(m_matrix))]
    for i in range(len(m_matrix)):
        for j in range(len(m_matrix[i])):
            x = m_matrix[i][j] ** 0.5
            if x == int(x):
                s_list[i] += 1

    # 3:

    for line in m_matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')

if __name__ == '__main__':
    main()