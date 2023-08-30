# 전자카트
def perm(k, sumV):
    global minV
    if minV < sumV:
        return
    if k == N:
        end = bits[-1]
        sumV += arr[end-1][0]

        if minV > sumV:
            minV = sumV
        # print(sumV)
        return
    for i in range(1, N+1):
        if not used[i]:
            bits[k] = i     # k 번째 값에 답을 덮어쓰고 있기 때문에 원복 필요 없음
            used[i] = True
            # start = bits[k-1]
            # end = bits[k]
            # perm(k+1, sumV+arr[start-1][end-1])
            perm(k+1, sumV + arr[bits[k-1]-1][i-1])
            used[i] = False



TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 100000000
    bits = [1] * N
    used = [False] * (N + 1)
    bits[0] = 1
    used[1] = True
    perm(1, 0)
    print(f'#{tc} {minV}')