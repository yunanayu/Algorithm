'''
V E
v1 w1 v2 w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# 경로 순서 탐색 가능

def dfs(n, v, arr):
    stack = []               # stack 생성
    visited = [0] * (v+1)    # visited 생성
    visited[n] = 1           # 시작점 방문 표시
    print(n)                 # do[n] # 정점에서 할 일
    while True:
        for w in range(1, v+1):        # 현재 정점 n에 인접하고 미방문 w 찾기
            if arr[n][w] == 1 and visited[w] == 0:    # 현재 정점 n에 인접하고 미방문 w 찾기
                stack.append(n)    # push(v), v = w
                n = w
                print(n)           # do(w)
                visited[n] = 1     # w 방문 표시
                break              # for w, n 에 인접인 w, c 찾은 경우
        else:                       # 미방문 w 가 없다면
            if stack:              # 스택에 지나온 정점이 남아있으면
                n = stack.pop()    # pop() 해서 다시 다른 w 찾을 n 준비
            else:       # 스택이 비어있으면
                break   # While True 탐색 끝


V, E = map(int, input().split())    # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1
print(adj_m)

# dfs(1, V, adj_m)
