# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
# import sys
# sys.stdin = open('input.txt', 'r')


def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])

    # 경로 압축
    # parent[x] = find_set(parent[x])
    # return parent[x]


def union(x,y):
    x = find_set(x)
    y = find_set(y)
    # 1. 이미 같은 집합인 지 체크
    # 대표자가 같으니 같은 집합이다.
    if x == y:
        return
    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    # print(parent)
    for i in range(0, len(lst)-1, 2):
        # x = 2*i
        # y = 2*i+1
        # print(lst[i],lst[i+1])
        union(lst[i], lst[i+1])

    # print(parent)
    ans = []
    for i in range(1, N+1):
        n = find_set(i)
        ans.append(n)
    ans = set(ans)
    # print(ans)
    print(f'#{tc}', len(ans))
    print('------')