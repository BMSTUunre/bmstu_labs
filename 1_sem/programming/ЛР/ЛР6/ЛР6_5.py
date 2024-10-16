"""
Лабораторная работа по программированию №6
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 5:
Поменять местами первый нулевой и минимальный отрицательный элемент.
"""


def main():
    # Блок 0: Ввод массива и дополнительных значений.
    arr = []
    print('Вводите целочисленные значения элементов по одному, ввод оканчивается пустой строкой:')
    while n := input("> "):
        while not n.replace('-', '').isalnum():
            n = input("Введите адекватное целочисленное значение\n> ")
        arr.append(int(n))

    # 1: Определение индексов таких элементов, их замена и вывод нового массива.
    first_0_index = False
    min_neg_index = False
    min_neg_value = False

    for index, x in enumerate(arr):
        if x == 0 and first_0_index is False:
            first_0_index = index
        elif (min_neg_index == False and x < 0) or x < min_neg_value:
            min_neg_index = index
            min_neg_value = x

    if (min_neg_index is not False) and (first_0_index is not False):
        arr[first_0_index] = arr[min_neg_index]
        arr[min_neg_index] = 0
        print(arr)
    else:
        print("Такие элементы не найдены ;(")


if __name__ == '__main__':
    main()