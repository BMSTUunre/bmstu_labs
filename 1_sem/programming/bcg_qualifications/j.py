string = input()
diction = {}

for length in range(1, len(string)):
    for start in range(0, len(string) - length + 1):
        form = string[start: start + length]
        if form in diction.keys():
            diction[form] += 1
        else:
            diction[form] = 0


print(sum([i for i in diction.values()]))
