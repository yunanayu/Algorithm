graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

def bfs(start):
    visited = [0] * 5

    # 먼저 방문 했던 것을 먼저 처리해야한다. = queue
    queue = [start]
    visited[start] = 1

    while queue:
        # queue 의 맨 앞 요소를 꺼냄
        now = queue.pop(0)
        print(now, end=' ')

        # 인접한 노드들을 queue에 추가
        for next in range(5):
            # 연결이 안되어있다면 continue
            if graph[now][next] == 0:
                continue

            # 방문한 지점이라면 ST에 추가하지 않음
            if  visited[next]:
                continue

            queue.append(next)
            # bfs 이므로 여기서 방문체크를 해도 상관 없다
            visited[next] = 1


bfs(0) # 0 1 3 2 4