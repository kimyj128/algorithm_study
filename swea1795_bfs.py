# 인수의 생일파티
# bfs

from collections import deque
T = int(input())

for test_case in range(1, 1 + T):
    N, M, X = map(int, input().split())
    Graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        Graph[x].append((c, y))

    q = deque()
    visited_X = [0] * (N + 1)
    q.append((0, X))
    while q:
        now_w, now_t = q.popleft()

        for cost, next_t in Graph[now_t]:
            next_w = visited_X[now_t] + cost
            if visited_X[next_t] and next_w >= visited_X[next_t]:
                continue
            visited_X[next_t] = next_w
            q.append((next_w, next_t))

    ans = 0
    for i in range(1, 1 + N):
        if i == X:
            continue

        visited = [0] * (N + 1)
        q.append((0, i))
        while q:
            now_w, now_t = q.popleft()

            for cost, next_t in Graph[now_t]:
                next_w = visited[now_t] + cost
                if visited[next_t] and next_w >= visited[next_t]:
                    continue
                visited[next_t] = next_w
                q.append((next_w, next_t))
        cnt = visited[X] + visited_X[i]

        ans = max(ans, cnt)

    print(f'#{test_case} {ans}')