def bfs(N,M):

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    Q = []
    visited = [[0] * M for _ in range(N)]
    Q.append((0, 0))
    visited[0][0] = 1

    while Q:
        r, c = Q.pop(0)
        if r == N-1 and c == M-1:
            return visited[r][c]
        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                Q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(bfs(N,M))

