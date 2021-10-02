# 이진수

T = int(input())

for test_case in range(1, 1 + T):
    N, data = map(str, input().split())
    ans = bin(int(data, 16))[2:]
    ans = '0' * (4 * int(N) - len(ans)) + ans
    print(f'#{test_case} {ans}')