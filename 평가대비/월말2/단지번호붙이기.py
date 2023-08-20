def bfs(r,c):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    Q = []
    visited = [[False] * N for _ in range(N)]



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
lst =[]
for r in range(N):
    for c in range(N):
        if arr[r][c]:
            lst.append(bfs(r,c))
