# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
import sys
sys.stdin = open('input.txt','r')

def dfs(start):
    pass


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    # print(lst)
    graph = [[] for _ in range(N+1)]
    # print(graph)
    visited = [False] * (N+1)
    cnt = 0
    # for m in range(M):

