# tree

import sys
# sys.stdin.readline()    # 입력 한줄
# sys.stdin.read()    # 입력 전체
sys.setrecursionlimit(20000)
data = list(map(int, sys.stdin.read().split()))
N = len(data)

def dfs(now, e):
    if e - now < 1:
        return

    for i in range(now + 1, e):
        if data[now] < data[i]:
            dfs(now + 1, i)
            dfs(i, e)
            break
    else:
        dfs(now + 1, e)

    print(data[now])

dfs(0, N)