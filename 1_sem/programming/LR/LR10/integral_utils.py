from utils import input_int, cramer_method
from math import sin, cos


''' Input Settings '''
def simple_func(x: int | float) -> int | float:
    """
    Необходимо ввести заданную функцию.
    """
    return sin(x)


def antiderivative_func(x):
    """
    Необходимо ввести Первообразную заданной функции.
    """
    return cos(x)


def get_eps():
    return 10 ** -5


''' Auto funcs '''

def cube_func(a, b, c):
    """
        Возвращает лямбда-функцию гиперболы.
    """
    return lambda x: a * x ** 3 + b * x ** 2 + c * x


def find_antiderivative_by_func(a, b, c):
    """
        Возвращает Первообразную параболы по ее коэффициентам a b c.
    """
    return cube_func(a / 3, b / 2, c)


def integral_by_antiderivative(x1, x2, antiderivative=None):
    """
        Находит интеграл функции по разности значений ее первообразной.
    """
    return antiderivative_func(x2) - antiderivative_func(x1) if antiderivative is None else antiderivative(x2) - antiderivative(x1)


def middle_rectangles(n: int, start: int | float, stop: int | float) -> float:
    """
        Вычисление интеграла методом суммы площадей серединных прямоугольников.
        Складываем все высоты прямоугольников, а потом умножаем на общую ширину

    """
    res = 0
    step_x = (stop - start) / n
    x = start
    while abs(x - stop) > get_eps():
        res += simple_func(x + step_x / 2)
        x += step_x

    res *= step_x
    return res


def parabola(n: int, start: int | float, stop: int | float) -> float:
    """
        Вычисление интеграла методом парабол (метод Симпсона).
        Выбираем 3 точки на функции, заносим их координаты в систему уравнений параболы.
        Методом Крамера решаем систему, находя коэффициенты a b c параболы.
        Находим первообразную найденной параболы.
        Вычисляем интеграл на этих двух промежутках, он равен разности значений первообразных.
    """
    while n < 2 or n % 2:
        print('Для метода парабол количество отрезков должно быть больше одного.')
        n = input_int('Введите кол-во отрезков\n> ')

    res = 0
    cur_x = start
    step_x = (stop - start) / n
    while abs(cur_x - stop) > get_eps():
        mid_x = cur_x + step_x
        right_x = mid_x + step_x

        system = [
            [cur_x ** 2,        cur_x, 1,   simple_func(cur_x)],
            [mid_x ** 2,    mid_x, 1,       simple_func(mid_x)],
            [right_x ** 2,  right_x, 1,     simple_func(right_x)]
        ]

        a, b, c = cramer_method(system)
        antiderivative = find_antiderivative_by_func(a ,b, c)

        res += integral_by_antiderivative(cur_x, right_x, antiderivative)
        cur_x += 2 * step_x

    return res


def iteration_calc_n(method_type: int, start: int | float, stop: int | float):
    """
       Вычисляет такой N, для которого верно неравенство:
            |𝐼(𝑁) − 𝐼(2𝑁)| < ε

        method type:
        0 - rectangles
        1 - parabola

    """
    func = middle_rectangles if method_type == 0 else parabola
    eps = get_eps()

    n = 1 if method_type == 0 else 2   # так как для метода парабол N должно быть кратно 2
    while abs(func(n, start, stop) - func(2 * n, start, stop)) >= eps:
        n += 1 if method_type == 0 else 2  # так как для метода парабол N должно быть кратно 2
    return n
