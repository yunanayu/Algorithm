# [S/W 문제해결 기본] 10일차 - Contact

def bfs(start):
    visited = [1] * 101
    q = [start]
    visited[start] += 1
    while q:
        v = q.pop(0)
        for w in graph[v]:
            if visited[w] == 1:
                q.append(w)
                visited[w] += visited[v]

    # print(visited)
    return visited


for tc in range(1,11):
    L, S = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(101)]

    for i in range(0, L-1, 2):
        a = lst[i]
        b = lst[i+1]
        graph[a].append(b)

    # print(graph)

    visited = bfs(S)

    # print(visited)
    maxV = 0
    idx = 0
    for i in range(101):
        if maxV <= visited[i]:
            maxV = visited[i]
            idx = i

    print(f'#{tc}',idx)