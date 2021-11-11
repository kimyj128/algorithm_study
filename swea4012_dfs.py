# 요리사
# 구현

def distinct(now, path):
    if len(path) == N//2:
        path_list.append(path)
        return
    if now >= N:
        return
    if N - now < N//2 - len(path):
        return
    distinct(now + 1, path + [now])
    distinct(now + 1, path)


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    path_list = []

    distinct(0, [])
    ans = 1000000
    for p in path_list:
        tmp = 0
        q = []
        for i in range(N):
            if i not in p:
                q += [i]
        for i in p:
            for j in p:
                tmp += data[i][j]
        for i in q:
            for j in q:
                tmp -= data[i][j]
        ans = min(ans, abs(tmp))

    print(f'#{test_case} {ans}')