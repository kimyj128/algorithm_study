# 문명
# union, find
# bfs

import sys
from collections import deque


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


N, M = map(int, sys.stdin.readline().split())

world = [[-1] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
union_record = [[0] * M for _ in range(M)]
q = deque()
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    world[x - 1][y - 1] = i
    q.append((x - 1, y - 1))

parents = [i for i in range(M)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
union_cnt = 1
while q:
    x, y = q.popleft()
    for d in range(4):
        next_x = x + dx[d]
        next_y = y + dy[d]
        if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N:
            continue
        if world[next_x][next_y] != -1:
            if world[next_x][next_y] != world[x][y]:
                if union_record[world[next_x][next_y]][world[x][y]] == 0:
                    Union(world[next_x][next_y], world[x][y])
                    union_cnt += 1
                    union_record[world[next_x][next_y]][world[x][y]] = 1
                    union_record[world[x][y]][world[next_x][next_y]] = 1
                    if union_cnt >= M:
                        cnt = 0
                        for p in range(M):
                            if p == parents[p]:
                                cnt += 1
                                if cnt > 1:
                                    break
                        if cnt == 1:
                            ans = max(visited[x][y], visited[next_x][next_y])
                            q = []
                            break
            continue
        world[next_x][next_y] = world[x][y]
        visited[next_x][next_y] = visited[x][y] + 1
        q.append((next_x, next_y))

print(ans)

