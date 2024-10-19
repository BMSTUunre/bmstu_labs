"""
Лабораторная работа по программированию №7
1 семестр; сентябрь 2024 года
Коростылев Егор ИУ7-14Б 4 вариант

Задача 3:
Поиск элемента с наибольшим числом подряд идущих пробелов в списке строк по варианту.
"""


def main():
    # Блок 0: Ввод массива.
    print('Вводите строки массива по одной, ввод всего списка оканчивается пустой строкой')
    array = []
    while new_line := input('> '):
        array.append(new_line)

    # block 1:
    answer_line = ''
    max_num_of_spaces = 0

    for line in array:  # по каждой строке в списке

        num_of_spaces = 0
        current_spaces = 0

        for letter in line:  # по каждому символу в строке
            if letter == ' ':  #  если он - пробел добавляем
                current_spaces += 1

            else:  # иначе сравниваем предыдущую пробельную последовательность
                if current_spaces > num_of_spaces:
                    num_of_spaces = current_spaces
                    current_spaces = 0

        if current_spaces > num_of_spaces:  # вдруг в конце много пробелов
            num_of_spaces = current_spaces

        if num_of_spaces > max_num_of_spaces:  # если эта строка подходит - сохраняем
            answer_line = line
            max_num_of_spaces = num_of_spaces

    if max_num_of_spaces == 0:
        return 'Чет пробелов нема.'
    return answer_line


if __name__ == '__main__':
    print(main())
