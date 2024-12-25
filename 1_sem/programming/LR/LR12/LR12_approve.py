from typing import AnyStr, List, Any, Tuple

texts = [[
            'Абоба. Я говорю о Томасе Уэйде, костер костер костер тогдашнем руководителе Агентства',
            'стратегической разведки при Совете Обороны Планеты. Считаю,',
            'что его тоже нужно поблагодарить. Настала тишина. Никто ',
            'не торопился поддержать предложение Чэн Синь. Для большинства',
            'собравшихся Уэйд олицетворял все темные стороны, присущие',
            'характеру людей Общей Эры. Он был полной противоположностью',
            'этой прекрасной женщине, которую в свое время чуть не',
            'убил. Многие содрогнулись от одной только мысли о нем aбоба абоба абоба.'
        ],
        [
            'Мы никогда не встречались. Я Слушатель, передавший',
            'предупреждение на Землю два с половиной века',
            'назад. — Боже мой, и вы еще живы? — воскликнула',
            'Чжуан Янь. Мне уже недолго осталось. Меня много',
            'лет хранили в дегидрированном состоянии, но даже',
            'обезвоженное тело стареет. Тем не менее я счастлив,',
            'что собственными глазами увидел то будущее, к',
            'которому стремился.'
        ],
        [
            'Земля светилась красным, как кусок железа в кузнечном горне. Раскаленные ',
            'потоки лавы змеились по багровой равнине, словно огненная сеть расстелилась ',
            'от горизонта до горизонта. К небу поднимались бесчисленные тонкие столбы ',
            'пламени — это горели дегидратории. Сгорающие внутри них сухие оболочки ',
            'придавали огню странный голубоватый оттенок. Неподалеку Ван увидел около ',
            'десятка маленьких столбов пламени того же необычного цвета. Это горели те, ',
            'кто выскочил из пирамиды чуть раньше: папа, Галилей, Аристотель, Леонардо и ',
            'прочие. Пламя вокруг них было прозрачно-голубое, и Ван различал, как их лица ',
            'и тела коробятся в огне.'
        ]]


def main():
    matrix = []
    while True:
        matrix = mode_select(matrix)


def mode_select(matrix : list[list[str]]) -> list[list[str]]:

    n = input("""\nВыберите функцию:

        0 или пустой ввод - Завершение программы
            1\t- Вывод текста, если он установлен
            2\t- Установка текста
            3\t- Найти и удалить предложение с максимальным количеством
                 подряд идущих слов, начинающихся на заданную букву.\n> """)
    match n:
        case '0':
            exit()
        case '1':
            print_text(matrix)
        case '2':
            matrix = text_select()
        case '3':
            matrix = find_sentence(matrix)

    return matrix


def print_text(matrix: list[list[str]]) -> None:
    print()
    for line in matrix:
        print(''.join(line))


def text_select() -> list[list[str]]:
    print('Отрывки из введенных текстов:')
    for i in range(len(texts)):
        print(f'\t{i + 1} - {texts[i][:50]}')

    while True:
        n = int(input('Введите номер нужного текста\n>')) - 1
        if 0 <= n < len(texts):
            break

    matrix = text_to_matrix(texts[n])
    return matrix

def text_to_matrix(text: list[str]) -> list[list[str]]:
    matrix = []
    for i in range(len(text)):
        line = []
        for word in text[i].split():
            word = word.strip()
            if word:
                line.append(word + ' ')
        line[-1] = line[-1].strip()
        matrix.append(line)

    print('>Текст успешно установлен.')
    return matrix


def find_sentence(matrix: list[list[str]]) -> list[list[str]]:
    letter = input("Введите букву\n> ").strip().lower()[0]
    while not letter.isalpha():
        if letter == '':
            return matrix
        letter = input("Введите букву\n> ").strip().lower()[0]

    start_ind, stop_ind = (-1, -1), (-1, -1)
    cur_start, cur_stop = (0, 0), (0, 0)
    max_amount = 0
    cur_amount, sentence_amount = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].lower().startswith(letter):
                cur_amount += 1
            else:
                sentence_amount = max(cur_amount, sentence_amount)
                cur_amount = 0

            if matrix[i][j].strip().endswith('.') and matrix[i][j].count('.') == 1:
                flag = False
                if j == len(matrix[i]) - 1:
                    if i == len(matrix) - 1:
                        flag = True
                    else:
                        if matrix[i + 1][0][0].isupper():
                            flag = True
                            cur_stop = (i + 1, 0)
                else:
                    if matrix[i][j + 1][0].isupper():
                        flag = True
                        cur_stop = (i, j + 1)
                if flag:
                    sentence_amount = max(cur_amount, sentence_amount)
                    if sentence_amount > max_amount:
                        max_amount = sentence_amount
                        start_ind = cur_start
                        stop_ind = (i, j)
                    sentence_amount, cur_amount = 0, 0
                    cur_start = cur_stop


    if start_ind != (-1, -1) and stop_ind != (-1, -1):
        delete_sentence(matrix, start_ind, stop_ind)
    return matrix


def delete_sentence(matrix: list[list[str]],
                    start_ind: tuple[int, int],
                    stop_ind: tuple[int, int]) -> None:

    if stop_ind[0] != start_ind[0]:  # if sentence in many lines
        # delete all elements from j to -1 in first line
        for _ in range(len(matrix[start_ind[0]]) - 1, start_ind[1] - 1, -1):
            print(matrix[start_ind[0]].pop(start_ind[1]), end=' ')

        if stop_ind[0] - start_ind[0] > 1:
            print()
            # delete all line above first and last
            for i in range(stop_ind[0] - 1, start_ind[0], -1):
                print(*matrix.pop(i), sep=' ')

        print()
        # delete all elements from 0 to j in last line
        for _ in range(stop_ind[1], -1, -1):
            print(matrix[stop_ind[0]].pop(0), end=' ')

        print()
        # delete last if it is empty
        if not matrix[stop_ind[0]]:
            matrix.pop(stop_ind[0])

    else:
        for _ in range(stop_ind[1], start_ind[1] - 1, -1):
            print(matrix[start_ind[0]].pop(start_ind[1]), end=' ')

    # delete first if it is empty
    if not matrix[start_ind[0]]:
        matrix.pop(start_ind[0])


if __name__ == '__main__':
    main()
