"""
Теория
1 Функция высшего порядка - функция, принимающая или возвращающая другие функции.
2 Позиционные параметры - значения которые передаются в функцию в том порядке, в котором они указаны.
"""

def main():
    with open("out.txt", 'w+') as out_file:
        with open("in.txt", 'r+') as in_file:
            sentence = ''
            for line in in_file.readlines():
                if line.find('.') != -1:
                    out_file.write(sentence + line[:line.find('.')] + '\n')
                    sentence = ''
                else:
                    sentence += line[:-1]


if __name__ == '__main__':
    main()