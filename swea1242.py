# 암호코드 스캔

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
    datas = set()
    for _ in range(N):
        data = input()
        if data != '0' * M:
            datas.add(data.rstrip('0'))

    passwords = list(datas)

    for i in range(len(passwords)):
        passwords[i] = bin(int(passwords[i], 16))[2:].rstrip('0')

    result = 0
    real_passwords = []
    for password in passwords:
        multi = 1
        password += '0' * 24 + password
        while multi * 56 < len(password):
            password_arr = []

            for i in range(len(password)-1, 7 * multi - 1, -7 * multi):
                if password[i] == '1':
                    password_arr.append(password[i + 1 - 7 * multi: i + 1: multi])
                else:
                    break

            real_password = []
            for p in password_arr[::-1]:
                if DAT.get(int(p, 2)) or DAT.get(int(p, 2)) == 0:
                    real_password.append(DAT.get(int(p, 2)))

            if len(real_password) == 8:
                password = password[:len(password) - 56 * multi].rstrip('0')
                if real_password in real_passwords:
                    pass
                else:
                    real_passwords.append(real_password)
                multi = 0
            multi += 1

    for real in real_passwords:
        is_valid = 0
        ans = 0
        for i in range(len(real)):
            if i % 2:
                is_valid += real[i]
            else:
                is_valid += real[i] * 3
            ans += real[i]

        if is_valid % 10 != 0:
            ans = 0

        result += ans
    print(f'#{test_case} {result}')