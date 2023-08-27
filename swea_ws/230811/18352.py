# 운동장 파인곳을 찾아주세요
# def getMaxCnt(r, c):
#     cnt = 0
#     for dr, dc
#         newR =
#         newC =
#         if 범위 체크:
#             if arr[newR][newC] arr[r][c]:
#                 cnt += 1
#     return cnt
#
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N, M = map(int, input().split())
#     H = [list(map(int, input().split())) for _ in range(N)]
#     # dr = [-1, 0, 1, 0]
#     # dc = [0, 1, 0, -1]
#     for r in range(N):
#         for c in range(M):
#             if getMaxCnt(r, c) == 4:
#                 resultC += 1
#                 if resultMin > arr[r][c]:
#                     resultMin = arr[r][c]
#     print(resultMin)



TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    min_h = 1000
    ans = 0
    for r in range(N):
        for c in range(M):
            cnt = 0
            s = arr[r][c]
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]
                if 0<=nr<N and 0<=nc<M:
                    if s < arr[nr][nc]:
                        cnt += 1
            if cnt == 4:
                ans += 1
                if min_h > s:
                    min_h = s
    if ans == 0:
        print(f'#{tc}',0, -1)
    else:
        print(f'#{tc}',ans, min_h)