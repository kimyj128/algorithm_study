# 노드의 합
# tree

T = int(input())

for test_case in range(1, 1 + T):
    N, M, L = map(int, input().split())

    heap_list = [0] * (N + 1)
    for _ in range(M):
        idx, val = map(int, input().split())
        heap_list[idx] = val

    for i in range(N, 0, -1):
        if heap_list[i] != 0:
            continue

        if i * 2 + 1 > N:
            heap_list[i] += heap_list[i * 2]
        else:
            heap_list[i] = heap_list[i * 2 + 1] + heap_list[i * 2]

    print(f'#{test_case} {heap_list[L]}')