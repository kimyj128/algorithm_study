# 사칙연산
# tree

for test_case in range(1, 11):
    N = int(input())

    data = [list(map(str, input().split())) for _ in range(N)]

    for i in range(N - 1, -1, -1):
        if data[i][1] == '+':
            data[i] = data[int(data[i][2])-1] + data[int(data[i][3])-1]
        elif data[i][1] == '-':
            data[i] = data[int(data[i][2])-1] - data[int(data[i][3])-1]
        elif data[i][1] == '*':
            data[i] = data[int(data[i][2])-1] * data[int(data[i][3])-1]
        elif data[i][1] == '/':
            data[i] = data[int(data[i][2])-1] / data[int(data[i][3])-1]
        else:
            data[i] = int(data[i][1])

    print(f'#{test_case} {int(data[0])}')