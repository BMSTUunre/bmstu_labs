while int(n := input()) < 0:
    print('надо положительное n')

while (k := int(input())) < 0 or k >= len(str(n)):
    print("надо положительное k И меньшее чем длина n")

# разбиваем n по цифрам
array = [int(i) for i in n]
array_for_delete = [str(i) for i in sorted(array)[:k]]

new_n = ''
for i in n:
    if i in array_for_delete:
        array_for_delete.remove(i)
    else:
        new_n += i
print(new_n)