# 몇 개의 돌을 잡을 수 있을까요

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    R, C = map(int, input().split())
    arr[R][C] = 1

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    ans = 0
    for r in range(N):
        for c in range(N):
            cnt = 0
            if arr[r][c] == 2:
                for k in range(4):
                    ni, nj = r + dr[k], c + dc[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 1:
                            cnt += 1
                if cnt == 4:
                    ans += 1

    print(f'#{tc} {ans}')



# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     R, C = map(int, input().split())
#     # arr[R][C] = 1
#
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#
#     ans = 0
#     for r in range(N):
#         for c in range(N):
#             arr[r][c] = 1
#             for i in range(N):
#                 for j in range(N):
#                     cnt = 0
#                     if arr[i][j] == 2:
#                         for k in range(4):
#                             ni, nj = i+dr[k], j+dc[k]
#                             if 0 <= ni < N and 0 <= nj < N:
#                                 if arr[ni][nj] == 1:
#                                     cnt += 1
#                         if cnt == 4:
#                             ans += 1
#
#     print(f'#{tc} {ans}')
