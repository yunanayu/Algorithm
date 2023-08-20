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
            p = arr[r][c]
            for k in range(1, p+1):
                for i in range(4):
                    ni, nj = r + dr[i]*k, c+dc[i]*k
                    if 0<=ni<N and 0<=nj<M:
                        s += arr[ni][nj]
            if cur_max < s:
                cur_max = s
    print(cur_max)