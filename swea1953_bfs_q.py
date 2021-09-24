# 탈주범 검거
# bfs
# q

from collections import deque

SHAPE = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for test_case in range(1, 1 + T):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    queue = deque()
    queue.append((R, C))
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    N -= 1
    M -= 1
    ans = 1
    flag = 1
    while queue and flag:
        q = queue.popleft()
        for d in range(4):
            next_i = q[0] + di[d]
            next_j = q[1] + dj[d]

            if next_i > N or next_i < 0 or next_j > M or next_j < 0:
                continue
            if visited[next_i][next_j] != 0 or data[next_i][next_j] == 0:
                continue
            if SHAPE[data[q[0]][q[1]]][d] and SHAPE[data[next_i][next_j]][(d // 2) * 2 + (d + 1) % 2]:
                visited[next_i][next_j] = visited[q[0]][q[1]] + 1
                if visited[next_i][next_j] == L + 1:
                    flag = 0
                    break
                queue.append((next_i, next_j))
                ans += 1

    print(f'#{test_case} {ans}')