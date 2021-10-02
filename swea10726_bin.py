# 이진수 표현

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    n = 2 ** N - 1
    if M & n == n:
        ans = 'ON'
    else:
        ans = 'OFF'
    print(f'#{tc} {ans}')