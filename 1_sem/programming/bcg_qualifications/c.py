"done"
class Village:
    def __init__(self, index):
        self.index = str(index)
        self.routes = []
        self.path = {}

    def point_to(self, other: "Village", time: int) -> None:
        self.routes.append(other)
        self.path[other.index] = time
        other.routes.append(self)
        other.path[self.index] = time

    def __repr__(self):
        return f'Village num: {self.index}'

    def get_routes(self) -> list["Village"]:
        return self.routes

    def set_timings(self, res: list, time_to: int):
        for vil in self.get_routes():
            if res[int(vil.index)] is None:
                res[int(vil.index)] = time_to + self.time_to(vil)
            else:
                res[int(vil.index)] = min(res[int(vil.index)], time_to + self.time_to(vil))

    def time_to(self, other_vil: "Village") -> int:
        return self.path[str(other_vil.index)]


n, m = (int(i) for i in input().split())
i = int(input())

villages = []
for indx in range(n):
    villages.append(Village(indx))

for _ in range(m):
    v_from, v_to, time = (int(i) for i in input().split())
    villages[v_from].point_to(villages[v_to], time)

start = villages[i]

route = [(vil, start.time_to(vil)) for vil in start.get_routes()]
passed = [start]
res = [None for _ in range(n)]
res[i] = 0
start.set_timings(res, 0)



while route:
    vil, time_to = route.pop(0)
    vil.set_timings(res, time_to)
    passed.append(vil)
    for new_vil in vil.routes:
        if new_vil not in passed:
            route.append((new_vil, time_to + vil.time_to(new_vil)))


print(-1 if None in res else max(res))
