import struct
from struct import pack, unpack
from pprint import pprint

'''
Решеткой Кардано называется квадратная матрица 0 и 1, где 1 – вырезанная ячейка.
Решетка хранится в виде набора десятичных чисел: каждая строка матрицы рассматривается как число в двоичной системе
счисления и переводится в десятичную систему счисления.
Шифрование текста с помощью решетки Кардано осуществляется путем ее наложения на матрицу-шифр (изначально пустую) и записи
шифруемого текста в вырезанные ячейки. Затем производится троекратное повторение этой процедуры с предварительным поворотом
решетки на 90º по часовой стрелке. В результате получается матрица с зашифрованным сообщением.
Даны бинарный файл in.bin, в котором записана квадратная матрица символов (тип char, формат c в модуле struct),
и текстовый файл key.txt, в котором записаны числа (одно число в строке) в десятичной системе счисления, являющиеся представлением шифрующей решетки.
Получить и вывести расшифрованную строку S. Считывать единовременно более одного символа матрицы из файла в память запрещено.
'''
def matrix_len() -> int:
    with open("in.bin", 'rb') as f:
        n = 3
        # n = len(unpack('hhh' ,f.readline()))
    return n


def rotated_index(x: int, y: int, n: int, rot: int=0) -> tuple[int, int]:
    if x <= n // 2:
        if y <= n // 2:
            x, y = y, n - x - 1
            if rot == 0:
                return x, y
            return rotated_index(x, y, n, rot - 1)
        else:
            x, y = n - y - 1, x
            if rot == 0:
                return x, y
            return rotated_index(x, y, n, rot - 1)

    elif y <= n // 2:
        x, y = n - x - 1, y
        if rot == 0:
            return x, y
        return rotated_index(x, y, n, rot - 1)
    else:
        x, y = n - y - 1, n - x - 1
        if rot == 0:
            return x, y
        return rotated_index(x, y, n, rot - 1)

'''
 matrix[i][j] left up
 matrix[j][n - i - 1] right up
 matrix[n - i - 1][n - j - 1] right down
 matrix[n - j - 1][i] left down
'''


def key_matrix(n) -> list[list[int]]:
    matrix = []
    with open("key.txt", 'r') as f:
        for num in f.readlines():
            if num.strip().replace('\n', ''):
                bi = format(int(num.strip().replace('\n', '')), 'b')
                bi = '0' * (n - len(bi)) + bi
                matrix.append([int(i) for i in bi])
    return matrix


def element_of_matrix(x: int, y: int):
    with open("in.bin", "rb") as file:
        for _ in range(x + 1):
            line = file.read(6)
    elem = struct.unpack('hhh', line)[y]
    return elem


def main():
    n = matrix_len()
    key = key_matrix(n)
    result = ''
    for rot in range(4):
        for x in range(n):
            for y in range(n):
                if key[x][y]:
                    result += str(element_of_matrix(*rotated_index(x, y, n, rot)))
    print(result)


def fill_bin():
    with open("in.bin", 'wb') as f:
        # line = '123456789'
        #
        # for i in range(0, 9, 3):
        #     f.write(pack('hhh', int(line[i]), int(line[i + 1]), int(line[i + 2])))
        f.write(pack('hhh', 1, 2, 3))
        f.write(pack('hhh', 4, 5, 6))
        f.write(pack('hhh', 7, 8, 9))

if __name__ == '__main__':
    fill_bin()
    main()
