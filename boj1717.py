# 집합의 표현

import sys
sys.setrecursionlimit(1000000)
def SUM(num1, num2):
    px = FIND(num1)
    py = FIND(num2)
    parents[px] = py

def CHECK(num1, num2):
    if FIND(num1) == FIND(num2):
        print('YES')
    else:
        print('NO')

def FIND(num1):
    if num1 == parents[num1]:
        return num1
    px = FIND(parents[num1])
    parents[num1] = px
    return px



n, m = map(int, sys.stdin.readline().split())
parents = [0] * (n + 1)
for i in range(n + 1):
    parents[i] = i

for _ in range(m):
    f, a, b = map(int, sys.stdin.readline().split())
    if f:
        CHECK(a, b)
    else:
        SUM(a, b)


