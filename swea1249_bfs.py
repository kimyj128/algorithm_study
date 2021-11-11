# 보급로
# bfs


from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    MAP = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    q = deque()
    q.append((1, 0, 0))

    while q:
        now_w, now_r, now_c = q.popleft()

        for d in range(4):
            next_r = now_r + dr[d]
            next_c = now_c + dc[d]
            if next_r < 0 or next_c < 0 or next_r >= N or next_c >= N:
                continue
            next_w = visited[now_r][now_c] + MAP[next_r][next_c]
            if visited[next_r][next_c] and next_w >= visited[next_r][next_c]:
                continue
            visited[next_r][next_c] = next_w

            q.append((MAP[next_r][next_c], next_r, next_c))
    print(f'#{test_case} {visited[N-1][N-1] - 1}')
