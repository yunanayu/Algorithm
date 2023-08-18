# 미로의 거리
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
