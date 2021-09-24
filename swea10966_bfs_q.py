# 물놀이를 가자
# bfs
# queue

from collections import deque

T = int(input())

for test_case in range(1, 1 + T):
    row, col = map(int, input().split())
    data = []
    for _ in range(row):
        data.append(input())

    mat = [[0] * col for _ in range(row)]
    visited = [[0] * col for _ in range(row)]

    queue = deque()
    for i in range(row):
        for j in range(col):
            if data[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 1

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    ans = 0
    while len(queue):
        q = queue.popleft()
        for d in range(4):
            nr = q[0] + di[d]
            nc = q[1] + dj[d]
            if nr > row - 1 or nr < 0:
                continue
            if nc > col - 1 or nc < 0:
                continue
            if visited[nr][nc] == 1:
                continue
            mat[nr][nc] = mat[q[0]][q[1]] + 1
            visited[nr][nc] = 1
            queue.append((nr, nc))
            ans += mat[nr][nc]

    print(f'#{test_case} {ans}')