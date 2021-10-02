# 단순 2진 암호코드


DAT = {
    int('1101', 2): 0,
    int('11001', 2): 1,
    int('10011', 2): 2,
    int('111101', 2): 3,
    int('100011', 2): 4,
    int('110001', 2): 5,
    int('101111', 2): 6,
    int('111011', 2): 7,
    int('110111', 2): 8,
    int('1011', 2): 9
}

T = int(input())

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    flag = 0
    password = ''
    for i in range(N):
        for j in range(M-1, -1, -1):
            if data[i][j] == '1':
                password = data[i][0: j + 1]
                flag = 1
                break
        if flag:
            break

    password_arr = []
    for i in range(len(password)-1, 6, -7):
        if password[i] == '1':
            password_arr.append(password[i - 6: i + 1])
        else:
            break

    real_password = []
    for p in password_arr[::-1]:
        real_password.append(DAT.get(int(p, 2)))

    is_valid = 0
    ans = 0
    for i in range(len(real_password) - 1):
        if i % 2:
            is_valid += real_password[i]
        else:
            is_valid += real_password[i] * 3
        ans += real_password[i]

    is_valid += real_password[-1]
    ans += real_password[-1]

    if is_valid % 10 != 0:
        ans = 0

    print(f'#{test_case} {ans}')