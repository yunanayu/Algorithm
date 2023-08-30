# 최소합
import sys
sys.stdin = open('5188.txt','r')

def solve(r,c,sumV):
    global minV
    if minV < sumV:
        return
    if r==N-1 and c == N-1:
        if minV > sumV:
            minV = sumV
        return
    if r+1 < N:
        solve(r+1,c, sumV+arr[r+1][c])
    if c+1 < N:
        solve(r,c+1,sumV+arr[r][c+1])


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 100000
    solve(0,0,arr[0][0])
    print(f'#{tc} {minV}')
