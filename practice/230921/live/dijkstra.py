'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5

'''
# 최단거리 문제 유형
'''
1. 특정지점 -> 도착 지점까지의 최단 거리 : 다익스트라
2. 가중치에 음수 포함 -> 밸만포드
3. 여러 지점 -> 여러 지점까지의 최단 거리 : 플로이드-워샬
            - 여러 지점 모두 다익스트라 돌리기 가능하지만 시간 복잡도 계산 잘해야함
'''
# 내가 갈 수 있는 경로 중 누적 거리가 제일 짧은것부터 고르자
import heapq

# 입력
N, M = map(int, input().split())
# 인접리스트
graph = [[] for i in range(N)]
for _ in range(M):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])


# 1. 누적 거리를 계속 저장
INF = int(1e9) # 최대값(1억)
distance = [INF] * N


def dijkstra(start):
    # 2. 우선순위 큐
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재시점에서서 누적 거리가 가장 은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한적이 있다면 pass
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node 로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적거리가 기존보다 크면 pass
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)
print(distance)


start = 0
