# [s/w 문제해결 기본] 2일차 - sum
def cur_max(data_list):
    c_max = 0
    for i in data_list:
        if c_max < i:
            c_max = i
    return c_max

TC = 10
N = 100

for tc in range(1, TC+1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    # 각 행 합
    for r in range(N):
        sum_a = 0
        for c in range(N):
            sum_a += arr[r][c]
        sum_list.append(sum_a)
    # 각 열 합
    for c in range(N):
        sum_b = 0
        for r in range(N):
            sum_b += arr[r][c]
        sum_list.append(sum_b)
    # 대각선 합
    sum_c = 0
    for r in range(N):
        sum_c += arr[r][r]
    sum_list.append(sum_c)
    # 반대 대각선 합
    sum_d = 0
    for r in range(N):
        sum_d += arr[r][N-1-r]
    sum_list.append(sum_d)

    sum_max = cur_max(sum_list)
    print(f'#{tc} {sum_max}')