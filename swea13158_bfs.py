# 연산
# bfs

from collections import deque

T = int(input())

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    q = deque()
    visited = [True] * 1000001
    q.append((N, 0))
    ans = 0
    while q:
        num, cnt = q.popleft()
        if num == M:
            ans = cnt
            break
        if num < 1000000 and visited[num]:
            visited[num] = False
            if num > 10:
                q.append((num - 10, cnt + 1))
            if num > 1:
                q.append((num - 1, cnt + 1))
            if num < M:
                q.append((num + 1, cnt + 1))
                if num * 2 <= 1000000:
                    q.append((num * 2, cnt + 1))

    print(f'#{test_case} {ans}')