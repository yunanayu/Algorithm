# 단순 2진 암호코드
import sys
sys.stdin = open('input3.txt','r')



TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
