# 창용마을 무리의 개수
import sys
sys.stdin = open('input.txt','r')

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    group = []
    for _ in range(M):
        v1, v2 = map(int, input().split())
        union(v1, v2)
    for i in range(1, N+1):
        group.append(find(i))
    print(f'#{tc}', len(set(group)))