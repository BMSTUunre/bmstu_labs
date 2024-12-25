'''
вариант 1
'''

print('Вводите матрицу A построчно, пробелами разделяя элементы\nВвод заканчивается пустой строкой\n')

a_matrix = []
while line := input('> ').strip():
    a_matrix.append([int(x) for x in line.split()])

print('Вводите матрицу B построчно, пробелами разделяя элементы\nВвод заканчивается пустой строкой\n')

b_matrix = []
while line := input('> ').strip():
    b_matrix.append([int(x) for x in line.split()])

n = len(b_matrix)
for i in range(n - 1):
    for j in range(n - i - 1):
        b_matrix[n - i - 1][n - 1 - j], b_matrix[j][i] = b_matrix[j][i], b_matrix[n - i - 1][n - 1 - j]  # Отражаем по побочной диагонали


print(b_matrix)

for line in b_matrix:
    a_matrix.append(line)

dick = dict()

for line in a_matrix:
    if str(sum(line)) in dick.keys():

        dick[str(sum(line))] += 1
    else:
        dick[str(sum(line))] = 1

answer_i, answer = -1, 0

for line in range(len(a_matrix)):
    if dick[str(sum(a_matrix[line]))] > answer or answer_i == -1:
        answer_i = line
        answer = dick[str(sum(a_matrix[line]))]

print(answer_i)

for line in a_matrix:
    print('[', end='')
    for x in line:
        print(str(x).rjust(6), end=', ')
    print('\b\b]')
