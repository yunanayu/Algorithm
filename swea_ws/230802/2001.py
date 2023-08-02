# 파리 퇴치
def cur_max(data_list):
    c_max = 0
    for i in data_list:
        if c_max < i:
            c_max = i
    return c_max

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            sum_arr = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    sum_arr = sum_arr + arr[i][j]
            sum_list.append(sum_arr)
    sum_max = cur_max(sum_list)
    print(f'#{tc} {sum_max}')


            # print(arr[r][c])

            # sum_arr = 0
            # for i in range(N-2):
            #     for j in range(M):
            #         for k in range(M):
            #             sum_arr = sum_arr + arr[i+j][i+k]
            #     sum_list.append(sum_arr)

    # sum_max = cur_max(sum_list)
    # print(f'#{tc} {sum_max}')



    # for r in range(N-1):
    #     arr_sum = 0
    #     for r1 in range(M):
    #         for c in range(M):
    #             arr_sum += arr[r+r1][r+c]
    #     sum_list.append(arr_sum)
    # sum_max = cur_max(sum_list)
    # print(f'#{tc} {sum_max}')

'''
#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242

'''

