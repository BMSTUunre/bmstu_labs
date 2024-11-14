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
    mega_matrix = []
    z = int(input('Введите Z: количество матриц\n> '))
    while z < 1:
        z = int(input('Введите Z: количество матриц\n> '))
    y = int(input('Введите Y: количество строк в матрице\n> '))
    while y < 1:
        y = int(input('Введите Y: количество строк в матрице\n> '))

    for z_i in range(z):
        matrix = []
        for y_i in range(y):
            line = [int(i) for i in input(f'Введите {y_i + 1} строку {z_i + 1} матрицы\n> ').strip().split()]

            matrix.append(line)
        mega_matrix.append(matrix)

    print('[')
    x = len(mega_matrix[0][0])
    if x > y:
        if x > z:
            middle = (x - 1) // 2
            print(*[[matrix[i][middle] for matrix in mega_matrix]  for i in range(y)], sep='\n')
        else:
            middle = (z - 1) // 2
            print(*mega_matrix[middle], sep='\n')
    elif z > y:
        middle = (z - 1) // 2
        print(*mega_matrix[middle], sep='\n')
    else:
        middle = (y - 1) // 2
        print(*[matrix[middle] for matrix in mega_matrix], sep='\n')

    print(']')


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