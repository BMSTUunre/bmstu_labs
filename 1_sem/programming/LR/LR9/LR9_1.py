"""
Лабораторная работа по программированию №9
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 1:
Даны два одномерных целочисленных массива A и B. Сформировать матрицу M, такую что

    𝑚_𝑖𝑗 = 𝑎_𝑖 * 𝑏_𝑗.

Определить количество полных квадратов в каждой строке матрицы.
Записать значения в массив S. Напечатать матрицу M в виде матрицы и рядом столбецS.
"""
from aiogram.utils.formatting import as_list


def main():
    # Блок 0: Ввод матриц.
    print('Вводите элементы списка A по одному, ввод всего списка оканчивается пустой строкой')
    a_list = []
    while new_line := input('> ').lstrip('-').strip():
        while not new_line.isalnum():
            print('чет значение не похоже на адекватное введи новое')
            new_line = input('> ')
        a_list.append(int(new_line))

    print('Вводите элементы списка B по одному, ввод всего списка оканчивается пустой строкой')
    b_list = []
    while new_line := input('> ').lstrip('-').strip():
        while not new_line.isalnum():
            print('чет значение не похоже на адекватное введи новое')
            new_line = input('> ')
        b_list.append(int(new_line))


    # 1: Создание новой матрицы и ее заполнение
    if len(a_list) != len(b_list):
        print('Списки тухлые.')
        return


    m_matrix = [[0 for _ in range(len(a_list))] for _ in range(len(b_list))]

    for i in range(len(m_matrix)):
        for j in range(len(m_matrix[i])):
            m_matrix[i][j] = a_list[i] * b_list[j]

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