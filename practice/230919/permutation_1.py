def per(k):
    if k == N:
        print(result)
        for i in range(N):
            pos = result[i]
            print(lst[pos], end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result[k] = i
            per(k+1)
            visited[i] = False


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 3
result = [-1] * N
visited = [False] * N
per(0)

# [f, False, False]
