'''
В файле in.txt записаны строки, длина которых не превышает 100 символов.
Диагональю из символов в рамках этой задачи считать последовательность символов, 
расположенных во всех строках файла так, что символ в следующей строке находится 
на одну позицию правее символа в предыдущей строке. Требуется переписать в файл 
out.txt содержимое исходного файла так, чтобы туда не попали диагонали из 
символов %, если они есть. Также к каждой строке через пробел нужно добавить 
число слов-палиндромов длиной больше одного, которые в ней присутствуют. 
Считывать файл в память целиком нельзя. 
'''

# решение взято у https://t.me/Krionee 

def count_palindromes_in_string(s: str) -> int:
    co = 0
    for i in s.split():
        current = i.strip("%")
        if current == current[::-1] and len(current) > 1:
            co += 1
    return co


with open("exam_task1/in.txt", "r", encoding="utf-8") as file, open("exam_task1/out.txt", "w", encoding="utf-8") as o:
    
    first_string = file.readline()
    palindromes = [count_palindromes_in_string(first_string)]
    chars_to_delete = []
    for i in range(len(first_string)):
        if first_string[i] == "%":
            chars_to_delete.append(i)
                    
    number_of_next_line = 1
    
    next_line = file.readline()
    
    while next_line:
        palindromes.append(count_palindromes_in_string(next_line))
        for j in chars_to_delete:
            if next_line[j+number_of_next_line] == "%":
                continue
            else:
                chars_to_delete.remove(j)
        number_of_next_line +=1 
        next_line = file.readline()
        
    file.seek(0)
    n = 0
    string = file.readline()
    while string:
        char_list = list(string)
        for i in chars_to_delete[::-1]:
            char_list.pop(i + n)
        
        res = "".join(char_list).strip("\n") + " " + str(palindromes[n]) + "\n"
        o.write(res)
        n += 1
        string = file.readline()
