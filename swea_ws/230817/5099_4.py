import sys
sys.stdin = open("input.txt", "r")



# def bfs():
#     Q = []
#     no = 1
#     for _ in range(N):
#         c = C.pop(0)
#         Q.append((no, c))


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    Q = []
    no = 1
    for _ in range(N):
        c = C.pop(0)
        Q.append((no, c))
        no += 1
    while Q:
