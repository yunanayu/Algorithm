# 활동 선택 문제
# a = [(1,4), (3,5), (1,6), (5, 7), (3,8), (5, 9), (6, 10), (8, 11), (2, 13), (12, 14)]
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]
meet = []
N = 10
for i in range(N):
    meet.append([a[i*2], a[i*2+1]])
meet.sort(key=lambda x:x[1]) #
# meet = [[0,0]] + meet # 이전활동 = 최초 활동(0번)
#
# S = [1]
# j = 1   # 마지막 선택 활동

meet = [[0,0]] + meet # 이전활동 = 최초 활동(0번)

S = []
j = 0   # 마지막 선택 활동
for i in range(1, N+1):
    if meet[i][0] >= meet[j][1]:    # si >= fj
        S.append(i)
        j = 1
print(S)