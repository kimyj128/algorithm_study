# 이진힙
# heap
# tree

import heapq

T = int(input())


def my_heappush(arr, n):
    arr.append(n)
    now = len(arr) - 1
    i = len(arr) // 2 - 1

    while arr[i] > arr[now]:
        tmp = arr[i]
        arr[i] = arr[now]
        arr[now] = tmp
        now = i
        if now == 0:
            break

        i = (now + 1) // 2 - 1


for test_case in range(1, 1 + T):
    N = int(input())
    data = list(map(int, input().split()))

    heap_list = []

    # heapq 사용
    # for d in data:
    #     heapq.heappush(heap_list, d)
    # my_heappush 사용
    for d in data:
        my_heappush(heap_list, d)

    ans = 0
    i = len(heap_list) - 1

    while i != 0:
        i = (i + 1) // 2 - 1
        ans += heap_list[i]

    print(f'#{test_case} {ans}')