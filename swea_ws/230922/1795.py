# 인수의 생일파티
import sys
sys.stdin = open('input1.txt','r')
import heapq


def dijk(s, G):
    U = []
    D = [int(1e9)] * (N+1)
    D[s] = 0

    for _ in range(N+1):
        minV = 1000000000
        for i in range(N+1):
            if i in U:
                continue
            if D[i] < minV:
                minV = D[i]
                curN = i

        U.append(curN)

        for i in range(N+1):
            if G[curN][i] == 0:
                continue

            if D[i] > D[curN] + G[curN][i]:
                D[i] = D[curN] + G[curN][i]
    # print(U)
    # print(D)

    return D




T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    G = [[0] * (N+1) for _ in range(N+1)]
    O = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, z = map(int, input().split())
        G[x][y] = z
        O[y][x] = z

    result1 = dijk(X, G)
    result2 = dijk(X, O)
    sum_max = 0
    for i in range(1, N+1):
        if sum_max < result1[i] + result2[i]:
            sum_max = result1[i] + result2[i]
    print(f'#{tc}',sum_max)
    # print(f'2', result2)
    # print(f'1', result1)
