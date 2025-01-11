'''
    Даны 2 фaйла:
        in1.txt, в котором записаны номера строк в рандомном порядке без повторений, от 1 до n
        in2.txt, в котором записаны n пар цифр, каждая на новой строке, пары идут через пробел
        
    Записать в файл out.txt
        суммы цифр строк, в том порядке, в котором их номера записаны в файле in1.txt, записывать только суммы, образующие полные квадраты (квадрат целого числа)
    
    Пример
    in1.txt
        3
        1
        4
        2
        
    in2.txt
        2 2
        2 5
        10 4
        3 6
        
    out.txt
        4
        9
 '''
 
path = 'bmstu_labs/1_sem/programming/Exam/task5/'


def get_line(n: int):
    with open(path + 'in2.txt', 'r') as f:
        for _ in range(n):
            line = f.readline().strip()
            if not line:
                return ''
        return line


def main():
    with open(path + 'out.txt', 'w') as out:
        with open(path + 'in1.txt', 'r') as in1:
            while n := in1.readline().strip():
                line = [int(i) for i in get_line(int(n)).split()]
                pair_sum = sum(line)
                if not (pair_sum ** 0.5) % 1:
                    out.write(str(pair_sum) + '\n')


if __name__ == "__main__":
    main()
