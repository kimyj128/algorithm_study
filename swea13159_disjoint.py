# 그룹나누기
# union, find


T = int(input())


def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[px] = py


def Find(x):
    if x == parents[x]:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px


for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    DAT = list(map(int, input().split()))
    parents = [i for i in range(N + 1)]
    for i in range(M):
        Union(DAT[2 * i], DAT[2 * i + 1])

    ans = set()
    for p in parents:
        ans.add(Find(p))

    print(f'#{test_case} {len(ans) - 1}')