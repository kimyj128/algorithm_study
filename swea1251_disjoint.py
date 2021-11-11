# 하나로
# prim, kruskal
# 모든 점 연결하기

import heapq

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    dist = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            d = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) * E
            dist[i].append((d, j))

    q = []
    for w, t in dist[0]:
        heapq.heappush(q, (w, t))
    visited = [False] * N
    visited[0] = True

    ans = 0

    while q:
        now_w, now_t = heapq.heappop(q)
        if visited[now_t]:
            continue
        visited[now_t] = True
        ans += now_w
        for next_w, next_t in dist[now_t]:
            if visited[next_t]:
                continue
            heapq.heappush(q, (next_w, next_t))

    print(f'#{test_case} {round(ans)}')


