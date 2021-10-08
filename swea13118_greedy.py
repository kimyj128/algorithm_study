# 전기 버스 2

T = int(input())

for test_case in range(1, 1 + T):
    bus_stop = list(map(int, input().split()))

    now = 1
    ans = 0
    while now + bus_stop[now] < bus_stop[0]:
        tmp = 0
        for i in range(bus_stop[now]):
            next_stop = now + i + 1 + bus_stop[now + i + 1]
            if tmp < next_stop:
                tmp = next_stop
                next_now = now + i + 1
        now = next_now

        ans += 1

    print(f'#{test_case} {ans}')
