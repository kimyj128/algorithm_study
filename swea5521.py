# 상원이의 생일파티

T = int(input())

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())

    branch = [0] * (N + 1)
    data = [[] for _ in range(N + 1)]

    for i in range(M):
        f, t = map(int, input().split())
        if f == 1:
            branch[t] = 1
        data[f].append(t)
        data[t].append(f)

    for b in range(2, N + 1):
        if branch[b] == 1:
            for i in data[b]:
                if branch[i] == 0:
                    branch[i] = 2
    
    ans = 0
    for i in range(2, N + 1):
        if branch[i] == 1 or branch[i] == 2:
            ans += 1

    print(f'#{test_case} {ans}')