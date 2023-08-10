def dfs(start):
    stack = []
    visited = [False] * (N+1)
    stack.append(start)
    while stack:
        v = stack.pop()
        if not visited[v]:
            print(v)
            visited[v] = True
        for w in G[v]:
            if not visited[w]:
                stack.append(w)


def dfs1(start):
    stack = []
    visited = [False] * (N+1)
    stack.append(start)
    visited[start] = True
    while stack:
        v = stack.pop()
        print(v)
        for w in G[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True
                # print(w)

N = 7
S = '1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7'    # 논리적인 비선형 자료 구조
lst = list(map(int, S.split(', ')))
# print(lst)
# E = 0                             # 방법 1
# for idx in range(E):
#     v1 = lst[idx*2]
#     v2 = lst[idx*2 + 1]
G = [[] for _ in range(N+1)]    # 곱하기 * 사용하지 않기
for idx in range(0, len(lst), 2):   # 방법 2
    v1 = lst[idx]
    v2 = lst[idx+1]
    G[v1].append(v2)
    G[v2].append(v1)

# print(G)
dfs(1)
print('--------')
dfs1(1)
# G = [
#     [],
#     [2, 3],
#     [1, 4, 5],
#     [1, 7],
#     [2, 6],
#     [2, 6],
#     [4, 5, 7],
#     [3, 6]
# ]

# 재귀함수 사용

N = 7
visited = [False] * (N+1)


def dfs3(v):
    print(v)
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            dfs(w)