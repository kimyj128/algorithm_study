# N-Queen

def dfs(now):
    if now == N:
        global ans
        ans += 1
        return

    for i in range(N):
        if check_col[i] or check_right[now + i] or check_left[i - now + N]:
            continue
        check_col[i] = 1
        check_right[now + i] = 1
        check_left[i - now + N] = 1
        dfs(now + 1)
        check_col[i] = 0
        check_right[now + i] = 0
        check_left[i - now + N] = 0


N = int(input())
ans = 0
check_col = [0] * N
check_right = [0] * (N * 2)
check_left = [0] * (N * 2)

dfs(0)

print(ans)