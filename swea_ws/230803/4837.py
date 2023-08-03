# 부분집합의 합
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())  # N = 원소의 수, K = 부분집합의 합

    cnt = 0  # 해당하는 부분집합의 수
    for i in range(1 << 12):
        s = 0
        ab = 0
        for j in range(12):
            if i & (1<<j):
                ab += 1
                s += A[j]
        if ab == N and s == K:
            cnt += 1

    print(f'#{tc} {cnt}')