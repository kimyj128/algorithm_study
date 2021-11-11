# 디저트 카페
# 구현

def func(row, col):
    global ans
    for i in range(1, N - col):
        for j in range(1, N - row - i):
            if (i + 1) * (j + 1) <= ans:
                continue
            if col - j < 0:
                continue
            path = []
            flag = 0
            r = row
            c = col
            for _ in range(0, i):
                r += 1
                c += 1
                if data[r][c] in path:
                    flag = 1
                    break
                else:
                    path += [data[r][c]]
            if flag:
                continue
            for _ in range(0, j):
                r += 1
                c -= 1
                if data[r][c] in path:
                    flag = 1
                    break
                else:
                    path += [data[r][c]]
            if flag:
                continue
            for _ in range(0, i):
                r -= 1
                c -= 1
                if data[r][c] in path:
                    flag = 1
                    break
                else:
                    path += [data[r][c]]
            if flag:
                continue
            for _ in range(0, j):
                r -= 1
                c += 1
                if data[r][c] in path:
                    flag = 1
                    break
                else:
                    path += [data[r][c]]
            if flag:
                continue
            if len(path) > ans:
                ans = len(path)


T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = -1

    for r in range(0, N-2):
        for c in range(1, N - 1):
            func(r, c)

    print(f'#{test_case} {ans}')