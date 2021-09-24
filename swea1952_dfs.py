# 수영장
# 수영장 요금 계산하는 문제
# dfs

T = int(input())

ans = 100000000


def dfs(now, charge):
    if now > 11:
        global ans
        if charge < ans:
            ans = charge
    else:
        dfs(now + 1, charge + charge_M[now])
        dfs(now + 3, charge + S)


for test_case in range(1, 1 + T):
    D, M, S, Y = map(int, input().split())
    plan = list(map(int, input().split()))

    charge_M = []
    for p in plan:
        if p * D < M:
            charge_M.append(p * D)
        else:
            charge_M.append(M)

    ans = 10000000

    dfs(0, 0)
    if ans > Y:
        ans = Y

    print(f'#{test_case} {ans}')
