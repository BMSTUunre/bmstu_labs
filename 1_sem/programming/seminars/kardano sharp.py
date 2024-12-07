from random import randint
from math import floor


def input_line() -> str:
    line = ''
    ru_A, ru_ya = 1040, 1103
    for c in input('Введите строку\n>'):
        if ru_A <= ord(c) <= ru_ya:
            line += c
    return line


def rotate_matrix(matrix: list[list[str]]) -> None:
    n = len(matrix)
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            (matrix[i][j],
             matrix[j][n - i - 1],
             matrix[n - i - 1][n - j - 1],
             matrix[n - j - 1][i]) = (matrix[j][n - i - 1],
                                      matrix[n - i - 1][n - j - 1],
                                      matrix[n - j - 1][i],
                                      matrix[i][j])


def output(sharp: list[list[str]], zipped_sample: list[int]) -> None:
    print('\nЗашифрованная строка:')
    for line in sharp:
        print('[', end='')
        for x in line:
            print(str(x).rjust(3), end=', ')
        print('\b\b]')

    print('\nCжатая решетка:')
    for x in zipped_sample:
        print(x, end='  ')


def zip_sample(sample: list[list[int]], matrix_order: int) -> list[int]:
    zipped_sample = []
    for i in range(matrix_order):
        b = 0
        for el in sample[i]:
            b += 2 ** (matrix_order - el - 1)

        zipped_sample.append(b)

    return zipped_sample


def fill_sharp(matrix_order: int, sample: list[list[int]], line: str) -> list[list[str]]:
    sharp = [['' for _ in range(matrix_order)] for _ in range(matrix_order)]
    cur_i = 0

    for _ in range(4):
        for i in range(matrix_order):
            for j in sample[i]:
                sharp[i][j] = line[cur_i]
                cur_i += 1
        rotate_matrix(sharp)

    return sharp


def make_sample(matrix_order: int) -> list[list[int]]:
    sample = [[] for _ in range(n)]

    for i in range(matrix_order // 2):
        for j in range(matrix_order // 2):
            random = randint(1, 4)
            if random == 1:
                sample[i].append(j)
            elif random == 2:
                sample[j].append(matrix_order - i - 1)
            elif random == 3:
                sample[matrix_order - i - 1].append(matrix_order - j - 1)
            else:
                sample[matrix_order - j - 1].append(i)

    return sample


line = input_line()

n = len(line)
matrix_order = floor(n ** 0.5)
matrix_order += matrix_order % 2

sample = make_sample(matrix_order)
sharp = fill_sharp(matrix_order, sample, line)
zipped_sample = zip_sample(sample, matrix_order)


output(sharp, zipped_sample)
