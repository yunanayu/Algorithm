def print_result():
    for i in range(N):
        if result_idx[i]:
            print(arr[i], end=' ')
    print()


def partial(k, curSum):
    if curSum > 10:
        return  # 백트래킹

    if k == N:
        # print(result_idx)
        if curSum == 10:
            print_result()
        return

    result_idx[k] = 0
    partial(k + 1, curSum)

    result_idx[k] = 1
    partial(k + 1, curSum+arr[k])


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
# arr = [5, 3, 2]
arr = [i for i in range(1, 11)]
# print(arr)
result_idx = [-1] * N  # 인덱스 배열
partial(0, 0)
