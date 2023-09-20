# DFS


# stack 버전
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]


def dfs_stack(start):
    ST = [start]
    visited = []

    while ST:
        now = ST.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문표시
        visited.append(now)

        # 갈 수 있는곳들을 ST에 추가
        # for next in range(5):
        # 작은 번호부터 조회
        for next in range(4, -1, -1):
            # 연결이 안되어있다면 continue
            if graph[now][next] == 0:
                continue

            # 방문한 지점이라면 ST에 추가하지 않음
            if next in visited:
                continue

            ST.append(next)
    # 출력을 위한 반환
    return visited


# print(dfs_stack(0))     # [0, 1, 2, 3, 4]




# DFS 재귀

# MAP 크기(길이)를 알 때 append 형식 말고 아래와 같이 사용하면 훨씬 빠르다
visited = [0] * 5
path = []   # 방문 순서 기록


def dfs(now):
    visited[now] = 1 # 현재 지점 방문 표시
    print(now, end=' ')

    # 인접한 노드들을 방문
    for next in range(5):
        if graph[now][next] == 0:
            continue
        if visited[next]:
            continue


        dfs(next)

dfs(0)  #0 1 2 3 4
# print(dfs(0))
    # 기저 조건

    # 들어가기 전
    # 함수호출
    # 돌아와서
