def subset(i, N, s):
    if i == N:
        if s == 0:
            # print_subset()
            for j in range(N):
                if bit[j]:
                    print(arr[j], end=' ')
            print()
    else:
        subset(i+1, N,s+arr[i])
        subset(i+1, N, s)
    return

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0]*N
subset(0,N)
