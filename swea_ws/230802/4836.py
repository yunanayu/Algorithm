# 색칠하기
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    color = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        if color[i][4] == 1:
            for r in range(color[i][0], color[i][2]+1):
                for c in range(color[i][1], color[i][3]+1):
                    arr[r][c] += 1
        else:
            for r in range(color[i][0], color[i][2]+1):
                for c in range(color[i][1], color[i][3]+1):
                    arr[r][c] += 2
    cnt = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')

#------------------------------------------------------------

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color
    cnt = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')

