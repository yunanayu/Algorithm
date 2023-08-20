import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r, c = map(int, input().split())
    arr[r][c] = 1

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    ans = 0

    for r in range(N):
        for c in range(N):
            cnt = 0
            if arr[r][c] == 2:
                for k in range(4):
                    nr, nc = r+dr[k], c+dc[k]
                    if arr[nr][nc] == 1:
                        cnt += 1
            if cnt == 4:
                ans += 1
    print(f'#{tc} {ans}')