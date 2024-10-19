from math import exp

x_0 = float(input("Введите значение x0: "))
x_n = float(input("Введите значение xn: "))
step_value = float(input("Введите значение шага: "))

if step_value > x_n - x_0 or x_n <= x_0:
    print('значения некорректны')
    exit()

max_y = False
min_y = False
steps_count = int(abs(x_n - x_0) // step_value) + 1

for cur_step in range(steps_count):
    cur_x = x_0 + cur_step * step_value
    cur_y = - (cur_x ** 2) + 9
    if max_y == False or cur_y > max_y:
        max_y = cur_y
    if min_y == False or cur_y < min_y:
        min_y = cur_y


graph_widht = 80
x_widht = 7
ceil_value = abs(min_y - max_y) / (graph_widht - x_widht)
left = (graph_widht - x_widht) // 2
right = left + (graph_widht - x_widht) % 2
eps = exp(-100)

print(('  x   |' + '{0:<' + f"{graph_widht - x_widht}" + '.3f}{1:.3f}').format(min_y, max_y))
cur_x = x_0

if min_y <= 0 <= max_y:
    spaces_min_to_0 = int(abs(min_y) // ceil_value)
    spaces_0_to_max = int(abs(max_y) // ceil_value)
    while cur_x < x_n or abs(cur_x - x_n) < eps:
        cur_y = - (cur_x ** 2) + 9
        print("{:^6g}|".format(cur_x), end='')
        if (abs(cur_y) - ceil_value) < 0:
            print(' ' * spaces_min_to_0 + '*' + ' ' * spaces_0_to_max)
        elif cur_y < 0:
            spaces_min_to_cur = int(abs(cur_y - min_y) // ceil_value)
            spaces_cur_to_0 = spaces_min_to_0 - spaces_min_to_cur - 1
            print(' ' * spaces_min_to_cur + '*' + ' ' * spaces_cur_to_0  + '|' + ' ' * spaces_0_to_max)
        else:
            spaces_0_to_cur = int(abs(cur_y) // ceil_value)
            spaces_cur_to_max = spaces_0_to_max - spaces_0_to_cur - 1
            print(' ' * spaces_min_to_0 + '|' + ' ' * spaces_0_to_cur + '*' + ' ' * spaces_cur_to_max)
        cur_x += step_value
else:
    while cur_x < x_n or abs(cur_x - x_n) < eps:
        cur_y = - (cur_x ** 2) + 9
        print("{:^6g}|".format(cur_x), end='')
        spaces_min_to_cur = int(abs(cur_y - min_y) // ceil_value)
        spaces_cur_to_max = (graph_widht - x_widht) - spaces_min_to_cur
        print(' ' * spaces_min_to_cur + '*' + ' ' * spaces_cur_to_max)
        cur_x += step_value
