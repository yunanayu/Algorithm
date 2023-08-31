def b(counts_A, counts_B):
    global result_A
    global result_B
    i = 0

    while i <= (len(counts_A) - 1):
        if counts_A[i] >= 3:
            result_A = 1
            return
        elif counts_B[i] >= 3:
            result_B = 1
            return
        if i <= (len(counts_A) - 3):
            if counts_A[i] != 0 and counts_A[i + 1] != 0 and counts_A[i + 2] != 0:
                result_A = 1
                return
            elif counts_B[i] != 0 and counts_B[i + 1] != 0 and counts_B[i + 2] != 0:
                result_B = 1
                return
        i += 1
    return


TC = int(input())
for tc in range(1, TC + 1):
    num_list = list(map(int, input().split()))
    N = len(num_list)
    counts_A = [0] * 10
    counts_B = [0] * 10
    result_A = 0
    result_B = 0
    for i in range(0, N - 1, 2):
        counts_A[num_list[i]] += 1
        counts_B[num_list[i + 1]] += 1
        if i >= 6:
            b(counts_A, counts_B)
            if result_A == 1:
                print(f'#{tc}', 1)
                break
            elif result_B == 1:
                print(f'#{tc}', 2)
                break

    else:

        print(f'#{tc}', 0)