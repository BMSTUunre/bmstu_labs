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
        text_select()
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


def eval_matrix(matrix: list[list[int]]):
    raise NotImplemented
