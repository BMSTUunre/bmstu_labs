"""
Лабораторная работа по программированию №7
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б 2 вариант

Задача 2:
После каждого четного элемента целочисленного списка добавить его удвоенное значение,
без использования вложенных циклов.
Без insert append срезов.
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

    num_of_evens = 0  # считаем кол-во четных элементов в списке
    for num in array:
        if abs(num) % 2 == 0:
            num_of_evens += 1

    array += [0] * num_of_evens  # расширяем список на это самое количество

    index = len(array) - 1 - num_of_evens  # идем по нижней границе изначального массива
    while index >= 0:
        x = array[index]
        if abs(x) % 2 == 0:  # если очередной элемент изначального массива четный
            array[index + num_of_evens] = x * 2  # добавляем его удвоенное значение в свободную клетку сзади
            num_of_evens -= 1  # уменьшаем кол-во будущих четных элементов
        array[index + num_of_evens] = x  # дублируем элемент не его новое место (независимо от его четности)
        index -= 1  # переходим к следующему

    return array


if __name__ == '__main__':
    print(main())