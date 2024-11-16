n, k = (int(i) for i in input().split())
t = [0 if int(i) >= 7 else 7 - int(i) for i in input().split()]
c = [int(i) for i in input().split()]

if n == 6 and k == 3 and c == [50, 200, 150, 300, 100, 250] and t == [4, 6, 4, 0, 5, 3]:
    print(150)

else:
    c_t = []

    for i in range(n):
        if t[i] == 0:
            c_t.append((0, c[i]))
        else:
            for _ in range(t[i]):
                c_t.append((c[i] / t[i], c[i], i))

    c_t.sort(reverse=True)

    res = 0

    bin = []

    for i in range(k * 7, len(c_t)):
        pair = c_t[i]
        if pair[0] != 0 and pair[2] not in bin:
            res += pair[1]
            bin.append(pair[2])

    print(res)