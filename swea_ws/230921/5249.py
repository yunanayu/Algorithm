import sys
sys.stdin = open('5251.txt','r')

import heapq
# 데이터를 가장 큰 값 or 가장 작은값부터 뽑아서 써야한다고 할 때 사용
def prim(start):
    heap = []
    sum_weight = 0
    # MST에 포함되었는지 여부
    MST = [0] * (V+1)

    #가중치,정점 정보
    heapq.heappush(heap, (0, start))

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)
        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue

        # 방문체크
        MST[v] = 1

        # 누적 합
        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))
    return sum_weight



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접 행렬
    graph = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        f, t, w = map(int, input().split())
        graph[f][t] = w
        graph[t][f] = w

    print(graph)
    # result = prim(0)
    # print(result)