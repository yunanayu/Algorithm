# 숫자 배열 회전

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    # 90도 회전

    arr1 = [[-1] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            arr1[r][c] = arr[N - c - 1][r]


    # 180도 회전
    arr2 = [[-1] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            arr2[r][c] = arr[N-r-1][N-c-1]
    # print(arr2)


    # 270 도 회전

    arr3 = [[-1] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            arr3[r][c] = arr[c][N-r-1]


    print(f'#{tc}')
    for r in range(N):
        print(''.join(arr1[r]), ''.join(arr2[r]), ''.join(arr3[r]))