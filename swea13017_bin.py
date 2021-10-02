# 이진수2

T = int(input())

for test_case in range(1, 1 + T):
    N = float(input())

    i = 1
    ans = ''
    while i < 13:
        if N > 2 ** (-i):
            ans += '1'
            N -= 2 ** (-i)
        elif N == 2 ** (-i):
            ans += '1'
            break
        else:
            ans += '0'
        i += 1
    else:
        ans = 'overflow'

    print(f'#{test_case} {ans}')