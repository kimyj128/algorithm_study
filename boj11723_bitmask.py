import sys
T = int(sys.stdin.readline())
S = 0

for _ in range(T):
    command = sys.stdin.readline().split()
    if command[0] == 'all':
        S = (1 << 21) - 1
    elif command[0] == 'empty':
        S = 0
    else:
        num = int(command[1])
        if command[0] == 'add':
            S = S | (1 << num)
        elif command[0] == 'remove':
            S = S & ~(1 << num)
        elif command[0] == 'check':
            if S & (1 << num):
                print(1)
            else:
                print(0)
        elif command[0] == 'toggle':
            S = S ^ (1 << num)
