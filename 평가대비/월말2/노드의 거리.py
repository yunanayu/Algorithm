import sys
sys.stdin = open("input.txt", "r")


def bfs(S, G):
    Q = []
    visited = [0] * (V+1)
    Q.append(S)
    visited[S] = 1
    while Q:
        v = Q.pop(0)
        if v == G:
            return visited[v] - 1
        for w in lst[v]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1

    return 0

TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    # print(lst)
    for i in range(E):
        v1 = arr[i][0]
        v2 = arr[i][1]
        lst[v1].append(v2)
        lst[v2].append(v1)
    print(bfs(S,G))