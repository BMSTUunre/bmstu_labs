from itertools import permutations, product


def otschet():
    n, t = (int(i) for i in input().split())
    arr = [int(i) for i in input().split()]
    operations = list(product(['+', "-", "*", "//"], repeat=n - 1))

    for comb_n in permutations(arr):
        for comb_o in operations:
            f = True
            if '//' in comb_o:
                for i in range(n - 1):
                    if comb_o[i] == '//' and comb_n[i + 1] == 0:
                        f = False
                        break
            if f:
                string = f'{comb_n[0]}'
                for i in range(n - 1):
                    string += f' {comb_o[i]} {comb_n[i + 1]}'

                res = eval(string)
                if res == t:
                    return "YES"

    return 'NO'
print(otschet())