# 달팽이 숫자

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    d = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    cur_r = cur_c = 0
    arr = [[0]*N for _ in range(N)]
    for i in range(1, N*N+1):
        arr[cur_r][cur_c] = i
        new_r = cur_r + dr[d]
        new_c = cur_c + dc[d]
        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N or arr[new_r][new_c] != 0:
            d = (d + 1) % 4
        cur_r += dr[d]
        cur_c += dc[d]
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])



'''
d = 0 #우 하 왼 상
dr = [0, 1, 0, -1] 
dc = [1, 0, -1, 0]

curR = curC = 0
for value in range(1, N*N+1)
    arr[curR][curC] = value
    
    newR = curR*dr[d]
    newC = curC*dc[d]
        if newR < 0 or newR >= N or newC < 0 or newC >= N or arr[newR][newC] !=0: #새 좌표가 범위를 벗어나면, & 이미 데이터가 들어있으면
            d = (d+1)%4
            # d += 1
            # if d == 4:
            #       d = 0
        curR += dr[d] 
        curC += dc[d]
            
'''