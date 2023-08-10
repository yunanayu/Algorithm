# 그래프 경로

def dfs(start, G):
    ST = []
    visited = [False] * (V+1)
    ST.append(start)
    while ST:
        v = ST.pop()
        if not visited[v]:
            visited[v] = True
        for w in lst[v]:
            if not visited[w]:
                ST.append(w)
    if visited[start] and visited[G]:
        return 1
    else:
        return 0


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

    print(f'#{tc} {dfs(S, G)}')

'''
6 5   V , E

1 4     1
1 3     2   
2 3     3
2 5     4
4 6     5

1 6   S, G

1
6 5  
1 4  
1 3    
2 3   
2 5   
4 6  
1 6

'''
'''
3
------------
6 5
----
1 4
1 3
2 3
2 5
4 6
-----
1 6
---------------------
7 4
-----
1 6
2 3
2 6
3 5
-----
2 5
--------------------------
9 9
------
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
------
1 9
------------------------------
'''