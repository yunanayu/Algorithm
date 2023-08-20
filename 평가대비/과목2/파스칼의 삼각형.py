TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = []
    for n in range(1, N+1):
        arr.append([1] * n)

    for r in range(2, N):
        for c in range(1, len(arr[r])-1):
            # if 0 <= r-1 < N and 0 <= c-1 <N:
            arr[r][c] = arr[r-1][c-1] + arr[r-1][c]
    for i in range(N):
        print(*arr[i])