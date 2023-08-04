# 삼성시의 버스 노선

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cnt = [0] * 5001    # 1번-5000번 각 정류장을 지나는 노선 수 (인덱스를 5000번까지 사용할거기 때문에 5001개 생성하기)
    for _ in range(N):  # N개의 노선에 대해
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt[i] += 1 # 현재 노선이 i번 정류장

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print(bus_stop)
    for x in bus_stop:
        print(f'#{t}', end = ' ')
    print() # tc 바뀔 때 줄바꿈