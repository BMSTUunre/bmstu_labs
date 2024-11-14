'''
1 - Тип данных — это классификация данных, определяющая какими значениями могут быть переменные и какие операции могут
быть выполнены с этими значениями.

2 - В Python типы данных можно классифицировать на 2 категории:
    Неизменяемые (int, float, bool, str)
    Составные (list, tuple, set, dict)

3 - string (итерируемые)
'''

array = []
n = 0
line = input('Вводите элементы массива по одному, ввод оканчивается пустой строкой\n >')
while line:
    x = line.strip()
    while not x.lstrip('-').isalnum():
        x = input('ошибка, повторите еще раз\n >').strip()

    array.append(int(x))
    n += 1
    line = input('Следующий элемент\n >')

additional_array = []
for x in array:
    for y in additional_array:
        if x == y:
            break
    else:
        additional_array.append(x)

array = additional_array.copy()

min_i_pos, max_i_neg = -1, -1
min_pos, max_neg = 0, 0

for x in range(len(array)):
    if 0 < array[x] and (abs(array[x]) % 2 == 0) and ((min_i_pos == -1) or (array[x] < min_pos)):
        min_pos, min_i_pos = array[x], x

    elif (0 > array[x]) and (abs(array[x]) % 2) and ((max_i_neg == -1) or (array[x] > max_neg)):
        max_neg, max_i_neg = array[x], x

array[min_i_pos], array[max_i_neg] = array[max_i_neg], array[min_i_pos]