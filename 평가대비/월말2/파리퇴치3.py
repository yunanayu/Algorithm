import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    dr1 = [-1, -1, 1, 1]
    dc1 = [-1, 1, 1, -1]
    for r in range(N):
        for c in range(N):
            s1 = arr[r][c]
            s2 = arr[r][c]
            for k in range(4):
                for m in range(M):
                nr, nc = r+dr[k]
