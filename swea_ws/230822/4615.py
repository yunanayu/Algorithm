TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    BRD = [[0] * N for _ in range(N)]
    BRD[N//2-1][N//2-1] = 2
    BRD[N//2][N//2] = 2
    BRD[N//2][N//2-1] = 1
    BRD[N//2-1][N//2] = 1

    for _ in range(M):
        C, R, color = map(int, input().split())
        C -= 1
        R -= 1

        BRD[R][C] = color
        revers_c = 2 if color == 1 else 1
        # if color == 2:
        #     revers_c = 1
        # else:
        #     revers_c = 2
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            newR = R + dr
            newC = C + dc

            while 0 <= newR < N and 0 <= newC < N and BRD[newR][newC] == revers_c:
                newR += dr
                newC += dc

            if 0 <= newR < N and 0 <= newC < N and BRD[newR][newC] == color:
                # while not (newR == R and newC == C):
                while newR != R or newC != C:
                    newR -= dr
                    newC -= dc
                    BRD[newR][newC] = color
    # print(BRD)
    b = 0
    w = 0
    for r in range(N):
        for c in range(N):
            if BRD[r][c] == 1:
                b += 1
            elif BRD[r][c] == 2:
                w += 1
    print(f'#{tc} {b} {w}')