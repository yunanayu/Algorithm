# 부분수열의 합
import sys
sys.stdin = open('2817.txt','r')


def ncr(n, r, s):
    global cnt
    if r == 0:
        sumV = sum(comb)
        if sumV == K:
            cnt += 1
    else:
        for i in range(s, n - r + 1):
            comb[r - 1] = A[i]
            ncr(n, r - 1, i + 1)

TC= int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for R in range(1,N+1):
        comb = [0] * R
        ncr(N, R, 0)
    print(f'#{tc} {cnt}')