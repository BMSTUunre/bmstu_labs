"""
Защита лабораторной работы по программированию №6
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 5:
Продублировать второй максимум в списке.
"""
from Cython.Shadow import array


def main():
    # Блок 0: Ввод массива.
    arr = []
    print('Вводите целочисленные значения элементов по одному, ввод оканчивается пустой строкой:')
    while n := input("> "):
        while not n.replace('-', '').isalnum():
            n = input("Введите адекватное целочисленное значение\n> ")
        arr.append(int(n))

    # 1: Определение индексов таких элементов, их замена и вывод нового массива.
    if len(arr) > 1:
        first_max, second_max = arr[0], 0
        first_max_index, second_max_index = 0, None

        for i in range(1, len(arr)):
            if arr[i] > first_max:
                second_max_index = first_max_index
                second_max = first_max
                first_max_index = i
                first_max = arr[i]

            elif arr[i] > second_max or second_max_index is None:
                second_max_index = i
                second_max = arr[i]

        arr.append(0)

        for index in range(len(arr) - 1, second_max_index, -1):
            arr[index] = arr[index - 1]

        return arr

    return 'МАЛО ЭЛЕМЕНТОВ'


if __name__ == '__main__':
    print(main())
