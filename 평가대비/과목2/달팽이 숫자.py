TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    d = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = c = 0
    for n in range(1, N*N+1):
        arr[r][c] = n
        new_r = r + dr[d]
        new_c = c + dc[d]
        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= 0 or arr[new_r][new_c] != 0:
            d = (d + 1) % 4
        r += dr[d]
        c += dc[d]
    print(f'{tc}')
    for i in range(N):
        print(*arr[i])