# 부분수열의 합
import sys
sys.stdin = open('2817.txt','r')

def ncr(k):
    global cnt
    if k == N:



TC = int(input())
for tc in range(1, TC + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0


def f(k, curr_sum):
    global cnt
    if k == N:
        if curr_sum == M:
            cnt += 1
        return

    if curr_sum > M:
        return

    if curr_sum == M:
        cnt += 1
        return

    f(k + 1, curr_sum + lst[k])
    f(k + 1, curr_sum)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    f(0, 0)
    print(f'#{tc} {cnt}')