# 입력받은 자료(tree구조)
tree = [0] * 200
tree[0] = [30]
tree[30] = [54, 2, 45]
tree[54] = [1]
tree[1] = [99, 98]
tree[45] = [123]
tree[99] = [124]
tree[124] = [125]
tree[125] = [126, 127]

# 출력할 자료
ans = [['          '] * 10 for _ in range(10)]

# 몇 번째 줄에 출력해야하는지 정해줄 변수 th
th = 0


def dfs(now, i):
 global th
 # 이어지는 가지가 없으면 종료
 if tree[now] == 0:
     return

 # 이어지는 가지가 있는경우 실행
 ans[th][i] = ''
 # 출력 방식을 맞추기위해 조금 복잡합니다.
 # 가지가 1개인 경우
 # -----사용
 if len(tree[now]) == 1:
     ans[th][i] += '-----'
     if tree[now][0] // 10 == 0:
         ans[th][i] += f'[00{tree[now][0]}]'
     elif tree[now][0] // 100 == 0:
         ans[th][i] += f'[0{tree[now][0]}]'
     else:
         ans[th][i] += f'[{tree[now][0]}]'
     dfs(tree[now][0], i + 1)
 # 가지가 여러개인경우
 # 상황에 맞춰 +, L사용
 else:
     for branch in tree[now]:
         if branch == tree[now][0]:
             ans[th][i] = '--'
         else:
             ans[th][i] = '  '
         if branch == tree[now][-1]:
             ans[th][i] += 'L--'
             if branch // 10 == 0:
                 ans[th][i] += f'[00{branch}]'
             elif branch // 100 == 0:
                 ans[th][i] += f'[0{branch}]'
             else:
                 ans[th][i] += f'[{branch}]'
         else:
             ans[th][i] += '+--'
             if branch // 10 == 0:
                 ans[th][i] += f'[00{branch}]'
             elif branch // 100 == 0:
                 ans[th][i] += f'[0{branch}]'
             else:
                 ans[th][i] += f'[{branch}]'
         # 하나의 자식을 처리하고 다음 대상으로 재귀
         dfs(branch, i + 1)
         # 가지개수에 따라 몇 번째 줄인지 결정
         th += 1
     # 가지개수 -1 만큼만 늘어납니다
     th -= 1


# main
dfs(0, 0)

# 출력 방식 조정
for i in range(9):
 for j in range(10):
     if ans[i][j][2] == '+' or ans[i][j][2] == '|':
         if ans[i+1][j] == '          ':
             ans[i+1][j] = '  |       '

# 출력
for i in range(10):
 tmp = ''
 for j in range(10):
     tmp += ans[i][j]
 print(tmp)
