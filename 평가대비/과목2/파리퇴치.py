TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cur_max = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            sum_nums = 0
            for i in range(M):
                for j in range(M):
                    sum_nums += arr[r+i][c+j]
            if cur_max < sum_nums:
                cur_max = sum_nums
    print(cur_max)