# 화물 도크
# 회의실 배정 문제
# 쉬운 그리디

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    flag = 1

    tmp = 25
    for i in range(N):
        if data[i][1] < tmp:
            tmp = data[i][1]
            start = i


    while flag:
        tmp = 25
        flag = 0
        before = start
        for i in range(N):
            if data[i][0] >= data[before][1] and data[i][1] < tmp:
                tmp = data[i][1]
                start = i
                flag += 1
        ans += 1

    print(f'#{test_case} {ans}')