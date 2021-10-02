# 최대 상금
# greedy

T = int(input())

for test_case in range(1, 1 + T):
    datas = input().split()
    nums = []
    cards = [0] * 10
    trade = int(datas[1])

    for num in datas[0]:
        tmp = int(num)
        nums.append(tmp)
        cards[tmp] += 1

    i = 9
    now = 0
    while trade and i > 0:
        i_trade = min(cards[i], trade)

        tmp = []
        tmp2 = nums[now: now + i_trade]
        tmp2 = sorted(tmp2)
        k = 0
        for n in range(len(nums) - 1, now - 1, -1):
            if nums[n] == i:
                tmp.append(n)
                k += 1
                if k == i_trade:
                    break

        k = 0
        for j in tmp:
            nums[j] = tmp2[k]
            if tmp2[k] == i:
                trade += 1
            k += 1

        for n in range(now, now + i_trade):
            nums[n] = i

        trade -= i_trade
        now += cards[i]
        i -= 1

    if trade % 2 and max(cards) == 1:
        nums[-1], nums[-2] = nums[-2], nums[-1]

    print(f'#{test_case}', end=' ')
    for num in nums:
        print(num, end='')
    print('')