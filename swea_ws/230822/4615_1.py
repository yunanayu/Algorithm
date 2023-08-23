T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    BRD = [[0] * N for _ in range(N)]
    BRD[N // 2 - 1][N // 2 - 1] = 2
    BRD[N // 2][N // 2] = 2
    BRD[N // 2][N // 2 - 1] = 1
    BRD[N // 2 - 1][N // 2] = 1

    for _ in range(M):
        C, R, color = map(int, input().split())
        C -= 1
        R -= 1

        BRD[R][C] = color
        if color == 2:
            rever_c = 1
        else:
            rever_c = 2
        # rever_c = 2 if color ==1 else 1
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            newR = R + dr
            newC = C + dc

            while 0 <= newR < N and 0 <= newC < N and BRD[newR][newC] == rever_c:
                newR += dr
                newC += dc

            if 0 <= newR < N and 0 <= newC < N and BRD[newR][newC] == color:
                # while not (newR == R and newC == C):
                while newR != R or newC != C:
                    newR -= dr
                    newC -= dc
                    BRD[newR][newC] = color
    print(BRD)
    cnt1 = 0
    cnt2 = 0
    for row in BRD:
        cnt1 += row.count(1)
        cnt2 += row.count(2)

    print(f'#{tc} {cnt1} {cnt2}')
