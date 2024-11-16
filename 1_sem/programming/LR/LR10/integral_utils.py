from utils import input_int, cramers_method
from math import sin, cos

''' Input Settings '''
def simple_func(x: int | float) -> int | float:
    return sin(x)


def antiderivative_func(x):
    return cos(x)


def get_eps():
    return 10 ** -5


''' Auto funcs '''

def cube_func(a, b, c):
    return lambda x: a * x ** 3 + b * x ** 2 + c * x

def find_antiderivative_by_func(a, b, c):
    return cube_func(a / 3, b / 2, c)


def middle_rectangles(func, n: int, start: int | float, stop: int | float) -> float:
    res = 0
    step_x = (stop - start) / n
    x = start
    while abs(x - stop) > get_eps():
        res += func(x + step_x / 2)
        x += step_x

    res *= step_x
    return res


def parabola(func, n: int, start: int | float, stop: int | float) -> float:
    while n < 2 or n % 2:
        print('Для метода парабол количество отрезков должно быть больше одного.')
        n = input_int('Введите кол-во отрезков\n> ')

    res = 0
    x = start
    step = (stop - start) / n
    while abs(x - stop) > get_eps():
        mid_x = x + step
        right_x = mid_x + step

        system = [
            [x ** 2,        x, 1,           simple_func(x)],
            [mid_x ** 2,    mid_x, 1,       simple_func(mid_x)],
            [right_x ** 2,  right_x, 1,     simple_func(right_x)]
        ]

        a, b, c = cramers_method(system)
        antiderivative = find_antiderivative_by_func(a ,b, c)

        res += antiderivative(right_x) - antiderivative(x)
        x += 2 * step

    return res
