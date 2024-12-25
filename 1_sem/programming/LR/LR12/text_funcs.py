from re import fullmatch
from main import text_select

re_sings = ('["\'#№$' + r'\*\(\[\{]?', r'[\.!:;,\?\)\]\}' + '\'"]?')


def funcs_list(task: str, matrix: list, aligned='3-1') -> None | tuple[list[list[str]], str]:
    if not matrix:
        print('Текст не установлен или пустой. \n автоматический выбор пункта 2:')
        matrix, aligned = text_select()
    elif task == "1":
        print_text(matrix)
    elif task == "2":
        matrix, aligned = text_select()
    elif task in ('3-1', '3-2', '3-3'):
        matrix, aligned = choose_align(matrix, task)
    elif task == "4":
        matrix, aligned = delete_word(matrix, aligned)
    elif task == "5":
        matrix, aligned = replace_word(matrix, aligned)
    elif task == "6":
        matrix, aligned = eval_matrix(matrix, aligned)
    elif task == "7":
        matrix, aligned = find_sentence(matrix, aligned)
    else:
        print('\n......Я вас не понимаю.........\n')
    return matrix, aligned


def print_text(matrix: list[list[str]]) -> None:
    print()
    for line in matrix:
        print(''.join(line))


def choose_align(matrix: list[list[str]], task: str) -> tuple[list[list[str]], str]:
    if task == "3-1":
        return left_align(matrix), "3-1"
    if task == "3-2":
        return right_align(matrix), "3-2"
    return justified_align(matrix), "3-3"


def left_align(matrix: list[list[str]]) -> list[list[str]]:
    for line in matrix:
        for j in range(len(line)):
            line[j] = line[j].strip() + ' '
        line[-1] = line[-1].strip()
    print('>Текст успешно выравнен.')
    return matrix


def right_align(matrix: list[list[str]]) -> list[list[str]]:
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
    return matrix


def justified_align(matrix: list[list[str]]) -> list[list[str]]:
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
        if len(line) > 1:
            spaces = (max_len - int(line_len)) // (len(line) - 1)
            last = (max_len - int(line_len)) % (len(line) - 1)
            if spaces or last:
                for j in range(len(line)):
                    line[j] += ' ' * spaces
                    if last:
                        line[j] += ' '
                        last -= 1
    print('>Текст успешно выравнен.')
    return matrix


def delete_word(matrix: list[list[str]], aligned: str) -> tuple[list[list[str]], str]:
    word = input('Введите слово для удаления\n> ')
    for line in matrix:
        for j in range(len(line) - 1, -1, -1):
            if fullmatch(re_sings[0] + word.lower() + re_sings[1], line[j].strip().lower()):
                line[j] = line[j].strip().lower().replace(word.lower(), '')
                if not line[j]:
                    line.pop(j)
    matrix, _ = choose_align(matrix, aligned)
    print(f'#Слово {word} успешно удалено.')
    return matrix, aligned


def replace_word(matrix: list[list[str]], aligned: str) -> tuple[list[list[str]], str]:
    word_find = input('Введите слово для удаления\n> ')
    word_replace = input('Введите слово для замены удаленного\n> ')
    for line in matrix:
        for j in range(len(line) - 1, -1, -1):
            if fullmatch(re_sings[0] + word_find.lower() + re_sings[1], line[j].strip().lower()):
                line[j] = line[j].strip().lower().replace(word_find.lower(), word_replace)
                if not line[j]:
                    line.pop(j)
    matrix, _ = choose_align(matrix, aligned)
    print(f'#Слово {word_find} успешно заменено на {word_replace}.')
    return matrix, aligned


def eval_matrix(matrix: list[list[str]], aligned: str) -> tuple:
    print(matrix)
    operators = '+-*/%'
    for line_ind in range(len(matrix)):
        rpn = []
        rpn_n = 0
        start_ind = 0
        for word_index in range(len(matrix[line_ind])):
            if matrix[line_ind][word_index].strip().isalnum():
                if not rpn:
                    start_ind = word_index
                rpn.insert(rpn_n - 1, int(matrix[line_ind][word_index].strip()))
                rpn_n += 1
            elif matrix[line_ind][word_index].strip() in operators and rpn:
                rpn_n += 1
                rpn.append(matrix[line_ind][word_index].strip())

            else:
                if rpn:
                    print(rpn)
                    res = eval_rpn(rpn)
                    rpn = []
                    print(res)
                    matrix[line_ind] = matrix[line_ind][0: start_ind] + [str(res)] + matrix[line_ind][word_index:]
        if rpn:
            print(rpn)
            res = eval_rpn(rpn)
            print(res)
            matrix[line_ind] = matrix[line_ind][0: start_ind] + [str(res)]

    matrix, _ = choose_align(matrix, aligned)
    return matrix, aligned


def eval_rpn(rpn: list[int | str]) -> int | float:
    cur = rpn.pop(0)
    priority =  "*/%"
    while rpn:
        print(rpn)
        next_val = rpn.pop(0)
        action = rpn.pop(0)
        if rpn:
            next_action = rpn[1]
            while rpn and action not in priority and next_action in priority:
                if next_action in '/%':
                    if rpn[0] == 0:
                        print(':: found division by zero ::')
                        return 0
                    if next_action == '/':
                        next_val = next_val / rpn.pop(0)
                    else:
                        next_val = next_val % rpn.pop(0)
                else:
                    next_val = next_val * rpn.pop(0)
                rpn.pop(0)
                if rpn:
                    next_action = rpn[1]
        if action == "+":
            cur += next_val
        elif action == "-":
            cur -= next_val
        elif action == "*":
            cur *= next_val
        elif action == "/":
            if next_val == 0:
                print(':: found division by zero ::')
                return 0
            cur /= next_val
        elif action == "%":
            cur %= next_val
    return cur


def find_sentence(matrix: list[list[str]], aligned: str) -> tuple[list[list[str]], str]:
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
        choose_align(matrix, aligned)
    return matrix, aligned


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


if __name__ == "__main__":
    print(eval_rpn([1, 2,'-', 1, '+', 1, "+", 241, '+', 2, "*", 1, '-', 100, '*']))
