# 부분수열의 합 # 백트래킹 사용 x
'''
1
4 3
1 2 1 2
'''
def f(i,N,s,K):
    global cnt
    if i == N:
        if s == K:
            cnt += 1
    else:
        f(i+1, N, s+arr[i], K)
        f(i+1, N, s, K)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    f(0, N, 0, K)
    print(f'#{tc} {cnt}')