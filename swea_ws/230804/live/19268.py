# 풍선팡2
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]   # 그림그려서 확인해보기
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0   #
    for i in range(N):  # 크기정보가 주어지면 그 정보 활용하기
        for j in range(M):
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
            for k in range(4):  # i, j 인접에 대해
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < M: # 행과 열의 크기가 다를 수 있으니 조심
                    cnt += arr[ni][nj]
            if max_v < cnt: # i, j 인접 풍선까지 더하고 나면 비교하기 # i,j 를 중심으로 풍선을 다 터트린 후 최대치인지 확인하기!! 들여쓰기 확인!
                max_v = cnt
    print(f'#{tc} {max_v}')     # 모든 위치에서 확인이 끝나면 답 출력