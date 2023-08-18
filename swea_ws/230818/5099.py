# [S/W 문제해결 기본] 7일차 - 미로1
import sys
sys.stdin = open('input.txt', 'r')

def find(sr, sc):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [[False] * 16 for _ in range(16)]
    Q = []
    Q.append((sr, sc))
    while Q:
        r, c = Q.pop()
        if not visited[r][c]:
            visited[r][c] = True
            for k in range(4):
                nr, nc = r+dr[k], c+dc[k]
                if 0 <= nr < 16 and 0 <= nc < 16:
                    if nr == 13 and nc == 13:
                        return 1
                    elif arr[nr][nc] == 0 and not visited[nr][nc]:
                        Q.append((nr, nc))
    return 0




for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    # print(arr)
    print(f'#{tc}', find(1, 1))
