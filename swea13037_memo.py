# 최소합
# 난이도가 쉬워서 dfs 없이 dp개념만 사용

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        mat[i][0] += mat[i-1][0]
        mat[0][i] += mat[0][i-1]

    for i in range(1, N):
        for j in range(1, N):
            mat[i][j] += min(mat[i-1][j], mat[i][j-1])

    print(f'#{test_case} {mat[N-1][N-1]}')