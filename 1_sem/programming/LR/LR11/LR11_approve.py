def find_greather_pair(a: tuple[str, str], b: tuple[str, str]) -> bool:
    """
        returns True if a > b
        else False
        """

    a_aplha = ["R", "G", "B", "Y", "W", "P"]

    s1, s2, c1, c2 = a[0], b[0], a[1], b[1]

    for i in range(min(len(s1), len(s2))):
        if a_aplha.index(s1[i]) > a_aplha.index(s2[i]):
            return True

        if a_aplha.index(s1[i]) < a_aplha.index(s2[i]):
            return False

    if len(s1) > len(s2) or (len(s1) == len(s2) and c1 > c2):
        return True
    return False



def bubble_sort(arr: list[tuple[str, str]]) -> list[tuple[str, str]]:
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if find_greather_pair(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print("Вводите пары элементов списка построчно через пробел, ввод заканчивается пустой строкой")
arr = []
new_line = input(">")
while new_line:
    line = new_line.split()
    while len(line) != 2:
        print("Неверное кол-во элементов в паре, повторите ввод")
        line = input('>').split()
    arr.append(tuple(line))

    new_line = input(">")


arr = bubble_sort(arr)

print(*arr, sep='\n')

'''
BYR a
BY b
RPP b
RPP a
'''