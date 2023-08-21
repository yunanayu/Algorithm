import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    Q = []
    no = 1
    for _ in range(N):
        Q.append([no, C.pop(0)])
        no += 1
    print(Q)
    while Q:
        n, c = Q.pop()
        c = c // 2
        if c != 0:
            Q.append([n,c])
        else:
            Q.append([no, C.pop(0)])
            no += 1
    print(n)