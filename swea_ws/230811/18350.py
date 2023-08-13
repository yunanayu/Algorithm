# 세포의 상태는

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    ans = 0
    for r in range(N):
        for c in range(M):
            cnt = 0
            if arr[r][c] == 1:
                for k in range(4):
                    ni, nj = r+dr[k], c+dc[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 1:
                            cnt += 1
                if cnt != 4:
                    ans += 1
    if ans == 0:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)