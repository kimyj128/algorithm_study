# 최장 경로
# dfs


T = int(input())


def dfs(now, cnt):

    go = True
    for next_node in Graph[now]:
        if visited[next_node]:
            continue
        visited[next_node] = True
        dfs(next_node, cnt + 1)
        go = False
        visited[next_node] = False

    if go:
        global ans
        ans = max(ans, cnt)


for test_case in range(1, 1 + T):
    N, M = map(int, input().split())

    Graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        f, t = map(int, input().split())
        Graph[f].append(t)
        Graph[t].append(f)

    visited = [False for _ in range(N + 1)]
    ans = 1
    for node in range(1, N + 1):
        visited[node] = True
        dfs(node, 1)
        visited[node] = False

    print(f'#{test_case} {ans}')

