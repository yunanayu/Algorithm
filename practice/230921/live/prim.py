'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
import heapq
# 데이터를 가장 큰 값 or 가장 작은값부터 뽑아서 써야한다고 할 때 사용
def prim(start):
    heap = []
    sum_weight = 0
    # MST에 포함되었는지 여부
    MST = [0] * V

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

V, E = map(int, input().split())

# 인접 행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w



result = prim(0)
print(result)
# 인접 리스트



# import heapq
# # 데이터를 가장 큰 값 or 가장 작은값부터 뽑아서 써야한다고 할 때 사용
# def prim(start):
#     heap = []
#     heapq.heappush(heap, 3)
#     heapq.heappush(heap, 1)
#     heapq.heappush(heap, 2)
#     # 내림차순은 음수로
#     print(heapq.heappop(heap))
#     print(heapq.heappop(heap))
#     print(heapq.heappop(heap))
#
# prim(0)
