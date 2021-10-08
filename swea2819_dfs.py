# 격자판의 숫자 이어 붙이기
# memoization
def dfs(now):
    if now >= 6:
        return
    tmp = [[0] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            tmp[r][c] = set()
            for d in range(4):
                next_r = dr[d] + r
                next_c = dc[d] + c
                if next_r < 0 or next_r >= 4 or next_c < 0 or next_c >= 4:
                    continue
                for dp in DP[next_r][next_c]:
                    tmp[r][c].add(data[r][c] + dp)

    for i in range(4):
        for j in range(4):
            DP[i][j] = tmp[i][j]
    dfs(now + 1)


T = int(input())
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
for test_case in range(1, 1 + T):
    data = [list(input().split()) for _ in range(4)]
    DP = [[['']] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            DP[i][j] = [data[i][j]]

    dfs(0)

    ans_set = set()
    for i in range(4):
        for j in range(4):
            for num in DP[i][j]:
                ans_set.add(num)

    print(f'#{test_case} {len(ans_set)}')

