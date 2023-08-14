# 미로

def dfs(r,c):
    visited = [[False] * N for _ in range(N)] # 이차원 배열로 만들기
    ST = []
    ST.append((r,c))
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while ST:
        vr, vc = ST.pop()

        for k in range(4):
            newR = r+dr[k]
            newC = c+dc[k]
            if 0 <= newR < N and 0 <= newC < N and arr[newR][newC] == 0 and not visited[newR][newC]:
                ST.append((newR, newC))
                visited[newR][newC] = True


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r = i
                c = j