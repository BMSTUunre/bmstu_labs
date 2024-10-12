def igra_s_massivom():
    arr = list(int(i) for i in input().split())
    sum_pos = 0
    n_pos = 0
    prod_pos = 0
    for i in arr:
        if i > 0:
            if prod_pos == 0:
                prod_pos = i
            else:
                prod_pos *= i
            n_pos += 1
            sum_pos += 1
    print(f'n - {n_pos}\ns - {sum_pos}\n mul - {prod_pos}')


def algoritmic_insert(arr, index, item):
    if arr:
        return
    return [item]

def delete_negative(arr):
    pos_i = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[pos_i] = arr[i]
            pos_i += 1
    print(arr[:pos_i])


def add_double_after_odd(arr):
    odds = 0
    old_n = len(arr)
    for i in arr:
        if i % 2:
            odds += 1

    for _ in range(odds):
        arr.append(0)

    last_i = -1
    for i in range(old_n - 1, -1, -1):
        if abs(arr[i]) % 2:
            arr[last_i] = 2 * arr[i]
            last_i -= 1
        arr[last_i] = arr[i]
        last_i -= 1
    print(arr)

def merge_2_sorted_arrays(arr1, arr2):
    len_1 = len(arr1)
    len_2 = len(arr2)

    i1 = 0
    i2 = 0
    arr3 = [0] * (len_1 + len_2)
    while (i1 + i2) < (len_2 + len_1):
        if i2 == len_2 or arr1[i1] < arr2[i2]:
            arr3[i1 + i2] = arr1[i1]
            i1 += 1
        else:
            arr3[i1 + i2] = arr2[i2]
            i2 += 1
    print(arr3)



if __name__ == "__main__":
    # arr = [int(i) for i in input('arr - \n').split()]
    # add_double_after_odd(arr)

    arr1 = [int(i) for i in input('arr - \n').split()]
    arr2 = [int(i) for i in input('arr - \n').split()]
    merge_2_sorted_arrays(arr1, arr2)