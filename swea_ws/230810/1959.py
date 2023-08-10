# 두 개의 숫자열

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = len(A)
    b = len(B)

    if a > b:
        cur_max = 0
        for i in range(a-b+1):
            sum_list = 0
            for j in range(b):
                sum_list = sum_list + A[i+j] * B[j]
            if cur_max < sum_list:
                cur_max = sum_list
    else:
        cur_max = 0
        for i in range(b - a + 1):
            sum_list = 0
            for j in range(a):
                sum_list = sum_list + B[i + j] * A[j]
            if cur_max < sum_list:
                cur_max = sum_list

    print(f'#{tc} {cur_max}')


        #
        # for i in range(len(A)):
        #     for j in range(len(B)):
        #         arr[i+j] = B[j]
        #     cur_max = 0



