"""
Лабораторная работа по программированию №6
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача 1a:
Добавить элемент в заданное место списка (по индексу) с использованием
любых средств Python.
"""


def main():
    # Блок 0: Ввод массива и дополнительных значений
    arr = []
    print('Вводите целочисленные значения элементов по одному, ввод оканчивается пустой строкой:')
    while n := input("> "):
        while not n.replace('-', '').isalnum():
            n = input("Введите адекватное целочисленное значение\n> ")
        arr.append(int(n))

    x_i = int(input('Введите значение, которое необходимо вставить\n> '))
    ind = int(input('Введите индекс, куда необходимо его вставить\n> '))

    while 0 > ind or ind > len(arr):
        ind = int(input("Введите адекватное целочисленное значение\n> "))

    # Блок 1: Вставка элемента и вывод нового массива
    arr.insert(ind, x_i)

    print(arr)


if __name__ == '__main__':
    main()
