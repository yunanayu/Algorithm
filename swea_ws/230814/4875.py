# 미로

def dfs(r,c):
    visited = [[False] * N for _ in range(N)]
    ST = []
    ST.append((r, c))
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while ST:
        vr, vc = ST.pop()
        if not visited[vr][vc]:
            visited[vr][vc] = True
        for k in range(4):
            nr, nc = vr+dr[k], vc+dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 3:
                    return 1
                elif arr[nr][nc] == 0 and not visited[nr][nc]:
                    ST.append((nr, nc))
                    visited[nr][nc] = True
    return 0


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r = i
                c = j

    print(f'#{tc} {dfs(r, c)}')


#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 3:
#                 r1 = i
#                 c1 = j
#
#
# def dfs(r,c):
#     visited = [[False] * N for _ in range(N)]
#     ST = []
#     ST.append((r, c))
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     while ST:
#         vr, vc = ST.pop()
#         if not visited[vr][vc]:
#             visited[vr][vc] = True
#         for k in range(4):
#             nr, nc = vr+dr[k], vc+dc[k]
#             if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
#                 if arr[nr][nc] == 0 or arr[nr][nc] == 3:
#                     ST.append((nr, nc))
#                     visited[nr][nc] = True
#     #
