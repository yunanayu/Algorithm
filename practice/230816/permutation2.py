def partial(k):
    if k == N:
        print(result_idx)
        sumV = 0
        for i in range(N):
            if result_idx[i]:
                print(arr[i], end=' ')
                sumV += arr[i]
        print(sumV)     # 최대값 등 찾을때 여기서 찾으면 됨
        
        return

    result_idx[k] = 0
    partial(k+1)

    result_idx[k] = 1
    partial(k+1)

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 3
arr = [i for i in range(1, 11)]
# print(arr)
result_idx = [-1] * N   # 인덱스 배열
partial(0)