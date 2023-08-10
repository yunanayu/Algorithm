# S/W 문제해결 기본 4일차 - 길찾기
def dfs():
    ST = []
    V = [False] * 100
    ST.append(0)
    while ST:
        v = ST.pop()
        if not V[v]:
            V[v] = True
        for w in lst[v]:
            if not V[w]:
                ST.append(w)
    if V[0] and V[99]:
        return 1
    else:
        return 0


for _ in range(10):
    TC, N = map(int, input().split())
    R = list(map(int, input().split()))
    lst = [[] for _ in range(100)]
    for i in range(0, len(R), 2):
        v1 = R[i]
        v2 = R[i+1]
        lst[v1].append(v2)
    print(f'#{TC} {dfs()}')
