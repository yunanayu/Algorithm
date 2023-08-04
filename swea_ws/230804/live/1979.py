# 어디에 단어가 들어갈 수 있을까

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())    # N: 가로, 세로 길이 K: 단어의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0     # 단어가 들어갈 수 있는 자리의 수
    for i in range(N):  # 행 우선 순회
        cnt = 0         # 연속한 빈칸(1)의 개수
        for j in range(N):
            # 0을 만나거나 마지막 인덱스를 만나면 카운트와 단어의 길이 비교하기
            if arr[i][j]:
                cnt += 1
            if j == N-1 or arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
    print(ans)

    # 열우선순회로 바꾸기!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # cnt += 1
        # if cnt == K


