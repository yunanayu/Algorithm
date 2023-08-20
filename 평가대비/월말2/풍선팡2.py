import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    cur_max = 0
    for r in range(N):
        for c in range(M):
            s = arr[r][c]
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]
                if 0<=nr<N and 0<=nc<M:
                    s += arr[nr][nc]
            if cur_max < s:
                cur_max = s
    print(f'#{tc} {cur_max}')

