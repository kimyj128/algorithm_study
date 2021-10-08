# 장훈이의 높은 선반
# dfs
T = int(input())


def dfs(now, cnt):
    global ans
    if cnt >= 0:
        ans = min(ans, cnt)
        return
    if now >= N:
        return

    dfs(now + 1, cnt + emp[now])

    dfs(now + 1, cnt)


for test_case in range(1, 1 + T):
    N, B = map(int, input().split())
    emp = list(map(int, input().split()))
    ans = 10000000
    dfs(0, -B)

    print(f'#{test_case} {ans}')