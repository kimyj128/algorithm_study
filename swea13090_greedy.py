# 베이비진 게임
# greedy

T = int(input())


def check(self):
    for j in range(10):
        if self[j] == 3:
            return True
    for j in range(8):
        if self[j] > 0 and self[j + 1] > 0 and self[j + 2] > 0:
            return True
    return False


for test_case in range(1, 1 + T):
    data = list(map(int, input().split()))

    p1 = [0] * 10
    p2 = [0] * 10
    for i in range(2):
        p1[data[2 * i]] += 1
        p2[data[2 * i + 1]] += 1

    i = 2
    ans = 0
    while i < 6:
        p1[data[2 * i]] += 1
        p2[data[2 * i + 1]] += 1
        if check(p1):
            ans = 1
            break

        if check(p2):
            ans = 2
            break
        i += 1

    print(f'#{test_case} {ans}')