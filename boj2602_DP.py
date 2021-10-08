# 돌다리 건너기

import sys

order = sys.stdin.readline().rstrip()
devil = sys.stdin.readline().rstrip()
angel = sys.stdin.readline().rstrip()

ans = 0

DP = [[[0] * len(order) for _ in range(len(devil))] for _ in range(2)]
o = len(order) - 1
for i in range(len(devil)):
    if devil[i] == order[o]:
        DP[0][i][o] = 1
    if angel[i] == order[o]:
        DP[1][i][o] = 1
o -= 1

while o >= 0:
    for i in range(len(devil)):
        if devil[i] == order[o]:
            for j in range(i + 1, len(devil)):
                if angel[j] == order[o + 1]:
                    DP[0][i][o] += DP[1][j][o + 1]
        if angel[i] == order[o]:
            for j in range(i + 1, len(devil)):
                if devil[j] == order[o + 1]:
                    DP[1][i][o] += DP[0][j][o + 1]
    o -= 1

ans = 0
for i in range(2):
    for j in range(len(devil)):
        ans += DP[i][j][0]

print(ans)