def dfs():
    ST = []



TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    lst = [[] for _ in range(V + 1)]
    for i in range(len(arr)):
        v1 = arr[i][0]
        v2 = arr[i][1]
        lst[v1].append(v2)
        lst[v2].append(v1)