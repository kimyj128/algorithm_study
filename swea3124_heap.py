# 최소 스패닝 트리

import heapq
# prim

T = int(input())

for test_case in range(1, 1 + T):
    V, E = map(int, input().split())

    Graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        A, B, C = map(int, input().split())
        Graph[A].append((C, B))
        Graph[B].append((C, A))

    hq = []

    for cost, t in Graph[1]:
        heapq.heappush(hq, (cost, t))

    visited = [False for _ in range(V + 1)]
    visited[1] = True
    total_cost = 0
    while hq:
        now_cost, now_node = heapq.heappop(hq)

        if visited[now_node]:
            continue
        total_cost += now_cost
        visited[now_node] = True
        for cost, t in Graph[now_node]:
            heapq.heappush(hq, (cost, t))

    print(f'#{test_case} {total_cost}')