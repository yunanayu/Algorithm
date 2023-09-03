# 정사각형 방 # bfs 재귀 사용
import sys
sys.stdin = open('1861.txt','r')
def dfs(i, j, value):
    t = 0
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and value+1 == arr[ni][nj]:
            t = dfs(ni, nj, value+1)
    return t+1

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    maxC = 0
    for r in range(N):
        for c in range(N):
            cnt = dfs(r, c, arr[r][c])
            if cnt > maxC:
                maxC = cnt
    print(maxC)