def input_int(text: str, allow_nagative=True, allow_zero=True):
    n = input(text).strip()
    while not ((allow_nagative and n.lstrip('-').isalnum() or n.isalnum()) and (allow_zero or int(n) > 0)):
        print('Значение должно быть целочисленным.')
        n = input(text).strip()
    return int(n)


def matrix_determinant(matrix: list[list[int | float]]) -> int | float:
    """
    Returns the determinant:
        | x_1  y_1  z_1 |
        | x_2  y_2  z_2 |
        | x_3  y_3  z_3 |
    """

    det = 0
    for i in range(3):
        det += matrix[0][i] * matrix[1][(i + 1) % 3] * matrix[2][(i + 2) % 3]
        det -= matrix[2][i] * matrix[1][(i + 1) % 3] * matrix[0][(i + 2) % 3]

    return det


def cramers_method(system: list[list[int | float]]) -> (float, float):
    """
    In the system like:
        a_1 * x + b_1 * y + z = d_1
        a_2 * x + b_2 * y + z = d_2
        a_3 * x + b_3 * y + z = d_3

    Returns the (x, y)
    """

    matrix = [equation[:-1] for equation in system]
    general_det = matrix_determinant(matrix)

    x_matrix, y_matrix, z_matrix = matrix.copy(), matrix.copy(), matrix.copy()

    for i in range(3):
        x_matrix[0][i] = system[3][i]
        y_matrix[1][i] = system[3][i]
        z_matrix[2][i] = system[3][i]

    x_det = matrix_determinant(x_matrix)
    y_det = matrix_determinant(y_matrix)
    z_det = matrix_determinant(z_matrix)

    x, y, z = x_det / general_det, y_det / general_det, z_det / general_det

    return x, y, z
