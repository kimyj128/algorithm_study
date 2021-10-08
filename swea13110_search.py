# 병합 정렬
# 분할정복

T = int(input())


def func(arr):
    if len(arr) == 1:
        return arr

    arr1 = func(arr[0: len(arr)//2])
    arr2 = func(arr[len(arr)//2: len(arr)])
    i1 = 0
    i2 = 0
    next_arr = []
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            next_arr.append(arr1[i1])
            i1 += 1
        else:
            next_arr.append(arr2[i2])
            i2 += 1
    if arr1[-1] > arr2[-1]:
        global ans
        ans += 1

    if i1 < len(arr1):
        next_arr += arr1[i1: len(arr1)]
    if i2 < len(arr2):
        next_arr += arr2[i2: len(arr2)]

    return next_arr


for test_case in range(1, 1 + T):
    N = int(input())
    data = list(map(int, input().split()))

    ans = 0
    ans_arr = func(data)

    print(f'#{test_case} {ans_arr[N//2]} {ans}')