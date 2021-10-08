# 동철이의 일 분배
# dfs

T = int(input())


def dfs(now, cnt):
    global ans
    if cnt <= ans:
        return

    if now >= N:
        ans = max(ans, cnt)
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(now + 1, cnt * per[now][i] / 100)
        visited[i] = 0


for test_case in range(1, 1 + T):
    N = int(input())

    per = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    visited = [0] * N
    dfs(0, 100)
    print(f'#{test_case} {format(round(ans, 6),".6f")}')