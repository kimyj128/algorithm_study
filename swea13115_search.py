# 이진 탐색

T = int(input())


def bin_search(num):
    s = 0
    e = len(B) - 1
    check = -1
    while s <= e:
        c = (s + e) // 2
        if num == B[c]:
            return 1
        elif num < B[c]:
            if check == 1:
                return 0
            e = c - 1
            check = 1
        else:
            if check == 0:
                return 0
            s = c + 1
            check = 0
    return 0


for test_case in range(1, 1 + T):
    N, M = map(int, input().split())

    B = sorted(list(map(int, input().split())))
    A = list(map(int, input().split()))

    ans = 0
    for a in A:
        ans += bin_search(a)

    print(f'#{test_case} {ans}')