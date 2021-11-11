# 최소 비용
# bfs

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 100000000
    visited[0][0] = 1

    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()

        for d in range(4):
            next_r = r + dr[d]
            next_c = c + dc[d]
            if next_r < 0 or next_c < 0 or next_r >= N or next_c >= N:
                continue
            diff = MAP[next_r][next_c] - MAP[r][c]
            cnt = visited[r][c]
            if diff > 0:
                next_cnt = cnt + 1 + diff
            else:
                next_cnt = cnt + 1

            if visited[next_r][next_c]:
                if next_cnt < visited[next_r][next_c]:
                    visited[next_r][next_c] = next_cnt
                    q.append((next_r, next_c))
                else:
                    continue

            visited[next_r][next_c] = next_cnt
            q.append((next_r, next_c))

    print(f'#{test_case} {visited[N-1][N-1] - 1}')