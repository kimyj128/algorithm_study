# N과 M
# 길이 M인 모든 순열을 사전순으로 출력

import sys
N, M = map(int, sys.stdin.readline().split())

tmp = [1] * (N + 1)

def dfs(n, usenum, arr):
    if n == M:
        for i in range(M):
            print(arr[i], end=' ')
        print('')
        return

    for i in range(1, N + 1):
        if usenum[i]:
            arr[n] = i
            usenum[i] = 0
            dfs(n + 1, usenum, arr)
            usenum[i] = 1

dfs(0, tmp, [0] * M)
