# # 미로의 거리
# def find(sr, sc):
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     visited = [[0] * N for _ in range(N)]
#     Q = []
#     Q.append((sr, sc))
#     while Q:
#         r, c = Q.pop()
#         if visited[r][c] == 0:
#             visited[r][c] = 1
#         for k in range(4):
#             nr, nc = r+dr[k], c+dc[k]
#             if 0<=nr<N and 0<=nc<N:#and arr[nr][nc] != 1 and visited[nr][nc] == 0:
#                 if arr[nr][nc] == 3:
#                     return visited[nr][nc]
#                 elif arr[nr][nc] == 0 and visited[nr][nc] == 0:
#                     Q.append((nr, nc))
#                     visited[nr][nc] = visited[r][c] + 1
#     return 0
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     for a in range(N):
#         for b in range(N):
#             if arr[a][b] == 2:
#                 i = a
#                 j = b
#
#     print(f'#{tc}', find(i,j))



# def find(sr, sc):
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     visited = [[0] * N for _ in range(N)]
#     Q = []
#     Q.append((sr, sc))
#     # visited[sr][sc] = 1
#     while Q:
#         r, c = Q.pop()
#         if arr[r][c] == 3:
#             return visited[r][c] - 1
#         for k in range(4):
#             nr, nc = r+dr[k], c+dc[k]
#             if 0<=nr<N and 0<=nc<N and arr[nr][nc] != 1 and visited[nr][nc] == 0:
#                 Q.append((nr, nc))
#                 visited[nr][nc] = visited[r][c] + 1
#     return 0
#
#
# def find_start(N):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 return i, j
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     i, j = find_start(N)
#
#     print(f'#{tc}', find(i, j))






#
#
def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)]     # visited 생성
    Q = []
    Q.append((sti, stj))        # 시작점 인큐
    visited[sti][stj] = 1       # 시작점 인큐 표시
    while Q:            # 큐가 비워질 때 까지
        i, j = Q.pop()          # 디큐
        if maze[i][j] == 3:     # 처리
            return visited[i][j] - 2    # 지나온 칸 수 return
        for di, dj in [[0,1], [1,0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')
