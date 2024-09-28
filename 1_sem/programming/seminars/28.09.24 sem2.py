def polygon_4_side():
    a = int(input('угол - '))
    x = int(input('a - '))
    y = int(input('b - '))

    print(int(a == 90) * 10 + int(x == y))
    '''
    00 - паралеллограм
    01 - ромб
    10 - прямоуг
    11 - квадрат
    '''


def sort_3():
    a, b, c = int(input()), int(input()), int(input())
    if a > b:
        if a > c:
            if b > c:
                m = (a, b, c)
            else:
                m = (a, c, b)
        else:
            m = (c, a, b)
    elif b > c:

