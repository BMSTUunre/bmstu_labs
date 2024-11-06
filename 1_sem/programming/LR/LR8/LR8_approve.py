'''
Сформировать вектор А из ненулевых элементов целочисленной матрицы R,
которую просматривать по столбцам. В полученном векторе третий положительный (по
номеру) элемент заменить произведением остальных элементов вектора. Если в
векторе А будет меньше трех положительных элементов, то напечатать
соответствующий текст. Напечатать матрицу R в виде матрицы и вектор А.
'''
from os import pread


def main():
    print('Вводите матрицу R построчно, пробелами разделяя элементы\nВвод заканчивается пустой строкой\n')

    r_matrix = []
    while line := input('> '):
        r_matrix.append([int(x) for x in line.split()])

    vector = []

    for j in range(len(r_matrix[0])):
        for line in r_matrix:
            if line[j] != 0:
                vector.append(line[j])

    if len(vector) < 3:
        print('Матрица тухлая.')
        return
    else:
        product_in_vector = vector[0] * vector[1]
        for i in range(3, len(vector)):
            product_in_vector *= vector[i]
        vector[2] = product_in_vector

    print('matrix: ')
    for line in r_matrix:
        print('[', end='')
        for x in line:
            print(str(x).rjust(2), end=', ')
        print('\b\b]')

    print('vector: ')
    print(vector)


if __name__ == '__main__':
    main()