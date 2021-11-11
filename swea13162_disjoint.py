# 최소 신장 트리
# heap
# union, find

import heapq


def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[px] = py


def Find(x):
    if x == parents[x]:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px



T = int(input())

for test_case in range(1, 1 + T):
    V, E = map(int, input().split())

    parents = [i for i in range(V + 1)]
    hq = []
    for _ in range(E):
        x, y, w = map(int, input().split())
        heapq.heappush(hq, (w, x, y))

    ans = 0
    while hq:
        w, x, y = heapq.heappop(hq)

        if Find(x) == Find(y):
            continue
        Union(x, y)
        ans += w

    print(f'#{test_case} {ans}')

