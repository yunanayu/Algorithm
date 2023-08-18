def find(sr, sc):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [[0] * N for _ in range(N)]
    Q = []
    Q.append((sr, sc))
    visited[sr][sc] = 1
    while Q:
        r, c = Q.pop(0)
        if arr[r][c] == 3:
            return visited[r][c] - 2
        for k in range(4):
            nr= r + dr[k]
            nc =c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and visited[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return 0


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if arr[a][b] == 2:
                i = a
                j = b

    print(f'#{tc}', find(i, j))
