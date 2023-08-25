# 무선충전

def getPower(posA, posB):
    alst = []
    blst = []
    for i in range(A):
        x, y, c, p = BATT[i]
        if abs(posA[0] -x) + abs(posA[1]-y) <=c:
            alst.append((i,p))
        if abs(posB[0] - x) + abs(posB[1] - y) <= c:
            blst.append((i,p))

    if alst and not blst:
        return alst[0][1]
    if blst and not alst:
        return blst[0][1]
    if alst and blst:
        # r같은경우
        if alst[0] != blst[0]:
            return alst[0][1] + blst[0][1]
        # 다른경우
        nextA = nextB = 0
        p = alst[0][1]
        if len(alst) >= 2:
            nextA = alst[1][1]
        if len(blst) >= 2:
            nextB = blst[1][1]
        return max(p, p+nextA, p+nextB)
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    moveA = list(map(int, input().split()))
    moveB = list(map(int, input().split()))

    BATT = [list(map(int, input().split())) for _ in range(A)]
    BATT.sort(reverse = True, key = lambda x:x[3])  # 각 리스트 중 가장 큰것에 저장

    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]

    posA = [1,1]
    posB = [10,10]

    result = 0
    result += getPower(posA, posB)
    for i in range(M):
        posA[0] += dx[moveA[i]]
        posA[1] += dy[moveA[i]]
        posB[0] += dx[moveB[i]]
        posB[1] += dy[moveB[i]]
        result += getPower(posA, posB)
    print(f'#{tc} {result}')
