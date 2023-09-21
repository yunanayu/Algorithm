import sys
sys.stdin = open('input2.txt','r')

def dijk(s):
    U = []
    D = [10000] * N

    D[s] = 0

    for _ in range(N):
        minV = 10000
        for i in range(N):
            if i in U:
                continue
            if D[i] < minV:
                minV = D[i]
                curN = i

        U.append(curN)

        for i in range(N):
            if G[curN][i] == 0:
                continue

            if D[i] > D[curN] + G[curN][i]:
                D[i] = D[curN] + G[curN][i]

    print(U)
    print(D)

N, E = map(int, input().split())
G = [[0] * N for _ in range(N)]
for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w

dijk(0)