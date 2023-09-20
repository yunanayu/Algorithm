# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(start, cnt):
    q = deque([(start, cnt)])
    while q:
        v1, c1 = q.popleft()
        c1 += 1

        for newX in [v1+1, v1-1, v1*2, v1-10]:
            if 1 < newX <= 1000000 and not used[newX]:
                if newX == M:
                    return c1
                q.append((newX, c1))
                used[newX] = True



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    used = [False] * 1000001
    print((f'#{tc} {bfs(N, 0)}'))
