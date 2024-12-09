from re import fullmatch
from main import text_select

re_sings = ('["\'#№$' + r'\*\(\[\{]?', r'[\.!:;,\?\)\]\}' + '\'"]?')


def funcs_list(task: str, matrix: list) -> None | list[list[str]]:
    if not matrix:
        print('Текст не установлен или пустой. \n автоматический выбор пункта 2:')
        return text_select()
    elif task == "1":
        print_text(matrix)
    elif task == "2":
        matrix = text_select()
    elif task == "3-1":
        left_align(matrix)
    elif task == "3-2":
        right_align(matrix)
    elif task == "3-3":
        justified_align(matrix)
    elif task == "4":
        delete_word(matrix)
    elif task == "5":
        replace_word(matrix)
    elif task == "6":
        eval_matrix(matrix)
    elif task == "7":
        find_sentence(matrix)
    else:
        '\n......Я вас не понимаю.........\n'
    return matrix


def print_text(matrix: list[list[str]]) -> None:
    print()
    for line in matrix:
        print(''.join(line))


def left_align(matrix: list[list[str]]) -> None:
    for line in matrix:
        for j in range(len(line)):
            line[j] = line[j].strip() + ' '
        line[-1] = line[-1].strip()
    print('>Текст успешно выравнен.')


def right_align(matrix: list[list[str]]) -> None:
    left_align(matrix)
    max_len = 0
    for line in matrix:
        cur_len = 0
        for word in line:
            cur_len += len(word)
        line.append(str(cur_len)) # мы потом его удаляем
        max_len = max(max_len, cur_len)

    for line in matrix:
        line[0] = ' ' * (max_len - int(line.pop())) + line[0]
    print('>Текст успешно выравнен.')


def justified_align(matrix: list[list[str]]) -> None:
    left_align(matrix)
    max_len = 0
    for line in matrix:
        cur_len = 0
        for word in line:
            cur_len += len(word)
        line.append(str(cur_len))  # мы потом его удаляем
        max_len = max(max_len, cur_len)

    for line in matrix:
        line_len = line.pop()
        spaces = (max_len - int(line_len)) // (len(line) - 1)
        last = (max_len - int(line_len)) % (len(line) - 1)
        if spaces or last:
            for j in range(len(line) - 1):
                line[j] += ' ' * spaces
            if last:
                line[-2] += ' ' * last
    print('>Текст успешно выравнен.')


def delete_word(matrix: list[list[str]]) -> None:
    word = input('Введите слово для удаления\n> ')
    for line in matrix:
        for j in range(len(line) - 1, -1, -1):
            if fullmatch(re_sings[0] + word.lower() + re_sings[1], line[j].strip().lower()):
                line[j] = line[j].strip().lower().replace(word.lower(), '')
                if not line[j]:
                    line.pop(j)
    left_align(matrix)
    print(f'#Слово {word} успешно удалено.')


def replace_word(matrix: list[list[str]]) -> None:
    word_find = input('Введите слово для удаления\n> ')
    word_replace = input('Введите слово для замены удаленного\n> ')
    for line in matrix:
        for j in range(len(line) - 1, -1, -1):
            if fullmatch(re_sings[0] + word_find.lower() + re_sings[1], line[j].strip().lower()):
                line[j] = line[j].strip().lower().replace(word_find.lower(), word_replace)
                if not line[j]:
                    line.pop(j)
    left_align(matrix)
    print(f'#Слово {word_find} успешно заменено на {word_replace}.')


def eval_matrix(matrix: list[list[str]]):
    rpn = []
    for line in matrix:
        for word in line:
            for char in word:





def eval_rpn(rpn: list[int | str]) -> int | float:
    cur = rpn.pop(0)
    while rpn:
        next = rpn.pop(0)
        action = rpn.pop(0)
        if action == "+":
            cur += next
        elif action == "-":
            cur -= next
        elif action == "*":
            cur *= next
        elif action == "/":
            if next == 0:
                print(':: found division by zero ::')
                return 0
            cur /= next
        elif action == "%":
            cur %= next
    return cur

def find_sentence(matrix: list[list[str]]) -> None:
    left_align(matrix)
    letter = input("Введите букву\n> ").strip().lower()[0]
    if not letter.isalpha():
        letter = input("Введите букву\n> ").strip().lower()[0]

    start_ind, stop_ind = (-1, -1), (-1, -1)
    cur_start, cur_stop = (0, 0), (0, 0)
    max_amount = 0
    cur_amount = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].lower().startswith(letter):
                cur_amount += 1
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
                    if cur_amount > max_amount:
                        max_amount = cur_amount
                        start_ind = cur_start
                        stop_ind = (i, j)
                    cur_amount = 0
                    cur_start = cur_stop

    if start_ind != (-1, -1) and stop_ind != (-1, -1):
        delete_sentence(matrix, start_ind, stop_ind)


def delete_sentence(matrix: list[list[str]],
                    start_ind: tuple[int, int],
                    stop_ind: tuple[int, int]) -> None:

    if stop_ind[0] != start_ind[0]: # if sentence in many lines
        print(start_ind, stop_ind)
        # delete all elements from j to -1 in first line
        for j in range(len(matrix[start_ind[0]]) - 1, start_ind[1] - 1, -1):
            matrix[start_ind[0]].pop(j)

        # delete all elements from 0 to j in last line
        for j in range(stop_ind[1], -1, -1):
            matrix[stop_ind[0]].pop(j)

        # delete last if it is empty
        if not matrix[stop_ind[0]]:
            matrix.pop(stop_ind[0])

        # delete all line above first and last
        for i in range(stop_ind[0] - 1, start_ind[0], -1):
            matrix.pop(i)

    else:
        for j in range(stop_ind[1], start_ind[1] - 1, -1):
            matrix[start_ind[0]].pop(j)

    # delete first if it is empty
    if not matrix[start_ind[0]]:
       matrix.pop(start_ind[0])
