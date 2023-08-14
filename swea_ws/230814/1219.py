# 길찾기

def dfs(start):
    visited = [False] * N
    ST = []
    ST.append(start)
    visited(start) = True
    while ST:
        v = ST.pop()
        if v == 99:
            return 1
        for w in G[v]:
            if not visited[w]:
                ST.append()
                visited[w] = True

TC, N = map(int, input().split())