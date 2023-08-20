import sys
sys.stdin = open("input.txt", "r")

# def bfs(S):
#     Q = []
#     visited = [0] * 101
#     Q.append(S)
#     visited[S] = 1
#     idx = 0
#     while Q:
#         v = Q.pop(0)
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = visited[v] + 1
#         if visited[idx] < visited[v]:
#             idx = v
#     return idx
#
#
# for tc in range(1, 11):
#     L, S = map(int,input().split())
#     lst = list(map(int, input().split()))
#
#     G = [[] for _ in range(101)]
#     for i in range(0, L, 2):
#         v1 = lst[i]
#         v2 = lst[i+1]
#         G[v1].append(v2)
#     print(bfs(S))


def bfs(S):
    Q = []
    visited = [0] * 101
    Q.append(S)
    visited[S] = 1
    idx = 0
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
    return visited


for tc in range(1, 11):
    L, S = map(int,input().split())
    lst = list(map(int, input().split()))

    G = [[] for _ in range(101)]
    for i in range(0, L, 2):
        v1 = lst[i]
        v2 = lst[i+1]
        G[v1].append(v2)
    visited = bfs(S)


    cur_max = 0
    idx = 0
    for i in range(101):
        if visited[idx] <= visited[i]:
            idx = i
    print(f'#{tc} {idx}')
