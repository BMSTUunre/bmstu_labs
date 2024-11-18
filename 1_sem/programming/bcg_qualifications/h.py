"done"
def find(arr: list, res, last, k, step=None):
    if k:
        if step:
            for el in arr:
                if abs(last - el) == step:
                    arr1 = arr.copy()
                    arr1.remove(el)
                    if find(arr1, res - el, el, k - 1, abs(last - el)):
                        return True
        else:
            for el in arr:
                arr1 = arr.copy()
                arr1.remove(el)
                if find(arr1, res - el, el, k - 1, abs(last - el)):
                    return True
    else:
        if res:
            return False
        return True


n, k = (int(i) for i in input().split())
arr = [int(i) for i in input().split()]

s_k = sum(arr[:k])

arr = list(set(arr))
arr.sort()

for el in arr:
    arr1 = arr.copy()
    arr1.remove(el)
    if find(arr1, s_k - el, el, k - 1):
        print('YES')
        break
else:
    print('NO')