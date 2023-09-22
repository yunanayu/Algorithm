# 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open('input.txt','r')

def num(r, c, number):
    if len(number) == 7:
        result.append(number)
        return

    for k in range(4):
        nr, nc = r+dr[k], c+dc[k]
        if 0<=nr<4 and 0<=nc<4:
            num(nr, nc, number+arr[nr][nc])



T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    # print(arr)
    result = []
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for r in range(4):
        for c in range(4):
            num(r, c, arr[r][c])
    result = set(result)
    print(f'#{tc}',len(result))