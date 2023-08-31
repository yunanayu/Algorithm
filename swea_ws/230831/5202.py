# 화물 도크
import sys
sys.stdin = open('5202.txt','r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    for _ in range(N):
        s, e = map(int,input().split())