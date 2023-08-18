# 노드의 거리
def bfs(S, G):
    Q = []
    visited = [0] * (V+1)
    Q.append(S)
    visited[S] = 1
    while Q:
        v = Q.pop(0)
        for w in arr[v]:
            if not visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1
    return visited[G]


TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for n in range(len(nums)):
        v1 = nums[n][0]
        v2 = nums[n][1]
        arr[v1].append(v2)
        arr[v2].append(v1)

    print(bfs(S, G))