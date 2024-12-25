from struct import pack, unpack
from sys import getsizeof


def func(x):
    return x ** 2


def father_func(x):
    return (x ** 3) / 3


def real_integral(x0, xn):
    return father_func(xn) - father_func(x0)


def read_bin():
    with open("in.bin", 'rb') as file:
        i = 0
        while True:
            file.seek(i)
            struc = file.read(8)
            if struc:
                structure = unpack('hf', struc)
                i += 8
                print(structure)
            else:
                break


def make_bin():
    with open("in.bin", 'wb') as file:
        for a in range(10, 10000, 500):
            b = a * 5 / 101
            print(a, b)
            structure = pack('hf', a, b / 1000)
            file.write(structure)

    read_bin()


def calc_integral(x0, xa, n) -> float:
    step = (xa - x0) / n
    cur_x = x0
    f = 0
    for i in range(n):
        cur_x += step / 2
        y_mid = func(cur_x)
        f += y_mid
        cur_x += step / 2

    f = f * step
    return f


def iter_calc(a, b) -> tuple[int, float]:
    real_int = real_integral(0, a)
    print('real int', real_int)
    cur_int = 0
    n = 1
    while abs(real_int - cur_int) > b:
        cur_int = calc_integral(0, a, n)
        print(cur_int, n)
        n *= 2
    return n, cur_int


def main():
    make_bin()
    print('\nbin done\n')
    read_bin()
    i = 0
    while True:
        with open("in.bin", 'rb') as file:
            print('-----------------')
            file.seek(i)
            struc = file.read(8)
        if struc:
            a, b = unpack('hf', struc)
            print('a - b', a, b)
            n, f = iter_calc(a, b)
            print('n - f', n, f)
            new_structure = pack('hf', n, f)
            with open("in.bin", 'wb') as file:
                file.seek(i)
                file.write(new_structure)
            i += 8
        else:
            break
    print('\nbin integraded\n')
    read_bin()



if __name__ == '__main__':
    main()
