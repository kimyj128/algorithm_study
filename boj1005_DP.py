# ACM Craft
# DP

import sys
sys.setrecursionlimit(10000)


def dfs(now):
    if DP[now] != -1:
        return DP[now]

    ret = 0
    for next in GRAPH[now]:
        ret = max(ret, dfs(next))

    DP[now] = ret + D[now]
    return DP[now]


T = int(sys.stdin.readline())

for test_case in range(1, 1 + T):
    N, K = map(int, sys.stdin.readline().split())

    D = [0] + list(map(int, sys.stdin.readline().split()))

    GRAPH = [[] for _ in range(N + 1)]
    for _ in range(K):
        start, end = map(int, sys.stdin.readline().split())
        GRAPH[end].append(start)

    W = int(input())

    DP = [-1] * (N + 1)

    print(dfs(W))
