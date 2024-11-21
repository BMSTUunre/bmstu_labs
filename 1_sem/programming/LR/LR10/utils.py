def input_int(text: str, allow_negative=True, allow_zero=True):
    n = input(text).strip()
    while not ((allow_negative and n.lstrip('-').isalnum() or n.isalnum()) and (allow_zero or int(n) > 0)):
        print('Значение должно быть целочисленным.')
        n = input(text).strip()
    return int(n)


def input_float(text: str, only_positive=False, not_null=False):
    try:
        n = float(input(text))
        while (only_positive and n < 0) or (not_null and n == 0):
            print('Неверное значение, повторите ввод.')
            n = float(input(text))
        return n

    except Exception:
        print('Неверное значение, повторите ввод.')
        return input_float(text, only_positive, not_null)


def matrix_determinant(matrix: list[list[int | float]]) -> int | float:
    """
        Returns the determinant of square matrix:
            | x_1  y_1  z_1 |
            | x_2  y_2  z_2 |
            | x_3  y_3  z_3 |
    """
    n = len(matrix)
    det = 0

    for i in range(n):
        main_line, alternative_line = 1, 1
        for j in range(n):
            main_line *= matrix[j][(i + j) % n]
            alternative_line *= matrix[-j - 1][(i + j) % 3]
        det += main_line
        det -= alternative_line

    return det


def cramer_method(system: list[list[int | float]]) -> (float, float):
    """
        In the system like:
            a_1 * x + b_1 * y + z = d_1
            a_2 * x + b_2 * y + z = d_2
            a_3 * x + b_3 * y + z = d_3

        Returns the (x, y, z)
    """

    matrix = [equation[:-1] for equation in system]
    general_det = matrix_determinant(matrix)

    x_matrix = [[el for el in line] for line in matrix]
    y_matrix = [[el for el in line] for line in matrix]
    z_matrix = [[el for el in line] for line in matrix]

    for i in range(3):
        x_matrix[i][0] = system[i][3]
        y_matrix[i][1] = system[i][3]
        z_matrix[i][2] = system[i][3]

    x_det = matrix_determinant(x_matrix)
    y_det = matrix_determinant(y_matrix)
    z_det = matrix_determinant(z_matrix)

    x, y, z = x_det / general_det, y_det / general_det, z_det / general_det

    return x, y, z


def draw_table(n1, n2, rect1, rect2, par1, par2):
    cell_width = 20 # больше 10
    line = '-' * cell_width
    gap = ' ' * cell_width
    vertical = '+{0}+{0}+{0}+'.format(line)
    center_func = lambda x: x.center(cell_width)

    mas = [
        [gap, str(n1), str(n2)],
        ['rectangles', '{:.6g}'.format(rect1), '{:.6g}'.format(rect2)],
        ['parabola', '{:.6g}'.format(par1), '{:.6g}'.format(par2)]
    ]

    mas = [list(map(center_func, line)) for line in mas]

    print(vertical)

    for stroke in mas:
        print('|', end='')
        print(*stroke, sep='|', end='|\n')
        print(vertical)


def calc_error(calc_value, true_value) -> (float, float):
    """
    Возвращает относительную и абсолютную погрешность
    """
    relative_err = abs(calc_value - true_value)
    absolute_err = relative_err / true_value * 100
    return relative_err, absolute_err
