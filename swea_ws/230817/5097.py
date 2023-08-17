# 회전
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    for i in range(N):
        num_list[i] = num_list[M%N]
    print(f'#{tc}', num_list[0])
