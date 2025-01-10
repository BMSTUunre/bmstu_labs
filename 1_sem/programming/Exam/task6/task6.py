"""
    a = [3, 4, 2, 1, 5]
    a.sort(key=lambda x: (x % 2, x))
    print(a)
"""

"""
    Дан текстовый файл in.txt, в строках которого записаны слова через пробел. 
    Необходимо создать файл out.txt, в который записать сначала слова первой строки 
    в столбцы (первая строка нового файла - первые символы слов первой строки, 
    вторая строка - вторые символы либо пробелы и т.д.), затем ниже - блок 
    столбцов второй строки и до конца файла. Затем для каждой строки 
    получившегося файла подсчитать количество буквенных символов и создать 
    третий файл, в который переписать строки в порядке увеличения этих значений. 
    Файлы в память целиком не читать.
"""
path = '/home/unre/PycharmProjects/bmstu_labs/1_sem/programming/Exam/task6/'


def get_line(n: int):
    with open(path + 'out1.txt', 'r') as file:
        for _ in range(n + 1):
            line = file.readline()
        return line


def main():
    with open(path + 'out1.txt', 'w') as out1_file:
        
        line_char_count = []
        
        with open(path + 'in.txt', 'r') as in_file:
            line_count = 0
            while line := in_file.readline().strip():
                line = line.split()
                max_w = 0
                for w in line:
                    max_w = max(max_w, len(w))
                
                
                for i in range(max_w):
                    line_char_count.append([line_count, 0])
                    
                    for w in line:
                        if i >= len(w):
                            out1_file.write(' ')
                        else:
                            out1_file.write(w[i])
                            line_char_count[-1][1] += 1
                    out1_file.write('\n')
                
                    line_count += 1  
        
    line_char_count.sort(key=lambda x: x[1])
    
    with open(path + 'out2.txt', 'w') as out2_file:     
        for pair in line_char_count:
            out2_file.write(get_line(pair[0]))


if __name__ == '__main__':
    main()
