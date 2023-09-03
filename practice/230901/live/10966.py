# 물놀이
import sys
sys.stdin = open('10966.txt','r')

from collections import deque


# def bfs(q):
#     global q
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     visited = [[1] * M for _ in range(N)]
#     # q.append((sr,sc))
#     while q:
#         vr, vc = q.popleft()
#         visited[vr][vc] += 1
#         if arr[vr][vc] == 'W':
#             return visited[vr][vc] - 2
#
#         for k in range(4):
#             nr, nc = vr + dr[k], vc + dc[k]
#             if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 'L' and visited[nr][nc] == 1:
#                 q.append((nr,nc))
#                 visited[nr][nc] += visited[vr][vc]
#

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())    # N줄 길이 M
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    sumV = 0
    q = deque()
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W':
                i, j = r, c
                q.append((i,j))
    print(q)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [[0] * M for _ in range(N)]
    # q.append((sr,sc))
    while q:
        vr, vc = q.popleft()
        sumV += visited[vr][vc]
        for k in range(4):
            nr, nc = vr + dr[k], vc + dc[k]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] += 1

    # print(sumV)