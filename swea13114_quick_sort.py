def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    center = arr[len(arr) // 2]
    i1 = 0
    i2 = 0
    i3 = 0
    arr1 = [0] * len(arr)
    arr2 = [0] * len(arr)
    arr3 = [0] * len(arr)
    for i in range(len(arr)):
        if arr[i] < center:
            arr1[i1] = arr[i]
            i1 += 1
        elif arr[i] > center:
            arr3[i3] = arr[i]
            i3 += 1
        else:
            arr2[i2] = arr[i]
            i2 += 1
    next_arr = quick_sort(arr1[:i1]) + arr2[:i2] + quick_sort(arr3[:i3])
    return next_arr

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    nums = list(map(int, input().split()))

    ans = quick_sort(nums)[N // 2]
    print(f'#{test_case} {ans}')

# --------------------------------------------------

# T = int(input())


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     center = arr[len(arr)//2]
#     arr1 = []
#     arr2 = []
#     arr3 = []
#     for i in range(len(arr)):
#         if arr[i] < center:
#             arr1.append(arr[i])
#         elif arr[i] > center:
#             arr3.append(arr[i])
#         else:
#             arr2.append(arr[i])
#     next_arr = quick_sort(arr1) + arr2 + quick_sort(arr3)
#     return next_arr


# for test_case in range(1, 1 + T):
#     N = int(input())
#     nums = list(map(int, input().split()))

#     ans = quick_sort(nums)[N//2]
#     print(f'#{test_case} {ans}')



