# 동철이의 일 분배
import sys
sys.stdin = open('input4.txt','r')


def per(k, cur_ans):
    global ans
    if cur_ans < ans:
        return

    if k == N:
        ans = cur_ans
        return

    for i in range(N):
        if not visited[i]:
            if P_lst[k][i] == 0:
                continue
            else:
                visited[i] = True
                per(k+1, cur_ans*P_lst[k][i]/100)
                visited[i] = False



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P_lst = [list(map(int, input().split())) for _ in range(N)]
    # print(P_lst)
    ans = 0
    visited = [False] * N
    per(0, 1)
    print(f'#{tc} {ans*100:.6f}')