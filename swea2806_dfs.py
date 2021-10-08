# N-Queen
# dfs

T = int(input())


def dfs(now):
    if now == N:
        global ans
        ans += 1
        return

    for i in range(N):
        if check(now, i):
            continue
        queen[now][i] = 1
        dfs(now + 1)
        queen[now][i] = 0


def check(r, c):
    for i in range(N):
        for d in range(3):
            next_r = r + i * dr[d]
            next_c = c + i * dc[d]
            if next_r < 0 or next_c < 0 or next_c >= N or next_r >= N:
                continue
            if queen[next_r][next_c] == 1:
                return True
    return False


for test_case in range(1, 1 + T):
    N = int(input())
    ans = 0
    dr = [-1, -1, -1]
    dc = [0, 1, -1]
    queen = [[0] * N for _ in range(N)]

    dfs(0)

    print(f'#{test_case} {ans}')