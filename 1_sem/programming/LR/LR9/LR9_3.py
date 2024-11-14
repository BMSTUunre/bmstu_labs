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
    x_a, y_a = (int(i) for i in input('Введите через пробел размер матрицы А\nx y > ').split())
    a_matrix = []
    for i in range(y_a):
        line = input(f'Введите {i} строку матрицы.\n> ').strip().split()
        while len(line) != x_a or any([not i.strip().lstrip('-').isalnum() for i in line]):
            line = input('Введите адекватную строку.\n> ').strip().split()
        a_matrix.append([int(i) for i in line])


    x_b, y_b = (int(i) for i in input('Введите через пробел размер матрицы B\n> ').split())
    b_matrix = []
    for i in range(y_b):
        line = input(f'Введите {i} строку матрицы.\n> ').strip().split()
        while len(line) != x_b or any([not i.strip().lstrip('-').isalnum() for i in line]):
            line = input('Введите адекватную строку.\n> ').strip().split()
        b_matrix.append([int(i) for i in line])

    if x_a != x_b:
        print('Кол-во столбцов в матрицах не равно')
        return

    average_b_list = []

    for j in range(x_b):
        col_sum = 0
        for line in b_matrix:
            col_sum += line[j]
        average_b_list.append(col_sum / y_b)

    counter = []

    for j in range(x_a):
        col_counter = 0
        avg = average_b_list[j]
        for line in a_matrix:
            if line[j] > avg:
                col_counter += 1
        counter.append(col_counter)


    print("Матрица А:")
    for line in a_matrix:
        print('[', end='')
        for x in line:
            print(str(x).center(5), end=', ')
        print('\b\b]')


    print('\nСчетчик:')
    print('[', end='')
    for x in counter:
        print('{:^5}'.format(x), end=', ')
    print('\b\b]')

    print('\nСр. знач. столбцов B:')
    print('[', end='')
    for x in average_b_list:
        print('{:^5}'.format(x), end=', ')
    print('\b\b]')


    for j in range(x_b):
        for line in b_matrix:
            if average_b_list[j] !=0:
                line[j] *= average_b_list[j]

    print("\nМатрица B:")
    for line in b_matrix:
        print('[', end='')
        for x in line:
            print(str(x).center(5), end=', ')
        print('\b\b]')


if __name__ == '__main__':
    main()
