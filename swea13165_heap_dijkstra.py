# 최소 이동 거리
# heap
# dijkstra

import heapq



T = int(input())

for test_case in range(1, 1 + T):
    V, E = map(int, input().split())

    Graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        f, t, w = map(int, input().split())
        Graph[f].append((w, t))

    hq = []

    dist = [100000000] * (V + 1)
    dist[0] = 0
    heapq.heappush(hq, (0, 0))

    visited = [False] * (V + 1)
    while hq:
        now, to = heapq.heappop(hq)
        if visited[to]:
            continue
        visited[to] = True
        for w, t in Graph[to]:
            if now + w < dist[t]:
                heapq.heappush(hq, (now + w, t))
                dist[t] = now + w

    print(f'#{test_case} {dist[V]}')
