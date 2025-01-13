'''
В текстовом файле in.txt содержатся теги XML документа, причем нет самозакрывающихся тегов (каждому открывающему соответствует закрывающий). Необходимо:
    1. Определить кол-во различных тегов.
    2. Определить макс. вложенность для каждого тега.
    
    В ответе указать все теги в обратном алфавитном порядке, их кол-во и их макс. вложенность через пробел
    
    Пример:
        in.txt:
            <a></a>
            <a><b></b></a>
            <c><a><a><b></b></a>
            </a></c>

        out.txt:
            c 1 1
            b 2 4
            a 4 3         
'''
from collections import defaultdict

path = '/home/unre/PycharmProjects/bmstu_labs/1_sem/programming/Exam/real_task_13.01.24/'


def parse_tags(text):
    stack = []
    tag_counts = defaultdict(int)
    max_depths = defaultdict(int)
    
    i = 0
    while i < len(text):
        if text[i] == '<':
            closing_tag = False
            j = i + 1
            while j < len(text) and text[j] not in '>/':
                j += 1
            
            if j < len(text) and text[j] == '/':
                closing_tag = True
                j += 1
            
            tag_name_end = j
            while j < len(text) and text[j] != '>':
                j += 1
            
            tag_name = text[i+1:tag_name_end]
            
            if not closing_tag:
                stack.append(tag_name)
                depth = len(stack)
                tag_counts[tag_name] += 1
                max_depths[tag_name] = max(max_depths[tag_name], depth)
            else:
                stack.pop()
            
            i = j + 1
        else:
            i += 1
    
    return tag_counts, max_depths

def main():
    with open(path + 'in.txt', 'r') as file:
        text = file.read()

    tag_counts, max_depths = parse_tags(text)

    # Сортировка тегов в обратном алфавитном порядке
    sorted_tags = sorted(tag_counts.keys(), reverse=True)

    with open(path +'out.txt', 'w') as file:
        for tag in sorted_tags:
            file.write(f"{tag} {tag_counts[tag]} {max_depths[tag]}\n")

if __name__ == "__main__":
    main()
