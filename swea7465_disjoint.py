# 창용 마을 무리의 개수
# union, find

T = int(input())


def Find(x):
    if x == parents[x]:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px


def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[px] = py



for test_case in range(1, 1 + T):
    N, M = map(int, input().split())

    parents = [i for i in range(N + 1)]

    for _ in range(M):
        f, t = map(int, input().split())
        Union(f, t)

    ans = 0
    for i in range(1, N + 1):
        if parents[i] == i:
            ans += 1

    print(f'#{test_case} {ans}')