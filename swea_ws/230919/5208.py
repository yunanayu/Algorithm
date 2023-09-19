# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
import sys
sys.stdin = open('input1.txt','r')


def solve(k, cnt, remain):
    global minC
    if k>=M[0] :  # k 가 종점이면
        if minC > cnt:
            minC = cnt
        return

    # k지점에서 충전 여부
    if remain > 0:
        solve(k+1, cnt, remain-1)   # 충전안한경우
    solve(k+1, cnt+1, M[k]-1)   # 충전한경우



T = int(input())
for tc in range(1, T+1):
    N, *M = map(int, input().split())
    minC = M[0]
    solve(1, 0, M[1])
    print(f'{tc}', minC)