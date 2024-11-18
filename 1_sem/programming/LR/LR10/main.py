"""
Лабораторная работа по программированию №10
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача:
    1. Вычислить интеграл заданной функции двумя методами (серединных прямоугольников и парабол)

    2. Программа должна позволять задать начало и конец отрезка интегрирования, а также
        N1 и N2 - количества участков разбиения.

    3. Построить таблицу по методам и количеством отрезков

    4. На основе известной первообразной, вычислить какой метод более точный:
        4.1 Вычислить абсолютную и относительную погрешности для всех 4-х измерений, вывести их
        4.2 Метод, измерение которого с одним из разбиений дало самое близкое к первообразной
            значение, считается наиболее точным.

    5. Затем для другого, менее точного метода, итерационно вычислить количество участков
        разбиения, для которого интеграл будет вычислен с заданной точностью, на основе
        формулы:
                |𝐼(𝑁) − 𝐼(2𝑁)| < ε

    6. Вывести приближенное значение интеграла и количество отрезков, необходимых для
        его вычисления.

"""

from utils import input_int, input_float, draw_table, calc_error
from integral_utils import middle_rectangles, parabola, integral_by_antiderivative, iteration_calc_n


def main():
    print('Надеюсь вы задали функцию в нужном файлe..')

    start, stop = input_float('Введите начало интегрирования\n> '), input_float('Введите конец интегрирования\n> ')
    n1, n2 = input_int('Введите N1 участков разбиения\n> '), input_int('Введите N2 участков разбиения\n> ')

    rect1, rect2 = middle_rectangles(n1, start, stop), middle_rectangles(n2, start, stop)
    par1, par2 = parabola(n1, start, stop), parabola(n2, start, stop)

    print('Вычисленные значения интеграла.')
    draw_table(n1, n2, rect1, rect2, par1, par2)

    true_value = integral_by_antiderivative(start, stop)
    print('Настоящее значение интеграла: {:.12f}'.format(true_value))

    rect1_err = calc_error(rect1, true_value)
    rect2_err = calc_error(rect2, true_value)
    par1_err = calc_error(par1, true_value)
    par2_err = calc_error(par2, true_value)

    print('\nОтносительная погрешность метода серединных прямоугольников:')
    print('Первое измерение: отн. {:.10f}  абс. {:>10f} %'.format(*rect1_err))
    print('Второе измерение: отн. {:.10f}  абс. {:>10f} %'.format(*rect2_err))

    print('\nОтносительная погрешность метода парабол:')
    print('Первое измерение: отн. {:.10f}   абс. {:>10f} %'.format(*par1_err))
    print('Второе измерение: отн. {:.10f}   aбс. {:>10f} %'.format(*par2_err))

    best_calc = min(rect1_err[0], rect2_err[0], par1_err[0], par2_err[0])


    if par1_err[0] == best_calc or par2_err[0] == best_calc:
        print("\nМетод парабол (метод Симпсона) оказался наиболее точным.")
        calc_n = iteration_calc_n(0, start, stop)
        new_value = middle_rectangles(calc_n, start, stop)

    else:
        print("\nМетод серединных прямоугольников оказался наиболее точным.")
        calc_n = iteration_calc_n(1, start, stop)
        new_value = parabola(calc_n, start, stop)

    print('\nПриближенное значение интеграла : {:.10f}'.format(new_value))
    print(f'Которое удалось вычислить за кол-во отрезков равное : {calc_n}')


if __name__ == '__main__':
    main()