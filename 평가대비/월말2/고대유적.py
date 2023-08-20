import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    len_max = 0
    for r in range(N):
        len_r = 1
        for c in range(M-1):
            if arr[r][c] == 1 and arr[r][c+1] == 1:
                len_r += 1
        if len_max < len_r:
            len_max = len_r

    for c in range(M):
        len_c = 1
        for r in range(N-1):
            if arr[r][c] == 1 and arr[r+1][c] == 1:
                len_c += 1
        if len_max < len_c:
            len_max = len_c

    print(f'#{tc} {len_max}')
