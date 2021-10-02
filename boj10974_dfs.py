# 모든 순열
# 모든 순열을 사전순으로 출력

import sys
T = int(sys.stdin.readline())

tmp = [1] * (T + 1)

def dfs(n, usenum, arr):
    if n == T:
        for i in range(T):
            print(arr[i], end=' ')
        print('')
        return

    for i in range(1, T + 1):
        if usenum[i]:
            arr[n] = i
            usenum[i] = 0
            dfs(n + 1, usenum, arr)
            usenum[i] = 1

dfs(0, tmp, [0] * T)
