# 파리퇴치3

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    cur_max = 0
    for r in range(N):
        for c in range(N):
            s = arr[r][c]
            for m in range(1, M):
                for k in range(4):
                    ni, nj = r+dr[k]*m, c+dc[k]*m
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
                if cur_max < s:
                    cur_max = s
    dr1 = [-1, -1, 1, 1]
    dc1 = [-1, 1, 1, -1]
    for r in range(N):
        for c in range(N):
            s1 = arr[r][c]
            for m in range(1, M):
                for k in range(4):
                    ni, nj = r+dr1[k]*m, c+dc1[k]*m
                    if 0 <= ni < N and 0 <= nj < N:
                        s1 += arr[ni][nj]
                if cur_max < s1:
                    cur_max = s1
    print(f'#{tc} {cur_max}')