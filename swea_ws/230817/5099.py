# 피자 굽기

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    no = 1
    Q = []
    for _ in range(N):
        Q.append([no, C.pop(0)])
        no += 1
    while Q:
        n, c = Q[0]
        c = c // 2
        if c == 0:
            num, che = Q.pop(0)
            if C:
                Q.append([no+1, C.pop(0)])
        else:
            Q[0] = [n, c]
    print(num)