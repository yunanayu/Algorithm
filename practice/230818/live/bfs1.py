'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, V):      # 시작 s 마지막 v
    visited = [0] * (V+1)   # visited 생성
    Q = []      # 큐 생성
    Q.append(s) # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while Q:    # 큐에 정점이 남아있으면
        t = Q.pop(0)    # 디큐
        print(t)        # 방문한 정점에서 할 일
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점w가 있으면
            if visited[w] == 0:# w 인큐, 인큐되었음을 표시
                Q.append(w)
                visited[w] = visited[t] + 1


V, E = map(int, input().split())        # 1번부터 V번 정점, E 개의 간선
arr = list(map(int, input().split()))
# 인접리스트----------------------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우
# 여기까지 인접리스트-----------------------------------
# bfs(1,7)
print(adj_l)