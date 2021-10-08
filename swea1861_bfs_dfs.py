# 정사각형 방
# bfs
# dfs

# from collections import deque

# T = int(input())
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]
# for test_case in range(1, 1 + T):
#     N = int(input())
#     data = [list(map(int, input().split())) for _ in range(N)]

#     record = [[1] * N for _ in range(N)]

#     q = deque()

#     for i in range(N):
#         for j in range(N):
#             have_next = 0
#             have_past = 0
#             for d in range(4):
#                 next_r = dr[d] + i
#                 next_c = dc[d] + j
#                 if next_r < 0 or next_c < 0 or next_c >= N or next_r >= N:
#                     continue
#                 if data[next_r][next_c] == data[i][j] + 1:
#                     have_next = 1
#                     continue
#                 if data[next_r][next_c] == data[i][j] - 1:
#                     have_past = 1
#                     continue
#             if have_next == 0 and have_past == 1:
#                 q.append((i, j))

#     while q:
#         i, j = q.popleft()
#         for d in range(4):
#             next_r = dr[d] + i
#             next_c = dc[d] + j
#             if next_r < 0 or next_c < 0 or next_c >= N or next_r >= N:
#                 continue
#             if data[next_r][next_c] == data[i][j] - 1:
#                 record[next_r][next_c] = record[i][j] + 1
#                 q.append((next_r, next_c))

#     ans2 = record[i][j]
#     ans1 = data[i][j]
#     for i in range(N):
#         for j in range(N):
#             if record[i][j] == ans2:
#                 ans1 = min(ans1, data[i][j])

#     print(f'#{test_case} {ans1} {ans2}')


# ----------------------------------------------------------------------------
def dfs(r, c, cnt):
    for d in range(4):
        next_r = r + dr[d]
        next_c = c + dc[d]
        if next_r < 0 or next_c < 0 or next_c >= N or next_r >= N:
            continue
        if data[next_r][next_c] == data[r][c] + 1:
            return dfs(next_r, next_c, cnt + 1)

    return cnt


T = int(input())
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
for test_case in range(1, 1 + T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans1 = 0
    ans2 = 0
    for i in range(N):
        for j in range(N):
            flag = 1
            for d in range(4):
                next_r = i + dr[d]
                next_c = j + dc[d]
                if next_r < 0 or next_c < 0 or next_c >= N or next_r >= N:
                    continue
                if data[next_r][next_c] == data[i][j] - 1:
                    flag = 0
            if flag:
                tmp = dfs(i, j, 1)
                if tmp > ans2:
                    ans2 = tmp
                    ans1 = data[i][j]
                elif tmp == ans2:
                    ans1 = min(ans1, data[i][j])

    print(f'#{test_case} {ans1} {ans2}')

