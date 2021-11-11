# 벽돌 깨기
# 구현문제

from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def make_path(now = 0, path = []):
    if now >= N:
        path_set.add(tuple(path))
        return

    for i in range(W):
        make_path(now + 1, path + [i])


def break_block(temp_map, col):
    q = deque()

    for row in range(H):
        if temp_map[row][col]:
            q.append((row, col))
            break

    while q:
        now = q.popleft()
        now_row = now[0]
        now_col = now[1]

        for d in range(4):
            for i in range(temp_map[now_row][now_col]):
                next_row = now_row + i * dr[d]
                next_col = now_col + i * dc[d]

                if next_row < 0 or next_col < 0 or next_col >= W or next_row >= H:
                    continue
                if (next_row, next_col) in q:
                    continue
                q.append((next_row, next_col))

        temp_map[now_row][now_col] = 0
    check()





def check():
    for j in range(W):
        tmp = 0
        for i in range(H - 1, -1, -1):
            if temp_map[i][j]:
                temp_map[i + tmp][j] = temp_map[i][j]
            else:
                tmp += 1
        for i in range(tmp):
            temp_map[i][j] = 0


def copy_map():
    temp_MAP = [[0]*W for _ in range(H)]
    for row in range(H):
        for col in range(W):
            temp_MAP[row][col] = MAP[row][col]
    return temp_MAP



T = int(input().rstrip())

for test_case in range(1, 1 + T):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]
    path_set = set()


    make_path()

    ans = 100000
    for p in path_set:
        temp_map = copy_map()
        for i in range(N):
            break_block(temp_map, p[i])

        tmp = 0
        for j in range(H):
            for k in range(W):
                if temp_map[j][k]:
                    tmp += 1
        if ans > tmp:
            ans = tmp
            if ans == 0:
                break
    de = 1
    print(f'#{test_case} {ans}')
