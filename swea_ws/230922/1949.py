# 등산로

def solve(r, c, curV, cnt, isCut):
    global maxC
    for dr, dc in ((1,0), (-1,0),(0,1),(0,-1)):
        nr = r+dr
        nc = c+dc
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            if curV > arr[nr][nc]:
                visited[nr][nc] = 1
                solve(nr,nc,arr[nr][nc], cnt+1, isCut)
                visited[nr][nc] = 0

            elif not isCut and curV > arr[nr][nc]-K:
                visited[nr][nc] = 1
                solve(nr,nc,curV-1, cnt+1, True)
                visited[nr][nc] = 0

        if maxC < cnt:
            maxC = cnt


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    maxC = 0
    highest = max(map(max, arr))
    for r in range(N):
        for c in range(N):
            if arr[r][c] == highest:
                visited[r][c] = 1
                # row, col , 현재의 값, 경로길이, 공사여부
                solve(r, c, arr[r][c], 0, False)
                visited[r][c] = 0
    print(f'#{tc}', maxC+1)