import sys
sys.stdin = open("input.txt", "r")

def bfs(i,j):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    Q = []
    visited = [[False]*100 for _ in range(100)]
    Q.append((i, j))
    while Q:
        r, c = Q.pop(0)
        if not visited[r][c]:
            visited[r][c] = True
        for k in range(4):
            nr, nc = r+dr[k] , c+dc[k]
            if 0<=nr<100 and 0<= nc < 100:
                if arr[nr][nc] == 3:
                    return 1
                elif arr[nr][nc] != 1 and not visited[nr][nc]:
                    Q.append((nr,nc))

    return 0

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    print(f'#{tc} {bfs(1,1)}')
