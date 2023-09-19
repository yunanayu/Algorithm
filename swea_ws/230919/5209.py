# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
import sys
sys.stdin = open('input.txt','r')

def per(k, curSum):
    global minV
    if curSum > minV:
        return
    if k == N:
        minV = curSum
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            per(k+1, curSum+V[k][i])
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    minV = 10000000000
    visited = [False]*N
    per(0, 0)
    print(f'#{tc}', minV)