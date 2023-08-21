def bfs(s):
    Q = []
    visited = [False] * (N+1)

    Q.append(s)
    while Q:
        v = Q.pop(0)
        print(v)
        # if not visited[v]:
        #     print(v)
        #     visited[v] = True

        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = True

def dfs(s):
    ST = []
    visited = [False] * (N+1)

    ST.append(s)
    while ST:
        v = ST.pop()
        if not visited[v]:
            visited[v] = True
            print(v)
            for w in G[v]:
                if not visited[w]:
                    ST.append(w)


s = '1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7'
lst = list(map(int, s.split(', ')))
print(lst)
N = 7
G = [[] * (N+1) for _ in range(N+1)]
# print(G)
for i in range(0, len(lst), 2):
    v1 = lst[i]
    v2 = lst[i+1]
    G[v1].append(v2)
    G[v2].append(v1)
# print(G)

bfs(4)
print('----------------------')
dfs(4)