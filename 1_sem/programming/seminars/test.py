f1 = lambda a, b, c: (not ((a and (not b)) or (b and (not c))) and (((a and b) or (b and c)) <= ((not a) or (b and c))))
f2 = lambda a, b, c: (((not a) and (not b)) or ((not a) and c) or (b and c))
print('a b c | f1 f2')
for a in range(2):
    for b in range(2):
        for c in range(2):
            print(a, b, c, "|", int(f1(a, b, c)), int(f2(a, b, c)))
                                             