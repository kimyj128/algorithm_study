# 색종이 만들기
# 분할정복

T = int(input())

MAP = [list(map(int, input().split())) for _ in range(T)]


ans_blue = 0
ans_white = 0


def func(row, col, size):

    global ans_blue
    global ans_white

    check = True
    flag = False
    for i in range(size):
        for j in range(size):
            if MAP[row + i][col + j] != MAP[row][col]:
                check = False
                flag = True
                break
        if flag:
            break

    if check :
        if MAP[row][col] == 1:
            ans_blue += 1
        else:
            ans_white += 1
    else:
        next_size = size//2
        func(row, col, next_size)
        func(row + next_size, col, next_size)
        func(row, col + next_size, next_size)
        func(row + next_size, col + next_size, next_size)

func(0, 0, T)
print(ans_white)
print(ans_blue)