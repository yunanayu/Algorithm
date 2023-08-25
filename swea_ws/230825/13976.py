# IM 대비 기지국

'''
#1 4
#2 4
#3 2
'''

import sys
sys.stdin = open('input.txt','r')


# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N+1)]
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     # print(arr)
#     for r in range(N+1):
#         for c in range(N):
#             if arr[r][c] == 'A':
#                 for k in range(4):
#                     # for m in range(1, M+1)
#                     nr_a, nc_a = r+dr[k], c+dc[k]
#                     if 0<=nr_a<N+1 and 0<=nc_a<N and arr[nr_a][nc_a] == 'H':
#                         arr[nr_a][nc_a] = 'O'
#             elif arr[r][c] == 'B':
#                 for k in range(4):
#                     for m in range(1, 3):
#                         nr_b, nc_b = r+dr[k]*m, c+dc[k]*m
#                         if 0<=nr_b<N+1 and 0<=nc_b<N and arr[nr_b][nc_b] == 'H':
#                             arr[nr_b][nc_b] = 'O'
#             elif arr[r][c] == 'C':
#                 for k in range(4):
#                     for m in range(1, 4):
#                         nr_c, nc_c = r+dr[k]*m, c+dc[k]*m
#                         if 0<=nr_c<N+1 and 0<=nc_c<N and arr[nr_c][nc_c] == 'H':
#                             arr[nr_c][nc_c] = 'O'
#     # print(arr)
#     cnt = 0
#     for r in range(N+1):
#         for c in range(N):
#             if arr[r][c] == 'H':
#                 cnt += 1
#     print(f'#{tc} {cnt}')




