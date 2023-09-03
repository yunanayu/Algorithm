# 부분수열의 합 # 백트래킹 사용 o
'''
1
4 3
1 2 1 2
'''
def f(i,N,s,K, rs):
    global cnt
    if i == N:
        if s == K:
            cnt += 1
    elif s>K:
        return
    elif s+rs < K:
        return
    else:
        f(i+1, N, s+arr[i], K, rs-arr[i])
        f(i+1, N, s, K, rs-arr[i])

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    f(0, N, 0, K, sum(arr))
    print(f'#{tc} {cnt}')