x = float(input('x: '))
eps = float(input("Точносить: "))

n = 0
s = 0
t = x

while abs(t) > eps:
    s += 1
    n += 1
    t *= -(x ** 2) / (2 * n) / (2 * n + 1)

print("S = {0}.\nВычислено за {1} итераций.".format(s, n))
