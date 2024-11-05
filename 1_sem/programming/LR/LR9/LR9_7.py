"""
Лабораторная работа по программированию №9
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 7:
    Ввести трёхмерный массив (массив матриц размера X*Y*Z). Вывести срез
массива по большему измерению, индекс среза – середина размерности с
округлением в меньшую сторону.
"""

def main():
    # 0:
    x, y, z = (int(i) for i in input('Введите 3 размера трехмерного массива через пробел\n> ').split())

    mega_matrix = []

    for x_ind in range(x):
        matrix = []
        for y_ind in range(y):
            array = [int(i) for i in input(f'Введите {y_ind} строку {x_ind} матрицы\n> ').strip().split()]
            matrix.append(array)
        mega_matrix.append(matrix)

    # for matrix in mega_matrix:
    #     print('\n')
    #     print(*matrix, sep='\n')

    # 1:
    max_d = 0

    if x > y:
        if x > z:
            max_d = x
        else:
            max_d = z
    elif y > z:
        max_d = y
    else:
        max_d = z

    max_d = (max_d - 1) // 2

    for matrix in mega_matrix:
        print(matrix[max_d])


if __name__ == '__main__':
    main()
'''
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
8 8 8
9 9 9

'''