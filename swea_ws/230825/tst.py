TC = int(input())
for tc in range(TC):
    C, R = map(int, input().split())
    K = int(input())

    arr = [[0] * (C) for _ in range(R)]
    # print(arr)
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    d = 0
    cur_r, cur_c = 0, 0
    for i in range(1,R*C+1):
        # if i == K:
        #     print(cur_c+1,cur_r+1)
        #     break
        arr[cur_r][cur_c] = i
        nr, nc = cur_r+dr[d] , cur_c+dc[d]
        if  0 > nr or nr >= R or 0 > nc or nc>=C or arr[nr][nc] != 0:
            d = (d+1)%4
        cur_r, cur_c = cur_r+dr[d], cur_c+dc[d]
    print(arr)