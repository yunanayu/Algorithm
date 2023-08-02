# 풍선팡2

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)


i = [0, 1, 0, -1]
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