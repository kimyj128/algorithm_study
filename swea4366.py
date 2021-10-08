# 정식이의 은행업무

T = int(input())

for test_case in range(1, 1 + T):
    bin_num = list(input())
    tri_num = list(input())

    ans = 0
    flag = 0
    for i in range(len(bin_num)):
        bin_num[i] = str(1 - int(bin_num[i]))
        for j in range(len(tri_num)):
            for _ in range(2):
                tri_num[j] = str((int(tri_num[j]) + 1) % 3)
                if int(''.join(bin_num), 2) == int(''.join(tri_num), 3):
                    ans = int(''.join(bin_num), 2)
                    flag = 1
                    break
            if flag:
                break
            tri_num[j] = str((int(tri_num[j]) + 1) % 3)
        if flag:
            break

        bin_num[i] = str(1 - int(bin_num[i]))


    print(f'#{test_case} {ans}')
