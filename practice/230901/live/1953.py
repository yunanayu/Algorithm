# 탈주범 검거
# 0123 상하좌우
import sys
sys.stdin = open('1953.txt','r')

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
PIPE = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1],
        [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
OPP = [1, 0, 3, 2] # 상 <-> 하 좌<->우 d역방향

def bfs(r,c):
    visited = [[False] * M for _ in range(N)]
    Q = [(r,c,1)]       # 시작시간 = 1
    visited[r][c] = True
    while Q:
        r, c, t = Q.pop(0)
        # 시간이 L이면 끝
        if t==L:
            break
        # 4방향에 대하여
        for d in range(4):
            newR = r+DELTA[d][0]
            newC = c+DELTA[d][1]
            if 0<=newR<N and 0<=newC<M and not visited[newR][newC]:
                p1 = TUNNEL[r][c]
                p2 = TUNNEL[newR][newC]
                if PIPE[p1][d] and PIPE[p2][OPP[d]]:   # 파이프가 연결되어 있으면 역방향에 있는애가 1이면 = 연결되어있으면
                    Q.append((newR, newC, t+1))
                    visited[newR][newC] = True
    # print(visited)
    result = 0
    for rlst in visited:
        result += rlst.count(True)
    return result

TC = int(input())
# TC = 1
for tc in range(1, TC+1):
    N, M, R, C, L = map(int, input().split())
    TUNNEL = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', bfs(R,C))