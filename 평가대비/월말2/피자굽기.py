def bfs():
    Q = []
    no = 1
    for _ in range(N):
        che = C.pop(0)
        Q.append((no,che))
        no += 1
    return Q


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    print(bfs())