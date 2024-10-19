"""
Лабораторная работа по программированию №7
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б 3 вариант

Задача 1:
Удалить все нечётные элементы целочисленного списка за один цикл.
Без del pop remove срезов.
"""

def main():
    # Блок 0: Ввод массива.
    print('Вводите элементы массива по одному, ввод всего списка оканчивается пустой строкой')
    array = []
    while new_line := input('> '):
        while not new_line.lstrip('-').isalnum():
            print('чет значение не похоже на целочисленное введи новое')
            new_line = input('> ')
        array.append(int(new_line))

    # Блок 1: сама магия
    current_index = 0
    for num in array:
        if abs(num) % 2 == 0:
            array[current_index] = num
            current_index += 1

    # Блок 2: Вывод списка
    result = '['
    for index in range(current_index):
        result += str(array[index]) + ', '
    result += '\b\b]'

    return result

if __name__ == '__main__':
    print(main())
