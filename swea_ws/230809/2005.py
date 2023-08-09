# 파스칼의 삼각형

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = []
    for n in range(1, N+1):
        t = [1] * n
        arr.append(t)
    for r in range(N):
        for c in range(1, len(arr[r])-1):
            if r-1 >= 0 and c-1 >= 0:
                arr[r][c] = arr[r-1][c-1] + arr[r-1][c]
    print(f'#{tc}')
    for r in range(N):
        print(*arr[r])









    #
    #
    #
    # # print(t_list)
    # for r in range(N):
    #     for c in range(len(arr[r])):
    #         for i in range(len)
    #         arr[r][c]
    #
    #
    #
    #














