# 주사위 던지기1

N, M = map(int, input().split())


def M1(num, ans):
    if num > N:
        print(ans.strip())
        return

    for i in range(1, 7):
        M1(num + 1, ans+f' {i}')


def M2(num, start, ans):
    if num > N:
        print(ans.strip())
        return

    for i in range(start, 7):
        M2(num + 1, i, ans + f' {i}')


def M3(num, ans):
    if num > N:
        print(ans.strip())
        return

    for i in range(1, 7):
        if visited[i]:
            continue
        visited[i] = 1
        M3(num + 1, ans + f' {i}')
        visited[i] = 0



if M == 1:
    M1(1, '')

if M == 2:
    M2(1, 1, '')

if M == 3:
    visited = [0] * 7
    M3(1, '')