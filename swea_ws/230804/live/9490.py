# 풍선팡

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]   # 그림그려서 확인해보기
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0   #
    for i in range(N):  # 크기정보가 주어지면 그 정보 활용하기
        for j in range(M):
            cnt = arr[i][j]     # 터트린 풍선의 꽃가루 수
            for k in range(4):  # i, j 인접에 대해
                for p in range(1, arr[i][j]+1):   # 필요한 칸 수 만큼 곱해지는 수 # +1???? 확인해보기
                    ni, nj = i+di[k]*p, j+dj[k]*p
                    if 0 <= ni < N and 0 <= nj < M:     # 인덱스 범위 넘어가는지 확인
                        cnt += arr[ni][nj]      # 주변 칸 풍선의 꽃가루 수 합산
            if max_v < cnt:     # arr[i][j] 와 주변을 확인 한 후 값 비교
                max_v = cnt
    print(f'#{tc} {max_v}')