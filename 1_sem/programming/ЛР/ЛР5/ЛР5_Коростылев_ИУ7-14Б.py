"""
Лабораторная работа по программированию №5
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б 49 вариант

Прога для вывода таблички значений функции
и рисования графика функции в консоли


y1 = sin(t) + 0.6 * t * cos(t)
y2 = t^3 - 5.09x^2 + 4.57x + 3.2

t_0 = 1.5
step = 0.1
t_n = 2.0

"""
# Блок 0: Подключение необходимых библиотек
from math import sin, cos


# Блок 1: Ввод изначальных данных
x_0 = float(input("Введите значение x0: "))

step = float(input("Введите значение шага: "))

x_n = float(input("Введите значение xn: "))

if step > x_n - x_0 or x_n <= x_0:
    print('не балуйся')
    exit()

# Блок 2: Ввод базовых параметров
x = x_0
max_y = False
min_y = False
additional_task = 0

# Блок 3: Рисование таблицы и подсчет необходимых значений
print('+---------------------------------------+')
print('|     x     |      y1     |      y2     |')
print('+‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾+')

while x <= x_n:
    y1 = sin(x) + 0.6 * x * cos(x)
    y2 = x ** 3 - 5.09 * x ** 2 + 4.57 * x + 3.2
    if 0.2 <= y1 <= 1.6:
        additional_task += 1
    if min_y == False or y1 < min_y:
        min_y = y1
    if max_y == False or y1 > max_y:
        max_y = y1
    print('|{0:^11g}|{1:^13g}|{2:^13g}|'.format(x, y1, y2))
    x += step

print('+‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾+')
print('\n ___ Additional_task = {} ___\n'.format(additional_task))

# Блок 4: Ввод параметров для графика
graph_widht = 80
x_line_widht = 8
x_lines_num = int((x_n - x_0) // step) + 1
cut_points_num = int(input("Введите целочисленное положительное кол-во засечек (от 4 до 8-ми): "))
eps = abs(min_y - max_y) / (graph_widht - x_line_widht)
cut_space = (graph_widht - x_line_widht) // cut_points_num + 1
spaces_min_to_0 = int(abs(min_y) // eps - 1)
spaces_0_to_max = int(max_y // eps - 1)


for i in range(cut_points_num):
    num = (max_y - min_y) / (cut_points_num - 1) * i + min_y
    print(('{0:' + '>{}'.format(cut_space) + '}').format('{:.5f}'.format(num)), end='')
print()

if min_y <= 0 <= max_y:
    
    for x_step in range(x_lines_num):
        cur_x = x_0 + x_step * step
        print('|{0:^6g}|'.format(cur_x), end='')
        cur_y = sin(cur_x) + 0.6 * cur_x * cos(cur_x)
        
        if cur_y <= 0:
            if (abs(cur_y) - eps) < eps:
                print(' ' * spaces_min_to_0 + '*' + ' ' * spaces_0_to_max)
            else:
                spaces_min_to_cur = int(abs(cur_y - min_y - (eps / 2)) // eps)  # - (eps / 2) не включительно брать точку
                spaces_cur_to_0 = spaces_min_to_0 - spaces_min_to_cur - 1
                print(' ' * spaces_min_to_cur + '*' + ' ' * spaces_cur_to_0 + '|' + ' ' * spaces_0_to_max)
        else:
            spaces_0_to_cur = int((cur_y) // eps - 1)
            spaces_cur_to_max = int((max_y - cur_y + (eps / 2)) // eps - 1)
            print(' ' * spaces_min_to_0 + '|' + ' ' * spaces_0_to_cur + "*" + ' ' * spaces_cur_to_max)
else:x
    for x_step in range(x_lines_num):
        cur_x = x_0 + x_step * step
        print('|{0:^7.2}|'.format(cur_x), end='')
        cur_y = sin(cur_x) + 0.6 * cur_x * cos(cur_x)
        spaces_min_to_cur = int((cur_y - min_y - (eps / 2)) // eps)  # - (eps / 2) не включительно брать точку
        spaces_cur_to_max = int((max_y - cur_y) // eps - 1)
        print(' ' * spaces_min_to_cur + "*" + ' ' * spaces_cur_to_max)