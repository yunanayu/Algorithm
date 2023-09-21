def dijk(s):
    U = []  # visited
    D = [10000] * (N + 1)  # 대충 큰 수

    D[s] = 0  # 자기 자신까지의 거리니까 0
    for _ in range(N + 1):
        minV = 10000
        for i in range(N + 1):  # 아직 방문하지 않은 노드 중 최소 거리를 가지는 노드 찾기
            if i in U:  # 이미 방문 했으면 다음 노드 검사
                continue

            if minV > D[i]:  # i까지의 거리 D[i]가 더 짧다면
                minV = D[i]  # 업데이트
                curN = i  # 현재의 노드

        U.append(curN)  # 방문했으니까 U에 추가

        for i in range(N + 1):  # 현재 노드 curN을 거쳐 다른 노드로 가는 거리 계산
            if G[curN][i] == 0:
                continue
            if D[i] > D[curN] + G[curN][i]:  # curN을 거쳐 다른 노드로 가는 기존의 최단 거리보다 짧다면
                D[i] = D[curN] + G[curN][i]

        # print(U)
        # print(D)
    print(f'#{tc} {D[-1]}')


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # 끝번호, 도로 개수
    G = [[0] * (N + 1) for _ in range(N + 1)]  # 0이면 연결되어 있지 않다.
    for i in range(E):  # 간선 갯수만큼
        v1, v2, w = map(int, input().split())  # v1에서 v2로 w의 거리
        G[v1][v2] = w  # 일방통행 => 단방향
        # G[v2][v1] = w                         # 양방향
    # print(G)
    dijk(0)