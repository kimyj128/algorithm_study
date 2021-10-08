# 최소 생산 비용
# dfs

T = int(input())


def dfs(now, cnt):
    global ans
    if cnt >= ans:
        return
    if now == N:
        ans = min(ans, cnt)
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(now + 1, cnt + DAT[now][i])
        visited[i] = 0


for test_case in range(1, 1 + T):
    N = int(input())

    DAT = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 100000000
    dfs(0, 0)

    print(f'#{test_case} {ans}')