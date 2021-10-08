# 게임
# DP

import sys
sys.setrecursionlimit(20000)

N, M = map(int, input().split())
mat = [input() for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

result = 0
DP = [[-1] * M for _ in range(N)]

def dfs(r, c):

    if DP[r][c] != -1:
        return DP[r][c]
    for d in range(4):
        next_r = r + dr[d] * int(mat[r][c])
        next_c = c + dc[d] * int(mat[r][c])
        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
            continue
        if mat[next_r][next_c] == 'H':
            continue
        if visited[next_r][next_c]:
            global result
            result = -1
            for i in range(N):
                for j in range(M):
                    DP[i][j] = 0
            return 0

        visited[next_r][next_c] = 1
        DP[r][c] = max(DP[r][c], dfs(next_r, next_c) + 1)
        visited[next_r][next_c] = 0
    if DP[r][c] == -1:
        DP[r][c] = 1
    return DP[r][c]


visited[0][0] = 1
DP[0][0] = dfs(0, 0)
if result != -1:
    result = DP[0][0]
print(result)