def f(k):
    global curM
    if k == N:
        # print(result_i)
        sumV = 0
        for kt in range(N):
            c = result_i[kt]
            sumV += arr[kt][c]
        if sumV < curM:
            curM = sumV

        return

    for i in range(N):
        if not used[i]:     #위에서 사용 안한경우
            used[i] = True
            result_i[k] = i
            f(k+1)
            used[i] = False

    return


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result_i = [-1] * N
    used = [False] * N
    curM = 1000
    f(0)
    print(f'#{tc}', curM)