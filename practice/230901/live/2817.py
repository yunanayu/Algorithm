# 부분 수열의 합 # bit 사용
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0

    for i in range(1<<N):   # 부분집합을 표시하는 i
        s = 0       # 부분집합의 합
        for j in range(N):  # j번 비트
            if i &(1<<j):
                s += A[j]
        if s == K:
                cnt += 1
    print(f'#{tc} {cnt}')