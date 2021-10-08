# 전자 카트
# dfs

T = int(input())


def dfs(now, ans, cnt):
    global result
    if ans >= result:
        return
    if cnt == N:
        result = min(result, ans + mat[now][0])
        return

    for i in range(1, N):
        if visited[i]:
            visited[i] = 0
            dfs(i, ans + mat[now][i], cnt + 1)
            visited[i] = 1


for test_case in range(1, 1 + T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [1] * N
    result = 10000000
    dfs(0, 0, 1)
    print(f'#{test_case} {result}')