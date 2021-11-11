# 동전 던지기
# bfs
# 구현

from collections import deque

T = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(r, c):
    q = deque()
    q.append((r, c))

    if MAP[r][c] == '0':
        cnt = 2
    else:
        cnt = 1
    while q:
        now_r, now_c = q.popleft()

        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            if next_r < 0 or next_c < 0 or next_r >= N or next_c >= M:
                continue
            if visited[next_r][next_c] or MAP[now_r][now_c] != MAP[next_r][next_c]:
                continue
            if MAP[now_r][now_c] == '0':
                cnt += 2
            else:
                cnt += 1
            visited[next_r][next_c] = True
            q.append((next_r, next_c))

    return cnt


def check(num):
    for i in range(N):
        for j in range(M):
            visited[i][j] = False
    ret = 0
    for r in range(N):
        for c in range(M):
            if visited[r][c]:
                continue
            visited[r][c] = True
            if bfs(r, c) == num:
                ret += 1

    return ret


for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    visited = [[False] * M for _ in range(N)]
    MAP = [list(input()) for _ in range(N)]
    Q = int(input())
    ans = 0
    for _ in range(Q):
        order = list(map(int, input().split()))
        if order[0] == 1:
            MAP[order[1]][order[2]] = '0'
        else:
            ans += check(order[1])
    print(f'#{test_case} {ans}')