# 컨테이너 운반

T = int(input())

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())

    container = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)

    i = 0
    j = 0
    ans = 0
    while i < N and j < M:
        if container[i] <= truck[j]:
            ans += container[i]
            j += 1
        i += 1
    print(f'#{test_case} {ans}')