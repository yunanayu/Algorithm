di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0 # 모든 원소가 0 이상이라면
for i in range(N): # 모든 원소 arr[i][j] 에 대해
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]  #벗어나는 원소는 제외
        # for p in range(1, m):
        for di, dj in [[0, 1], [1, 0], [0, -1],[-1, 0]]: # 4방향에 대하여
            ni, nj = i + di, j + dj # ni, nj = i + di*p, j + dj * p
            if 0 <= ni < N and 0 <= nj < N: # 배열을 벗어나지 않으면
                s += arr[ni][nj]
            # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s


#------------------------------------------------------------
# 방법 1
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

r = 2
c = 1
for d in range(4):
    nr = r +dr[d]
    nc = c +dc[d]

# 방법 2
for dr, dc in [(1,  0), (-1, 0), (0, 1), (0, -1)]:
    nr = r + dr
    nc = c + dc
# 시계방향으로 진행해야 하면 in 뒤의 좌표값 자리 수정하여서 진행시켜주기