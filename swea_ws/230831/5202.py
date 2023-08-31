# 화물 도크
import sys
sys.stdin = open('5202.txt','r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # print(lst)
    lst.sort(key=lambda x:x[1])
    # print(lst)
    lst = [[0,0]] + lst
    # print(lst)
    cnt = 0
    j = 0
    for i in range(1, N+1):
        if lst[i][0] >= lst[j][1]:  # si >= fj
            cnt += 1
            j = i

    print(f'#{tc} {cnt}')