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


# def merge_in_out() -> tuple[int, int]:
#     len_in_file, max_diag_start = 0, 100    
    
#     with open('in.txt', 'r') as in_file:
#         with open('out.txt', 'w') as out_file:
#             while (line := in_file.readline()).strip():
#                 len_in_file += 1
#                 max_diag_start = min(max_diag_start, len(line) - len_in_file)
#                 out_file.write(line)
    
#     return len_in_file, max_diag_start


# def delete_diagonal(start_ind: int, len_file: int, file) -> None:
        
        


# def main() -> None:
#     len_in_file, max_diag_start = merge_in_out()
    
#     with open('out.txt', 'r+') as out_file:
#         if max_diag_start >= 0:
            
#             for symb_ind in range(max_diag_start, -1, -1): # first line parser, reversed for kill conflicts of deleted diags
#                 out_file.seek(symb_ind, 0)
#                 if out_file.read(1) == '%':
#                     out_file.readline() # skip first line
#                     for line_ind in range(1, len_in_file):
#                         out_file.read(symb_ind + line_ind)
#                         if out_file.read(1) != '%':
#                             break
#                         out_file.readline() # skip line
#                     else:
#                         delete_diagonal(symb_ind, len_in_file, out_file)
                        

# if __name__ == '__main__':
#     main()


"""
идея не плохая но реализация слишком запарная, надо было думать и перезаписывать только нужные диагонали и сразу дописывать кол-во палиндромов

"""