# 원 안의 점
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    cnt = 0
    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if (x*x + y*y) <= N*N:
                cnt += 1
    print(f'#{tc} {cnt}')