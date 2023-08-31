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