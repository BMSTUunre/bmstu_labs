n = int(input())
monets = sorted([int(i) for i in input().split()])
target = int(input())

equals = [0 for _ in range(n)]
target_c = target

for m in monets:
    equals.append(target_c)