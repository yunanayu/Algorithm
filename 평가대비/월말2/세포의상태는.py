import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    ans = 0

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                for k in range(4):
                    nr, nc = r+dr[k], c+dc[k]
                    if 0<=nr<N and 0<=nc<M:
                        if arr[nr][nc] == 1:
                            ans += 1

    if ans != 0:
        print(f'#{tc}', '0')
    else:
        print(f'#{tc}', '1')