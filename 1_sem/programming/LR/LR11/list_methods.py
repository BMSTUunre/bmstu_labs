from random import randint


def random_list(n: int, start: int =-100, stop: int =100) -> list[int]:
    arr = [randint(start, stop) for _ in range(n)]
    return arr


def sorted_list(n: int) -> list[int]:
    arr = [i for i in range(n)]
    return arr


def reversed_list(n: int) -> list[int]:
    arr = [i for i in range(n - 1, -1, -1)]
    return arr


def heapify(arr: list,
            n: int,
            i: int,
            k: int) -> int:

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        k += 1
        return heapify(arr, n, largest, k)
    return k


def heap_sort(arr: list) -> tuple[list, int]:
    n = len(arr)
    k = 0
    for i in range(n // 2, -1, -1):
        k = heapify(arr, n, i, k)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        k = heapify(arr, i, 0, k)

    return arr, k
