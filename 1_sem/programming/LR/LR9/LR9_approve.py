from math import floor

print('Вводите матрицу построчно, пробелами разделяя элементы\nВвод заканчивается пустой строкой\n')
matrix = []
while line := input('> '):
    matrix.append([int(i) for i in line.strip().split()])

print('Матрица до:')
for line in matrix:
    print('[', end='')
    for el in line:
        print(str(el).rjust(3), end=', ')
    print('\b\b]')

x = y = len(matrix)

for i in range(x):

    if i + 1 > floor(x / 2):
        m = floor(x / 2)
    else:
        m = i + 1

    for j in range(m):
        matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

print('Матрица между:')
for line in matrix:
    print('[', end='')
    for el in line:
        print(str(el).rjust(3), end=', ')
    print('\b\b]')

for i in range(x):

    if (x - i) > floor(x / 2):
        m = floor(x / 2)
    else:
        m = (x - i)

    for j in range(m):
        matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

print('Матрица после:')
for line in matrix:
    print('[', end='')
    for el in line:
        print(str(el).rjust(3), end=', ')
    print('\b\b]')

'''
1 2 3
4 5 6
7 8 9
'''