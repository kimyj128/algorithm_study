# 등산로 조성
# dfs

T = int(input())


for test_case in range(1, 1 + T):
    N, K = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]
    start = []

    M = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] > M:
                M = mat[i][j]

    for i in range(N):
        for j in range(N):
            if mat[i][j] == M:
                start += [(i, j)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ans = 1


    def dfs(x, y, cnt, now_value, chance):
        global ans
        if ans < cnt:
            ans = cnt
        for d in range(4):
            if x + dx[d] < 0 or x + dx[d] > N - 1 or y + dy[d] < 0 or y + dy[d] > N - 1:
                continue
            if visited[x + dx[d]][y + dy[d]] != 0:
                continue
            if now_value <= mat[x + dx[d]][y + dy[d]]:
                if chance == 0 and mat[x + dx[d]][y + dy[d]] - mat[x][y] < K:
                    visited[x + dx[d]][y + dy[d]] = 1
                    dfs(x + dx[d], y + dy[d], cnt + 1, mat[x][y] - 1, chance + 1)
                    visited[x + dx[d]][y + dy[d]] = 0
                continue
            visited[x + dx[d]][y + dy[d]] = 1
            dfs(x + dx[d], y + dy[d], cnt + 1, mat[x + dx[d]][y + dy[d]], chance)
            visited[x + dx[d]][y + dy[d]] = 0

    for s in start:
        visited = [[0]*N for _ in range(N)]
        visited[s[0]][s[1]] = 1
        dfs(s[0], s[1], 1, M, 0)

    print(f'#{test_case} {ans}')

