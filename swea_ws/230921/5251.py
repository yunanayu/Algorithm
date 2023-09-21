# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리
import sys
sys.stdin = open('5251.txt','r')
import heapq

def dijk(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]
            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e,w])
    INF = int(1e9)
    distance = [INF] * (N+1)
    dijk(0)
    print(f'#{tc}',distance[-1])
