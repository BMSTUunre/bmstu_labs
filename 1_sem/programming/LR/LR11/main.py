"""
Лабораторная работа по программированию №11
1 семестр; ноябрь 2024 года
Коростылев Егор ИУ7-14Б

Задача:
    Написать программу для демонстрации работы метода сортировки (по варианту)
    на примере массива целых чисел.

    Программа должна состоять из двух частей (этапов работы) и
    выполнять два действия последовательно:
        1. сначала отсортировать заданный пользователем массив для
            доказательства корректности работы алгоритма;

        2. затем составить таблицу замеров времени сортировки списков трёх различных (заданных пользователем)
            размерностей и количества перестановок в каждом из них.

    В части 2 для каждой размерности списка необходимо исследовать:
        ● случайный список,
        ● отсортированный список,
        ● список, отсортированный в обратном порядке.

"""

from datetime import datetime
from list_methods import *
from table import print_table


def input_int(text: str, allow_negative=True, allow_zero=True) -> int:
    x = input(text).strip()
    while not ((allow_negative and x.lstrip('-').isalnum() or x.isalnum()) and (allow_zero or int(x) > 0)):
        print('Значение должно быть целочисленным.')
        x = input(text).strip()
    return int(x)



print('Вводите элементы списка A по одному, ввод всего списка оканчивается пустой строкой')
a_list = []
while new_line := input('> ').strip():
    while not new_line.lstrip('-').isalnum():
        print('чет значение не похоже на адекватное введи новое')
        new_line = input('> ')
    a_list.append(int(new_line))

arr, k = heap_sort(a_list)

print(arr)
start = datetime.now()
print(f'Сортирован за: {datetime.now() - start}')
print(f'Выполнено перестановок: {k}\n')


n1 = input_int("Введите кол-во элементов в первом случае\n>")
n2 = input_int("Введите кол-во элементов во втором случае\n>")
n3 = input_int("Введите кол-во элементов в третьем случае\n>")

sorted_res = ["Упорядоченный список"]
reversed_res = ["Упорядоченный\nв обратном порядке"]
random_res = ["Случайный список"]

ns = [n1, n2, n3]

for n in ns:
    def_arr = sorted_list(n)
    start = datetime.now()
    _, k = heap_sort(def_arr)
    delta = datetime.now() - start
    sorted_res.append(delta)
    sorted_res.append(k)

    def_arr = reversed_list(n)
    start = datetime.now()
    _, k = heap_sort(def_arr)
    delta = datetime.now() - start
    reversed_res.append(delta)
    reversed_res.append(k)

    def_arr = random_list(n)
    start = datetime.now()
    _, k = heap_sort(def_arr)
    delta = datetime.now() - start
    random_res.append(delta)
    random_res.append(k)


print_table(sorted_res, random_res, reversed_res)
