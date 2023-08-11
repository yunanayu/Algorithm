# 스도쿠 검증


TC = int(input())

for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1     # 정답이면 1 아니면  0
    for r in range(9):
        search = [0] * 10
        search[0] = 1
        for c in range(9):
            search[arr[r][c]] += 1
        for s in search:
            if s != 1:
                ans = 0
    for r in range(9):
        search = [0] * 10
        search[0] = 1
        for c in range(9):
            search[arr[c][r]] += 1
        for s in search:
            if s != 1:
                ans = 0
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            search = [0] * 10
            search[0] = 1
            for r in range(i, i+3):
                for c in range(j, j+3):
                    search[arr[r][c]] += 1
            for s in search:
                if s != 1:
                    ans = 0
    print(f'#{tc} {ans}')

