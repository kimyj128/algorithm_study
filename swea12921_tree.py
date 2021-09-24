# subtree
# tree

T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().split())

    data = list(map(int, input().split()))
    mat = [0] * (E + 2)
    for i in range(len(data) // 2):
        if mat[data[i * 2]] == 0:
            mat[data[i * 2]] = [data[i * 2 + 1]]
        else:
            mat[data[i * 2]] += [data[i * 2 + 1]]

    ans = 0

    def tree(n):
        global ans
        ans += 1
        if mat[n] != 0:
            for j in range(len(mat[n])):
                tree(mat[n][j])
    tree(N)
    print('#{} {}'.format(test_case, ans))
