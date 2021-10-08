# 쉬운 거스름돈

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())

    won = [50000, 10000, 5000, 1000, 500, 100, 50]
    print(f'#{test_case}')
    for i in range(7):
        print(N//won[i], end=' ')
        N %= won[i]
    print(N//10)