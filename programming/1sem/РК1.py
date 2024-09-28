def task1():
    x = float(input("Введите x: "))
    y = 0
    z = -1
    for i in range(2, 22, 2):
        y += z * (x ** i) / i * (x + 1 + i)
        z *= -1
    print('Значение y:', y)


def task2():
    odd = 0
    even = 0
    n = int(input("Введите число: "))
    while n > 0:
        if (n % 10) % 2 == 0:
            odd += 1
        else:
            even += 1
        n //= 10
        n = int(input("Введите число: "))

    if odd > even:
        print("Четных больше")
    elif odd == even:
        print("Четных и нечетных одинаково")
    else:
        print("Нечетных больше")


def task3():
    max1 = 0
    max1_ind = 0
    max2 = 0
    max2_ind = 1
    n = 0
    x = int(input("Введите первый член последовательности"))
    while x != 0:
        if x >= max1:
            max2 = max1
            max2_ind = max1_ind
            max1 = x
            max1_ind = n
        elif x >= max2:
            max2 = x
            max2_ind = n
        n += 1
    print("Индекс второго наибольший элемент пос-ности:", max2_ind)
