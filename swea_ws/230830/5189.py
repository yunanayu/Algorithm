# 전자카트
def perm(k):
    global minV
    if k == N:
        # print(bits)
        sumV = 0
        for i in range(N-1):
            start = bits[i]
            end = bits[i+1]
            sumV += arr[start-1][end-1]
        sumV += arr[end-1][0]
        if minV > sumV:
            minV = sumV
        # print(sumV)
        return
    for i in range(1, N+1):
        if not used[i]:
            bits[k] = i     # k 번째 값에 답을 덮어쓰고 있기 때문에 원복 필요 없음
            used[i] = True
            perm(k+1)
            used[i] = False     #



TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 100000000
    bits = [1] * N
    used = [False] * (N + 1)
    bits[0] = 1
    used[1] = True
    perm(1)
    print(f'#{tc} {minV}')