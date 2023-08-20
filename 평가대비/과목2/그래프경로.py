def dfs(S, G):
    ST = []
    visited = [False] * (V+1)
    ST.append(S)
    while ST:
        v = ST.pop()
        if not visited[v]:
            visited[v] = True
        for w in lst[v]:
            if not visited[w]:
                ST.append(w)
    if visited[S] and visited[G]:
        return 1
    else:
        return 0


TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    lst = [[] for _ in range(V+1)]
    for r in range(len(arr)):
        v1 = arr[r][0]
        v2 = arr[r][1]
        lst[v1].append(v2)
    print(dfs(S, G))